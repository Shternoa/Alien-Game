import sys

import pygame

from bullet import Bullet
from alien import Alien


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
        fire_bullets(al_inv_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(al_inv_settings, screen, ship, aliens, bullets):
    """Обновление изображения и его отображение"""
    # Перерисовываем экран в другой цвет
    screen.fill(al_inv_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_a_bullet()
    ship.shipdraw()
    for alien in aliens.sprites():
        alien.alien_draw()
    # Показывает последний прорисованный экран
    pygame.display.flip()


def fire_bullets(al_inv_settings, screen, ship, bullets):
    new_bullet = Bullet(al_inv_settings, screen, ship)
    bullets.add(new_bullet)


def update_bullets(bullets):
    bullets.update()
    # Удаление пуль
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        # print(len(bullets))


def get_number_of_rows(al_inv_settings, ship_height, alien_height):
    """Колво рядов помещения"""
    available_screen_space_y = (al_inv_settings.screen_height - (2 * alien_height) - ship_height)
    number_of_rows = int(available_screen_space_y / (2 * alien_height))
    return number_of_rows


def get_number_of_aliens_x(al_inv_settings, alien_width):
    """Колво пришельцев в ряду"""
    available_screen_space_x = al_inv_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_screen_space_x / (2 * alien_width))
    return number_aliens_x


def creat_alien(al_inv_settings, screen, aliens, alien_number, row_number):
    alien = Alien(al_inv_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(al_inv_settings, screen, ship, aliens):
    """Флот из пришельцев"""
    alien = Alien(al_inv_settings, screen)
    number_aliens_x = get_number_of_aliens_x(al_inv_settings, alien.rect.width)
    number_of_rows = get_number_of_rows(al_inv_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_of_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(al_inv_settings, screen, aliens, alien_number, row_number)

def update_aliens(aliens):
    """Обновление пришельцев"""
    aliens.update()
