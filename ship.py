import pygame


class Ship():
    def __init__(self, al_inv_settings, screen):
        """Инициализация коробля с его начальной позицией"""
        self.screen = screen
        self.al_inv_settings = al_inv_settings

        #
        self.image = pygame.image.load(r'C:\Users\evilp\PycharmProjects\Study2\Alien Game\images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновление позиции корабля"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.al_inv_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.al_inv_settings.ship_speed
        self.rect.centerx = self.center

    def shipdraw(self):
        """Рисует корабль"""
        self.screen.blit(self.image, self.rect)
