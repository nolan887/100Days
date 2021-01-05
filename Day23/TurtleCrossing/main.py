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
car_count = 0
time_tracker = 0

# Generate game board
player = Player()
scoreboard = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(player.move,"Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.make_car()
    car.drive()

    # Check for squish
    for cars in car.traffic:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Check for finish line
    if player.is_finished():
        player.reset()
        scoreboard.increase_level()
        car.drive_faster()


screen.exitonclick()