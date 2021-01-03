from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

# Variables assigned
game_is_on = True

# Screen window setup
screen = Screen()
screen.setup(width=840, height=640)
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
screen.onkey(l_paddle.pad_up,"w")
screen.onkey(l_paddle.pad_down,"s")

screen.onkey(scoreboard.l_point,"q")
screen.onkey(scoreboard.r_point,"e")


while game_is_on:
    screen.update()


screen.exitonclick()
