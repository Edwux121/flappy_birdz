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
        #Limiting the speed of the game
        self.fps = 60
        self.clock = pygame.time.Clock()
        while True:
            self.clock.tick(60)
            self._check_events()
            self._bird_movement()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self._bird_movement_add()

    def _update_screen(self):
        """Updating the screen"""
        #Drawing display
        self.screen.fill(self.settings.bg_color) 
        self.bird.blitme()  
        pygame.display.flip()

    def _bird_movement(self):
        """Function for bird movement"""
        #Get dimensions of the screen
        self.screen_info = pygame.display.Info()
        self.screen_width = self.screen_info.current_w
        self.screen_height = self.screen_info.current_h

        self.bird.rect.y += 2
        #Checking if the Bird has reached the Bottom of the screen
        self.bird.rect.clamp_ip(pygame.Rect(0, 0, self.screen_width, self.screen_height))

    def _bird_movement_add(self):
        """After pressing the spacebar makes the bird go up"""
        self.bird.rect.y -= 100

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = Main()
    ai.run_game()