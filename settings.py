class Settings():
    """Класс для хранения настроек игры"""

    def __init__(self):
        """Инициализация настроек игры"""
        # Параметры экрана
        self.screen_width = 1400
        self.screen_height = 800
        self.bg_color = (30, 255, 30)
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Параметры пули
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 0, 255

        # Настройки пришельцев
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1



