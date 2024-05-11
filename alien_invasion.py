import pygame
from pygame.sprite import Group
import time
from time import sleep

from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
# from blok import Blok


def run_game():
    # Загружаем (pygame.mixer)
    pygame.mixer.pre_init(44100, -16, 1, 512)
    # Инициализирует игру и создает обьект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # Создание космо коробля
    ship = Ship(ai_settings, screen)
    # Создание пули для хранения пуль.
    bullets = Group()
    # Создание пуль пришельцев
    bulletsNLO = Group()
    # Создание пришельца.
    # alien = Alien(ai_settings, screen)
    # Создание групы пришельцев.
    aliens = Group()
    # Создание Флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Создаём экзмпляр для хранения игровой статистики.
    stats = GameStats(ai_settings)
    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, "Игра")
    # Создание экземпляров GameStats и Scoreboard.
    sb = Scoreboard(ai_settings, screen, stats)
    # запускаем фоновую музыку
    gf.sours_fon('sound/fon_01.wav')
    sleep(2.6)
    # Звуковой эфект Пули
    spulya = pygame.mixer.Sound('sound/ship_pula.wav')
    # Взрыв пришельца
    soundnlo = pygame.mixer.Sound('sound/nlo_vzriv.wav')
    # Время для отчёта стрельбы пришельцев
    ai_settings.nachala_time = time.time()
    # Создаю группу преград меджу пришельцами и кораблём
    metiorits = Group()

    while True:  # Запуск основной цикла игры.
        # Отслеживаем события клавиатуры и мыши
        gf.check_events(ai_settings, screen, stats, sb,
                        play_button, ship, bullets, aliens, spulya, metiorits)
        if stats.game_active:
            # отсчитываем сколько прошло времени чтоб отоковать пришельцу
            gf.vistrel_nlo(ai_settings, aliens, screen, ship, bulletsNLO)
            # Обновление нажатий клавиш
            ship.update()
            # Обновление позиции пуль и уничтожает старые пули
            gf.update_bullets(
                ai_settings, screen, stats, sb, ship, aliens, bullets
            )
            # Обновляем позиции пуль пришельцев
            gf.update_bulletsNLO(
                ai_settings, screen, stats, sb, ship, aliens, bulletsNLO
            )
            # Обработка колизий удалять сталкнувшихся пуль с пришельцами
            gf.check_bullet_alien_collisions(
                ai_settings, screen, stats, sb, ship, aliens,
                bullets, soundnlo, bulletsNLO
            )
            # Проверка столкновений с блоком и пулей пришельца
            gf.check_bulletNLO_blok_collisions(
                ai_settings, screen, stats, sb, ship, aliens,
                bullets, soundnlo, bulletsNLO, metiorits
            )
            # Проверка столкновений пуль коробля с блоком
            gf.check_ship_blok_collisions(
                ai_settings, screen, stats, sb, ship, aliens,
                bullets, soundnlo, bulletsNLO, metiorits
            )
            # Обновление позиции пришельцев
            gf.update_aliens(
                ai_settings, screen, stats, sb, ship, aliens, bullets
            )

        # Обновляет изображения на экране и отображает новый экран.
        gf.update_screen(
            ai_settings, screen, stats, sb, ship, aliens,
            bullets, play_button, bulletsNLO, metiorits
        )


run_game()
