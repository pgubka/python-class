import turtle

# modified https://gist.github.com/saadat99/67a5b4796bef3763e422d09f92ca7b26

wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(5, 1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(5, 1)

# Ball
ball = turtle.Turtle()  
ball.speed(0)  
ball.shape("circle")  
ball.color("white")  
ball.penup()  
# Ball starts from the centre of the screen  
ball.goto(0, 0)  
# Setting dx and dy that decide the speed of the ball  
ball.dx = 0.1
ball.dy = 0.1 

# Pen
#pen = turtle.Turtle()
#pen.speed(0)
#pen.color('white')
#pen.penup()
#pen.goto(0, 260)
#pen.hideturtle()

# Score
#score_a = 0
#score_b = 0

#def reprint_score():
#    pen.clear()
#    pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'bold'))
#reprint_score()

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')

#wn.mainloop()  # This will make sure the program continues to run 
# Main game loop

while True:
    wn.update()

    # Moving Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
