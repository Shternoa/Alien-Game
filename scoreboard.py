import pygame


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

    def prepare_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.al_inv_settings.bg_color)

        # Вывод счета
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
