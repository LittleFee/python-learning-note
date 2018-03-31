class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1024
        self.screen_height = 640
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
