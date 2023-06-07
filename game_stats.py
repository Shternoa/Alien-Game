import json


class Game_Stats():

    def __init__(self, al_inv_settings):
        """ Статистика """
        self.al_inv_settings = al_inv_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
        self.load_high_score()

    def reset_stats(self):
        """Изменение статистики в течении игры"""
        self.ship_left = self.al_inv_settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """Сохранение рекорда в файл"""
        with open('high_score.txt', 'w') as file:
            json.dump(self.high_score, file)

    def load_high_score(self):
        """Загрузка файла"""
        try:
            with open('high_score.txt') as file:
                self.high_score = json.load(file)
        except FileNotFoundError:
            self.high_score = 0

