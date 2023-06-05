import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as game_func
from pygame.sprite import Group
from game_stats import Game_Stats
from button import Button


def run_game():
    '''Инициализация игры c объектами на экране'''
    pygame.init()
    al_inv_settings = Settings()
    screen = pygame.display.set_mode((al_inv_settings.screen_width, al_inv_settings.screen_height))
    ship = Ship(al_inv_settings, screen)
    bullets = Group()
    aliens = Group()
    game_func.create_fleet(al_inv_settings, screen, ship, aliens)
    stats = Game_Stats(al_inv_settings)

    pygame.display.set_caption('Alien Invasion')
    play_button = Button(al_inv_settings, screen, 'Play')

    # Запуск основного цикла игры
    while True:
        # Отслеживание клавиатуры и мышки
        game_func.check_events(al_inv_settings, screen, stats, play_button, ship, bullets, )
        if stats.game_active:
            ship.update()
            bullets.update()
            ship.shipdraw()
            game_func.update_bullets(al_inv_settings, screen, ship, aliens, bullets)
            game_func.update_aliens(al_inv_settings, stats, screen, ship, aliens, bullets)
        game_func.update_screen(al_inv_settings, screen, stats, ship, aliens, bullets, play_button)
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


run_game()
