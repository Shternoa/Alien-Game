import sys

import pygame

from settings import Settings
from ship import Ship
import game_function as game_func
from pygame.sprite import Group


def run_game():
    '''Инициализация игры c объектами на экране'''
    pygame.init()
    al_inv = Settings()
    screen = pygame.display.set_mode((al_inv.screen_width, al_inv.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(al_inv, screen)
    bullets = Group()

    # Запуск основного цикла игры
    while True:
        # Отслеживание клавиатуры и мышки
        game_func.check_events(al_inv, screen, ship, bullets)
        ship.update()
        bullets.update()
        #Удаление пуль
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
            #print(len(bullets))
        # Перерисовываем экран в другой цвет
        game_func.update_screen(al_inv, screen, ship, bullets)


run_game()
