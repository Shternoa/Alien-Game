import sys

import pygame

from bullet import Bullet


def check_keydown_events(event, al_inv_settings, screen, ship, bullets):
    """Реагированиеи нажатия клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # Создание пули
        new_bullet = Bullet(al_inv_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Реакция на прекращения нажатия"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(al_inv_settings, screen, ship, bullets):
    # Отслеживание клавиатуры и мышки
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, al_inv_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(al_inv_settings, screen, ship, bullets):
    """Обновление изображения и его отображение"""
    # Перерисовываем экран в другой цвет
    screen.fill(al_inv_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_a_bullet()
    ship.shipdraw()
    # Показывает последний прорисованный экран
    pygame.display.flip()
