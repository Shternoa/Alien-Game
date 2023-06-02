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


def fire_bullets(al_inv_settings, screen, ship, bullets):
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


def update_screen(al_inv_settings, screen, ship, aliens, bullets):
    """Обновление изображения и его отображение"""
    # Перерисовываем экран в другой цвет
    screen.fill(al_inv_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_a_bullet()
    ship.shipdraw()
    aliens.draw(screen)
    # Показывает последний прорисованный экран
    pygame.display.flip()


def update_bullets(al_inv_setting, screen, ship, aliens, bullets):
    bullets.update()
    # Удаление пуль, вышедших за край экрана.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(al_inv_setting, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(al_inv_setting, screen, ship, aliens, bullets):
    """Обработка коллизий пуль с пришельцами."""
    # Удаление пуль и пришельцев, участвующих в коллизиях.

    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    if len(aliens) == 0:
        # Уничтожение существующих пуль и создание нового флота.
        bullets.empty()
        create_fleet(al_inv_setting, screen, ship, aliens)


def get_number_of_aliens_x(al_inv_settings, alien_width):
    """Колво пришельцев в ряду"""
    available_screen_space_x = al_inv_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_screen_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(al_inv_settings, screen, aliens, alien_number, row_number):
    alien = Alien(al_inv_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(al_inv_settings, screen, ship, aliens):
    """Флот из пришельцев"""
    """Создает флот пришельцев."""

    # Создание пришельца и вычисление количества пришельцев в ряду.
    alien = Alien(al_inv_settings, screen)
    number_aliens_x = get_number_of_aliens_x(al_inv_settings, alien.rect.width)
    number_rows = get_number_of_rows(al_inv_settings, ship.rect.height, alien.rect.height)

    # Создание флота пришельцев.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(al_inv_settings, screen, aliens, alien_number,
                         row_number)


def get_number_of_rows(al_inv_settings, ship_height, alien_height):
    """Колво рядов помещения"""
    available_screen_space_y = (al_inv_settings.screen_height - (2 * alien_height) - ship_height)
    number_of_rows = int(available_screen_space_y / (2 * alien_height))
    return number_of_rows


def check_fleet_edges(al_inv_settings, aliens):
    """Достижение края"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(al_inv_settings, aliens)
            break


def change_fleet_direction(al_inv_settings, aliens):
    """Флот опускается и меняет направление"""
    for alien in aliens.sprites():
        alien.rect.y += al_inv_settings.fleet_drop_speed
    al_inv_settings.fleet_direction *= -1


def update_aliens(ai_settings, ship, aliens):
    """Обновляет позиции всех пришельцев во флоте."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # Проверка коллизий "пришелец-корабль".
    # if pygame.sprite.spritecollideany(ship, aliens):
    #     print("Ship hit!!!")
