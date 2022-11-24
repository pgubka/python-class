# Import the pygame module
import pygame

from pygame.locals import (
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user click the window close button? If so, stop the loop
        if event.type == QUIT:
            running = False

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    #player.update(pressed_keys)

    # Fill the screen with sky blue
    #screen.fill((135, 206, 250))

    # Draw all our sprites
    #for entity in all_sprites:
    #screen.blit(entity.surf, entity.rect)
    #screen.blit(player.surf, player.rect)

    # Flip everything to the display
    pygame.display.flip()
    clock.tick(30)

# Done! Time to quit.
pygame.quit()
