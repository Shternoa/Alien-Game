import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''Класс для управления пулями'''

    def __init__(self, al_inv_settings, screen, ship):
        """Создает пулю в корабле"""
        super().__init__()
        self.screen = screen

        # Создание пули в позиции (0,0) и позицонирование её
        self.rect = pygame.Rect(0, 0, al_inv_settings.bullet_width, al_inv_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = al_inv_settings.bullet_color
        self.speed = al_inv_settings.bullet_speed

    def update(self):
        """Полет пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_a_bullet(self):
        """Показывает пулю"""
        pygame.draw.rect(self.screen, self.color, self.rect)
