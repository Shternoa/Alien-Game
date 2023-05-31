class Settings():
    """Класс для хранения настроек игры"""

    def __init__(self):
        """Инициализация настроек игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 900
        self.bg_color = (50, 50, 255)
        self.ship_speed = 1.5
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 255, 0)

