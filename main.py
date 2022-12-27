import sys
import pygame

from settings import Settings
from bird import Bird

class Main:
    """Class for managing the behavior of the app"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        #Starting the PyGame
        pygame.init()

        #Load Settings
        self.settings = Settings()
        #Setting display height and width
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Flappy birdz")

        #Calling the Bird
        self.bird = Bird(self)

    def run_game(self):
        """Running the game"""
        while True:
            #Watching for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Drawing display
            self.screen.fill(self.settings.bg_color) 
            self.bird.blitme()  
            pygame.display.flip()


if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = Main()
    ai.run_game()