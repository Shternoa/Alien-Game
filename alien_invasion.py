import sys

import pygame

from settings import Settings
from ship import Ship
import game_function as game_func
from pygame.sprite import Group
from alien import Alien


def run_game():
    '''Инициализация игры c объектами на экране'''
    pygame.init()
    al_inv = Settings()
    screen = pygame.display.set_mode((al_inv.screen_width, al_inv.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(al_inv, screen)
    bullets = Group()
    aliens = Group()
    game_func.create_fleet(al_inv, screen, ship, aliens)

    # Запуск основного цикла игры
    while True:
        # Отслеживание клавиатуры и мышки
        game_func.check_events(al_inv, screen, ship, bullets)
        ship.update()
        game_func.update_bullets(bullets)
        game_func.update_aliens(aliens)
        # Перерисовываем экран в другой цвет
        game_func.update_screen(al_inv, screen, ship, aliens, bullets)


run_game()
