class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализируем настройки игры."""
        self.screen_width = 900
        self.screen_height = 500
        self.bg_color = (89, 102, 105)
        # self.ship_speed_factor = 1.5
        # Количество жизней коробля
        self.ship_limit = 3
        # Параметры пули
        # self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 5
        # Настройка пришельцев
        # self.alien_speed_factor = 0.01
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение в право, а -1 - влево.
        # self.fleet_direction = 1
        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        # настройки пуль пришельцев
        self.nachala_time = 0
        self.time_puli_nlo = 2
        self.bulletNLO_width = 9
        self.bulletNLO_height = 9
        self.bulletNLO_color = (255, 5, 5)
        self.kol_strelyuchih = 2
        # Блоки
        self.kol_bloka_v_vryd = 7

    def initialize_dynamic_settings(self):
        """Инициализируем настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 0.1
        self.bullet_speed_factor = 0.09
        self.alien_speed_factor = 0.01
        # fleet_direction = 1 обозначает движение в право, а -1 - влево.
        self.fleet_direction = 1
        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимости пришельцев."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
