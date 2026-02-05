# Tasks todo:
# - enable  "esc" pressed
# - change sky color
# - enable player
# - make it not to be square
# - implement moving player

# Import the pygame module
import pygame

# Import random for random numbers
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
# from pygame.locals import *
from pygame.locals import (
#    RLEACCEL,
#    K_UP,
#    K_DOWN,
#    K_LEFT,
#    K_RIGHT,
#    K_ESCAPE,
#    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Define the Player object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("jet.png").convert()
        #self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on keypresses
    def update(self, pressed_keys):
        pass
        #if pressed_keys[K_UP]:
        #    self.rect.move_ip(0, -5)

# Initialize pygame
pygame.init()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Create our 'player'
#player = Player()

#all_sprites = pygame.sprite.Group()
#all_sprites.add(player)


running = True
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        #if event.type == KEYDOWN:
        #    # Was it the Escape key? If so, stop the loop
        #    if event.key == K_ESCAPE:
        #        running = False

        # Did the user click the window close button? If so, stop the loop
        if event.type == QUIT:
            running = False

    # Get the set of keys pressed and check for user input
    #pressed_keys = pygame.key.get_pressed()
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
