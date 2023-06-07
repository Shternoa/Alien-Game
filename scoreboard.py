import pygame

from pygame.sprite import Group
from ship import Ship


class Scoreboard():
    """Вывод цифровой инфы"""

    def __init__(self, al_inv_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.al_inv_settings = al_inv_settings
        self.stats = stats

        # Настройка отображения
        self.text_color = (50, 50, 50)
        self.font = pygame.font.SysFont(None, 48)

        self.prepare_score()
        self.prepare_high_score()
        self.prepare_level()
        self.prepare_ships()

    def prepare_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.al_inv_settings.bg_color)

        # Вывод счета
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prepare_high_score(self):
        """Преобразование числа в графическое изображение"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.al_inv_settings.bg_color)

        # Выравнивание

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prepare_level(self):
        """Прербразование числа уровня в графическое изображение"""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.al_inv_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left
        self.level_rect.top = self.screen_rect.top

    def prepare_ships(self):
        """Количество оставшихся кораблей в изображениях"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.al_inv_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
