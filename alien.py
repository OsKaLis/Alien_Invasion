import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс, представляющего одного пришельца."""
    def __init__(self, ai_settings, screen):
        """Иницилизируем пришельца и задает его начальную позицию."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрусска изображения пришельца и назначения атрибута rect.
        self.image = pygame.image.load('images/m_prishelec_compress.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точности позиции пришельца.
        self.x = float(self.rect.x)

    def blitme(self):
        """Выводит пришельца в текущем положении."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Перемещает пришельца влево или вправо."""
        alien_speed_factor = self.ai_settings.alien_speed_factor
        fleet_direction = self.ai_settings.fleet_direction
        self.x += (alien_speed_factor * fleet_direction)
        self.rect.x = self.x
