# Import the pygame module
import pygame

# Import random for random numbers
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
# from pygame.locals import *
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_a,
    KEYDOWN,
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
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        ## Keep player on the screen
        #if self.rect.left < 0:
        #    self.rect.left = 0
        #elif self.rect.right > SCREEN_WIDTH:
        #    self.rect.right = SCREEN_WIDTH
        #if self.rect.top <= 0:
        #    self.rect.top = 0
        #elif self.rect.bottom >= SCREEN_HEIGHT:
        #    self.rect.bottom = SCREEN_HEIGHT

# Define the enemy object extending pygame.sprite.Sprite
# The surface we draw on the screen is now a property of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the enemy based on speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Define the cloud object extending pygame.sprite.Sprite
# Use an image for a better looking sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the cloud based on a constant speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


# Initialize pygame
pygame.init()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Create our 'player'
player = Player()
enemies = pygame.sprite.Group()
#clouds = pygame.sprite.Group()

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

#ADDCLOUD = pygame.USEREVENT + 2
#pygame.time.set_timer(ADDCLOUD, 1000)

#pygame.mixer.init()
#pygame.mixer.music.load("pozadie.mp3")
#pygame.mixer.music.play(loops=-1)

#collision_sound = pygame.mixer.Sound("zrazka.ogg")
#collision_sound.set_volume(0.5)

running = True
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_a:
                new_enemy = Enemy()
                enemies.add(new_enemy)
        # Did the user click the window close button? If so, stop the loop
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
        #elif event.type == ADDCLOUD:
        #    new_cloud = Cloud()
        #    clouds.add(new_cloud)


    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    #clouds.update()

    # Fill the screen with sky blue
    screen.fill((135, 206, 250))

    # Draw all our sprites
    screen.blit(player.surf, player.rect)
    for enemy in enemies:
        screen.blit(enemy.surf, enemy.rect)
    #for cloud in clouds:
    #    screen.blit(cloud.surf, cloud.rect)

    #if pygame.sprite.spritecollideany(player, enemies):
    #    #pygame.mixer.music.stop()
    #    #collision_sound.play()
    #    player.kill()
    #    running = False

    # Flip everything to the display
    pygame.display.flip()
    clock.tick(30)

# Done! Time to quit.
#pygame.mixer.quit()
pygame.quit()
