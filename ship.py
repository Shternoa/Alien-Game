import pygame


class Ship():
    def __init__(self, screen):
        """Инициализация коробля с его начальной позицией"""
        self.screen = screen

        #
        self.image = pygame.image.load(r'C:\Users\evilp\PycharmProjects\Study2\Alien Game\images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def shipdraw(self):
        """Рисует корабль"""
        self.screen.blit(self.image, self.rect)

