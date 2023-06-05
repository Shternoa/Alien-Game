class Settings():
    """Класс для хранения настроек игры"""

    def __init__(self):
        """Инициализация настроек игры"""
        # Параметры экрана
        self.screen_width = 1400
        self.screen_height = 800
        self.bg_color = (30, 255, 30)
        self.ship_limit = 3

        # Параметры пули
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 0, 255

        # Настройки пришельцев
        self.speed_scale = 1.2
        self.scale_settings()

    def scale_settings(self):
        self.ship_speed = 1.5
        self.alien_speed = 1
        self.fleet_direction = 1
        self.fleet_drop_speed = 10
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speed_scale
        self.alien_speed *= self.speed_scale
        self.fleet_direction *= self.speed_scale
