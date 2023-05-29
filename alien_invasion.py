import sys

import pygame

from settings import Settings
from ship import Ship
import game_function as game_func


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
        game_func.check_events()
        # Перерисовываем экран в другой цвет
        game_func.update_screen(al_inv, screen, ship)


run_game()
