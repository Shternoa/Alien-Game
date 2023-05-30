import sys

import pygame


def check_events(ship):
    # Отслеживание клавиатуры и мышки
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(al_inv_settings, screen, ship):
    """Обновление изображения и его отображение"""
    # Перерисовываем экран в другой цвет
    screen.fill(al_inv_settings.bg_color)
    ship.shipdraw()
    # Показывает последний прорисованный экран
    pygame.display.flip()

