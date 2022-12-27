import pygame

class Bird:
    """Class for storing Bird settings"""

    def __init__(self, ai_game):
        """Initialize Bird and set it's position to the middle of the screen"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        #Load Bird image
        self.image_size = (50, 50)
        self.image = pygame.image.load('images/bird.png')
        self.image = pygame.transform.scale(self.image, self.image_size)
        self.rect = self.image.get_rect()

        #Starting the bird in the middle
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the Bird at the current location"""
        self.screen.blit(self.image, self.rect)