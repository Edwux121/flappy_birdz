class Settings:
    """Class for storing game settings"""

    def __init__(self):
        """Initialize game settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Obsticle settings
        self.cube_speed = 3
        self.cube_width = 100
        self.cube_height = 500
        self.cube_color = (0, 255, 0)