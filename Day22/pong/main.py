from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

# Variables assigned
game_is_on = True

# Screen window setup
screen = Screen()
screen.setup(width=900, height=640)
screen.bgcolor("black")
screen.title("P O N G")
screen.tracer(0)

# Generate game board
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(r_paddle.pad_up, "Up")
screen.onkey(r_paddle.pad_down, "Down")
screen.onkey(l_paddle.pad_up, "w")
screen.onkey(l_paddle.pad_down, "s")

while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.moving()

    # Ball bounces off of top and bottom walls
    if ball.ycor() >= 285 or ball.ycor() <= -285:
        ball.setheading(ball.heading() * -1)

    # Ball passes by a paddle for a score on either side
    if ball.xcor() >= 380:
        scoreboard.l_point()
        ball.new_point()
    elif ball.xcor() <= -380:
        scoreboard.r_point()
        ball.new_point()

    # Ball bounces off of right paddle
    if ball.xcor() >= 325 and ball.distance(r_paddle) < 50:
        if ball.ycor() > r_paddle.ycor() and ball.heading() < 90:
            ball.mirror()
        elif ball.ycor() > r_paddle.ycor() and ball.heading() > 270:
            ball.reverse()
        elif ball.ycor() < r_paddle.ycor() and ball.heading() < 90:
            ball.reverse()
        elif ball.ycor() < r_paddle.ycor() and ball.heading() > 270:
            ball.mirror()

    # Ball bounces off of left paddle
    if ball.xcor() <= -325 and ball.distance(l_paddle) < 50:
        if ball.ycor() > l_paddle.ycor() and ball.heading() < 180:
            ball.mirror()
        elif ball.ycor() > l_paddle.ycor() and ball.heading() > 180:
            ball.reverse()
        elif ball.ycor() < l_paddle.ycor() and ball.heading() < 180:
            ball.reverse()
        elif ball.ycor() < l_paddle.ycor() and ball.heading() > 180:
            ball.mirror()

    if scoreboard.l_score == 11:
        scoreboard.game_over("LEFT")
        game_is_on = False
    elif scoreboard.r_score == 11:
        scoreboard.game_over("RIGHT")
        game_is_on = False

screen.exitonclick()
