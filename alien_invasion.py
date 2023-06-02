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
    al_inv_settings = Settings()
    screen = pygame.display.set_mode((al_inv_settings.screen_width, al_inv_settings.screen_height))
    ship = Ship(al_inv_settings, screen)
    bullets = Group()
    aliens = Group()
    game_func.create_fleet(al_inv_settings, screen, ship, aliens)
    alien = Alien(al_inv_settings, screen)

    pygame.display.set_caption('Alien Invasion')

    # Запуск основного цикла игры
    while True:
        # Отслеживание клавиатуры и мышки
        game_func.check_events(al_inv_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        game_func.update_screen(al_inv_settings, screen, ship, aliens, bullets)
        ship.shipdraw()
        game_func.update_bullets(al_inv_settings, screen, ship, aliens, bullets)
        game_func.update_aliens(al_inv_settings, ship, aliens)
        game_func.update_screen(al_inv_settings, screen, ship, aliens, bullets)
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


run_game()
