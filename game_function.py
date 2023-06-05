import sys

import pygame

from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, al_inv_settings, screen, stats, ship, aliens, bullets):
    """Реагированиеи нажатия клавиш"""
    if event.key == pygame.K_p:
        start_game(al_inv_settings, screen, stats, ship, aliens, bullets)
    elif event.key == pygame.K_RIGHT:
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


def check_events(al_inv_settings, screen, stats, play_button, ship, aliens, bullets):
    # Отслеживание клавиатуры и мышки
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_1, mouse_2 = pygame.mouse.get_pos()
            check_play_button(al_inv_settings, screen, stats, play_button, ship, aliens, bullets, mouse_1, mouse_2)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, al_inv_settings, screen, stats, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_play_button(al_inv_settings, screen, stats, play_button, ship, aliens, bullets, mouse_1, mouse_2):
    """Запуск новой игры при нажатии"""
    button_click = play_button.rect.collidepoint(mouse_1, mouse_2)
    if button_click and not stats.game_active:
        pygame.mouse.set_visible(False)
        # Сброс игровой статистики
        start_game(al_inv_settings, screen, stats, ship, aliens, bullets)


def start_game(al_inv_settings, screen, stats, ship, aliens, bullets):
    stats.reset_stats()
    stats.game_active = True

    aliens.empty()
    bullets.empty()

    create_fleet(al_inv_settings, screen, ship, aliens)
    ship.center_ship()


def update_screen(al_inv_settings, screen, stats, ship, aliens, bullets, play_button):
    """Обновление изображения и его отображение"""
    # Перерисовываем экран в другой цвет
    screen.fill(al_inv_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_a_bullet()
    ship.shipdraw()
    aliens.draw(screen)
    # Если игра активна, то кнопка не появится
    if not stats.game_active:
        play_button.draw_button()
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


def ship_hit(al_inv_settings, stats, screen, ship, aliens, bullets):
    """Столкновение с короблем"""
    if stats.ship_left > 0:
        stats.ship_left -= 1

        # Очистка пришельцев с пулями
        aliens.empty()
        bullets.empty()

        # Новый флот
        create_fleet(al_inv_settings, screen, ship, aliens)
        ship.center_ship()

        # Задержка
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        # sys.exit()


def update_aliens(al_inv_settings, stats, screen, ship, aliens, bullets):
    """Обновляет позиции всех пришельцев во флоте."""
    check_fleet_edges(al_inv_settings, aliens)
    aliens.update()
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(al_inv_settings, stats, screen, ship, aliens, bullets)
        # Проверка коллизий "пришелец-корабль".
        elif pygame.sprite.spritecollideany(ship, aliens):
            ship_hit(al_inv_settings, stats, screen, ship, aliens, bullets)
