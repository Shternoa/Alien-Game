class Game_Stats():

    def __init__(self, al_inv_settings):
        """ Статистика """
        self.al_inv_settings = al_inv_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Изменение статистики в течении игры"""
        self.ship_left = self.al_inv_settings.ship_limit
