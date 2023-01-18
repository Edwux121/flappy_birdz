import sys
import pygame

from settings import Settings
from bird import Bird
from cube import Cube

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

        #Calling the Bird/Cube
        self.bird = Bird(self)
        self.new_cube = Cube(self)
        self.cube = pygame.sprite.Group()

        #Creating a timer for the obsticle to spawn
        pygame.time.set_timer(pygame.USEREVENT, 1500)
        

    def run_game(self):
        """Running the game"""
        #Limiting the speed of the game
        self.fps = 60
        self.clock = pygame.time.Clock()
        
        while True:
            self.clock.tick(60)
            self._check_events()
            self._bird_movement()
            self._create_cube()
            self._update_cube()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #Checking the space button press, if pressed move the bird up
                    self.bird.rect.y -= 100
            elif event.type == pygame.USEREVENT:
                #Spawning new obsticle after the timer goes off
                self._new_cube()

    def _bird_movement(self):
        """Function for bird movement"""
        #Get dimensions of the screen
        self.screen_info = pygame.display.Info()
        self.screen_width = self.screen_info.current_w
        self.screen_height = self.screen_info.current_h

        #Makes bird always go down
        self.bird.rect.y += 2

        #Checking if the Bird has reached the Bottom of the screen
        self.bird.rect.clamp_ip(pygame.Rect(0, 0, self.screen_width, self.screen_height))

    def _create_cube(self):
        """Function to draw cube"""
        self.cube.add(self.new_cube)

    def _new_cube(self):
        """Class for creating additional cubes after the event executed"""
        new_cube = Cube(self)
        self.cube.add(new_cube)

    def _update_cube(self):
        """Updates position of the obsticle"""
        self.cube.update()
        #Getting rid of cubes that go behind the screen
        for cube in self.cube.copy():
            if cube.rect.left <=0:
                self.cube.remove(cube)

    def _update_screen(self):
        """Updating the screen"""
        #Drawing display
        self.screen.fill(self.settings.bg_color) 
        self.bird.blitme()
        #Printing each cube from sprites list
        for cube in self.cube.sprites():
            cube.draw_cube()
        pygame.display.flip()


if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = Main()
    ai.run_game()