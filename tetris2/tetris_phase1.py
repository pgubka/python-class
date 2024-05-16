import pygame
import sys

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 25

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
COLORS = [RED, BLUE, GREEN]

SHAPES = [
    [
        ['.....',
         '.....',
         '.....',
         'OOOO.',
         '.....'],
        ['.....',
         '..O..',
         '..O..',
         '..O..',
         '..O..']
    ],
]

class Tetromino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(COLORS) # You can choose different colors for each shape
        self.rotation = 0

class Tetris:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [['.' for _ in range(width)] for _ in range(height)]
        #self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0  # Add score attribute

    def print_grid(self):
        for row in self.grid:
            rowstr = ""
            for cell in row:
                rowstr += cell
            print(rowstr)


def main():

    pygame.init()
    # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetris')
    # Create a clock object
    clock = pygame.time.Clock()
    # Create a Tetris object
    game = Tetris(SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE)
    fall_time = 0
    fall_speed = 50
    while True:

        # vypln pozadie
        screen.fill(BLACK)

        # 
        for event in pygame.event.get():
            # Check for the QUIT event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game.print_grid()

        # Get the number of milliseconds since the last frame
        delta_time = clock.get_rawtime() 
        # Add the delta time to the fall time
        fall_time += delta_time 
        if fall_time >= fall_speed:
            # Move the piece down
            #game.update()
            # Reset the fall time
            fall_time = 0

        # Update the display
        pygame.display.flip()
        # Set the framerate
        clock.tick(60)

if __name__ == "__main__":
    main()
