import pygame
import random
 
pygame.init()
 
#colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0,0,255)

# display
width=800
hight=600
dis = pygame.display.set_mode((width, hight))
pygame.display.set_caption('Snake Game')
 
# flags
game_close = False
game_over=False
game_speed=20
 
# snake
snake_block=10
x1 = width/2
y1 = hight/2
x1_change = 0       
y1_change = 0
snake_length=1
 
#fruit
def new_fruit():
    return random.randint(0,(width-10)/10)*10, random.randint(0,(hight-10)/10)*10
fruitx, fruity =  new_fruit()

clock = pygame.time.Clock()

def show_score():
    font = pygame.font.Font(pygame.font.get_default_font(), 36)
    score_text = font.render('Your score: {}'.format(snake_length-1), True, black)
    dis.blit(score_text, dest=(0,0))

while not game_close:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_close = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x1_change == 0:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT and x1_change == 0:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP and y1_change == 0:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN and y1_change == 0:
                y1_change = snake_block
                x1_change = 0

    dis.fill(white)

    if game_over:
        show_score()
    else:
        x1 += x1_change
        y1 += y1_change

        if x1 >= width or x1 < 0 or y1 >= hight or y1 < 0:
            x1 -= x1_change
            y1 -= y1_change
            game_over = True

        if x1==fruitx and y1==fruity:
            snake_length += 1
            fruitx, fruity = new_fruit()

    pygame.draw.rect(dis, blue, [x1, y1, snake_block, snake_block])
    pygame.draw.rect(dis, red, [fruitx, fruity, snake_block, snake_block])
 
 
    pygame.display.update()
    clock.tick(game_speed)
 
pygame.quit()
quit()
