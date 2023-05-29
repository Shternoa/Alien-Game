import pygame


class Ship():
    def __init__(self, screen):
        """Инициализация коробля с его начальной позицией"""
        self.screen = screen

        #
        self.image = pygame.image.load('b0c34caf4d3814d69143af5bba2ce6d8.bmp')
        self.rect = self.image.get_rect()
        #
        self.rect.centerx = self.screen_center.centrex
        self.rect.bottom = self.screen_bottom.bottom

    def shipdraw(self):
        """Рисует корабль"""
        self.screen.draw(self.image, self.rect)
