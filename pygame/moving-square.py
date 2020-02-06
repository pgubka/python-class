# Simple pygame program (compiled from https://realpython.com/pygame-a-primer/#images-and-rects)
# docs: https://devdocs.io/pygame/
# Import and initialize the pygame library

import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
color=(255,0,0)
x=30
y=30


clock=pygame.time.Clock()
# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]: x+=3
    if pressed[pygame.K_LEFT]: x-=3
    if pressed[pygame.K_UP]: y-=3
    if pressed[pygame.K_DOWN]: y+=3

    # Fill the background with white
    screen.fill((255, 255, 255))
    # Draw a solid blue circle in the center
    pygame.draw.rect(screen, color, pygame.Rect(x,y,60,60))

    # Flip the display
    pygame.display.flip()
    clock.tick(10)

# Done! Time to quit.
pygame.quit()
