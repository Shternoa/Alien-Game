import sys

import pygame


def run_game():
    '''Инициализация игры c объектами на экране'''
    pygame.init()
    screen = pygame.display.set_mode((1200, 900))
    pygame.display.set_caption('Alien Invasion')

    # Запуск основного цикла игры
    while True:
        # Отслеживание клавиатуры и мышки
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Показывает последний прорисованный экран
        pygame.display.flip()


run_game()
