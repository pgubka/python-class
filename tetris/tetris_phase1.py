# Import the pygame module
import pygame

from pygame.locals import (
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


#def draw_text_middle(text, size, color, surface):
#    font = pygame.font.SysFont("comicsans", size, bold=True)
#    label = font.render(text, 1, color)
#    surface.blit(label, (30,30))


# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#pygame.display.set_caption("Tetris")
#draw_text_middle("Press any key to begin.", 60, (255, 255, 255), screen)

running = True
while running:
    #screen.fill((0,0,0))
    # Look at every event in the queue
    #for event in pygame.event.get():
    #    # Did the user click the window close button? If so, stop the loop
    #    if event.type == QUIT:
    #        running = False
    #
    #    if event.type == pygame.KEYDOWN:
    #        pygame.display.flip()
    #        draw_text_middle("Game started.", 60, (255, 255, 255), screen)

    #pygame.display.flip()
    pygame.display.update()
    clock.tick()

# Done! Time to quit.
pygame.quit()
