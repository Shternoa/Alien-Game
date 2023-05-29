import sys

import pygame

from settings import Settings
from ship import Ship


def run_game():
    '''Инициализация игры c объектами на экране'''
    pygame.init()
    al_inv = Settings()
    screen = pygame.display.set_mode((al_inv.screen_width, al_inv.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen)

    # Запуск основного цикла игры
    while True:
        # Отслеживание клавиатуры и мышки
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Перерисовываем экран в другой цвет
        screen.fill(al_inv.bg_color)
        # Показывает корабль
        ship.shipdraw()
        # Показывает последний прорисованный экран
        pygame.display.flip()


run_game()
