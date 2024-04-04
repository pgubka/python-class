import pygame
 
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
 
game_over = False
 
# snake
snake_block=10
x1 = width/2
y1 = hight/2
x1_change = 0       
y1_change = 0
 
clock = pygame.time.Clock()
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
 
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, blue, [x1, y1, 10, 10])
 
    pygame.display.update()
 
    clock.tick(30)
 
pygame.quit()
quit()
