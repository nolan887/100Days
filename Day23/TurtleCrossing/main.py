import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen window setup
screen = Screen()
screen.setup(width=600, height=620)
screen.bgcolor("slategray")
screen.title("Turtle Frogger")
screen.tracer(0)

# variables assigned
game_is_on = True

# Generate game board
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.is_finished():
        player.reset()
        scoreboard.increase_level()

screen.exitonclick()