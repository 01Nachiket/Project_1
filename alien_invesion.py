import sys
import pygame
from Settings import settings
import self

#here it will just create blank card with ship image
class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        # Set the background color.
        self.bg_color = (230, 230, 230)


def run_game():
    """Start the main loop for the game."""

    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)
            # Make the most recently drawn screen visible.
            pygame.display.flip()

        if __name__ == '__main__':
            ai = AlienInvasion()
            ai.run_game()
            
# The ship crreation part ends here
