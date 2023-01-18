import pygame
from pygame.sprite import Sprite
import random

class Cube(Sprite):
    """Class for creating an obsticle"""

    def __init__(self, ai_game):
        "Creating an obsticle on the right of the screen"
        super().__init__()
        
        #Getting screen parameters
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setttings = ai_game.settings
        
        #Getting the cube settings
        self.color = self.setttings.cube_color
        self.cube_left = 0
        self.cube_top = 0
        self.cube_width = 50
        self.cube_height = random.randint(0, 350)

        #Drawing the cube with the settings from the above
        self.rect = pygame.Rect(self.cube_left, self.cube_top, self.cube_width, self.cube_height)
        self.rect_second = pygame.Rect(self.cube_left, self.cube_top, self.cube_width, self.cube_height)

        #Placing the cube at the bottom right
        self.rect.bottomright = self.screen_rect.bottomright
        self.rect_second.topright = self.screen_rect.topright

        self.x = float(self.rect.x)
        self.x_second = float(self.rect_second.x)

    def update(self):
        """Update obsticles location"""
        self.x -= self.setttings.cube_speed
        self.x_second -= self.setttings.cube_speed
        self.rect.x = self.x
        self.rect_second.x = self.x


    def draw_cube(self):
        """Drawing the obsticle on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect_second)