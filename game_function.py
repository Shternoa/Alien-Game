import sys

import pygame


def check_events():
    # Отслеживание клавиатуры и мышки
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(al_inv_settings, screen, ship):
    """Обновление изображения и его отображение"""
    # Перерисовываем экран в другой цвет
    screen.fill(al_inv_settings.bg_color)
    ship.shipdraw()
    # Показывает последний прорисованный экран
    pygame.display.flip()
