import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, al_inv_settings, screen):
        """Класс пришелец"""
        super().__init__()
        self.screen = screen
        self.al_inv_settings = al_inv_settings

        # Загрузка изображения пришельца
        self.image = pygame.image.load(r'C:\Users\evilp\PycharmProjects\Study2\Alien Game\images\gina.bmp')
        self.rect = self.image.get_rect()

        # Пришелец появляется в верхнем левом углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Позиция пришельца
        self.x = float(self.rect.x)

    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана."""
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Перемещение вправо или лево"""
        self.x += (self.al_inv_settings.alien_speed * self.al_inv_settings.fleet_direction)
        self.rect.x = self.x

    def alien_draw(self):
        """Вывод пришельца на экран"""
        self.screen.blit(self.image, self.rect)
