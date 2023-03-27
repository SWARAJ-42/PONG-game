# This is a tutorial for making a classic game named pong
import turtle

# screen
wn = turtle.Screen()
wn.title("PONG")
wn.bgcolor("black")
wn.setup(height=600, width=800)
wn.tracer(0)  # the main take away is that it speeds up the game

# Paddle A
shape = ((-5, 55), (5, 55), (10, 50), (10, -50),
         (5, -55), (-5, -55), (-10, -50), (-10, 50))
turtle.register_shape("paddle", shape)

paddle_a = turtle.Turtle()  # this is turtle
paddle_a.speed(0)  # sets the speed to maximum level
paddle_a.shape("paddle")  # this is the shape of the turtle
paddle_a.tilt(90)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, -25)


# Paddle B
paddle_b = turtle.Turtle()  # this is turtle initiation
paddle_b.speed(0)  # sets the speed to maximum level
paddle_b.shape("paddle")  # this is the shape of the turtle
paddle_b.tilt(90)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, -25)

# Ball
ball = turtle.Turtle()
ball.speed(0)
shape1 = ((-5, 10), (5, 10), (10, 5), (10, -5),
          (5, -10), (-5, -10), (-10, -5), (-10, 5))
turtle.register_shape("hexagon", shape1)
ball.shape("hexagon")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, -25)
ball.dx = .2
ball.dy = .2

# score
score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,265)
pen.write("Player A : {}  |   Player B : {}".format(score_a,score_b), align= "center" ,  font=("Courier",15,"normal"))
pen.goto(0,250)
pen.pendown()
pen.forward(400)
pen.backward(800)
pen.penup()
pen.goto(0,265)

def boundary():
    pen.goto(0,250)
    pen.pendown()
    pen.forward(400)
    pen.backward(800)
    pen.penup()
    pen.goto(0,265)

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")  # IMPORTANT!!!! No brackets
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game Loop

while True:
    wn.update()  # Everytime the loop runs it updates the screen
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    ball.tilt(0.1)

    if ball.ycor() > 240:
        ball.sety(240)
        ball.dy *= -1  # only method for reversing the direction
        ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # only method for reversing the direction
        ball.sety(ball.ycor() + ball.dy)

    if ball.xcor() > 370:
        ball.setx(0)
        ball.sety(-25)
        ball.dx *= -1
        ball.setx(ball.xcor() + ball.dx)
        score_a +=1 
        pen.clear()
        pen.write("Player A : {}  |   Player B : {}".format(score_a,score_b), align= "center" ,  font=("Courier",15,"normal"))
        boundary()

    if ball.xcor() < -370:
        ball.setx(0)
        ball.sety(-25)
        ball.dx *= -1
        ball.setx(ball.xcor() + ball.dx)
        score_b +=1 
        pen.clear()
        pen.write("Player A : {}  |   Player B : {}".format(score_a,score_b), align= "center" ,  font=("Courier",15,"normal"))
        boundary()

    # collision
    if ball.xcor() > 340 and ball.ycor() > (paddle_b.ycor() - 50) and ball.ycor() < (paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.ycor() > (paddle_a.ycor() - 50) and ball.ycor() < (paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
    
    if paddle_a.ycor() > 195:
        paddle_a.sety(195)
    if paddle_a.ycor() < -235:
        paddle_a.sety(-235)
    
    if paddle_b.ycor() > 195:
        paddle_b.sety(195)
    if paddle_b.ycor() < -235:
        paddle_b.sety(-235)
    