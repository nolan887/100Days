from turtle import Turtle
import time
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2.5
LANES_Y = [-255, -225, -195, -165, -135, -105, -75, -45, -15, 15, 45, 75, 105, 135, 165, 195, 225, 255]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.traffic = []
        self.speed = STARTING_MOVE_DISTANCE
        self.make_car()

    def make_car(self):
        dice_roll = random.randint(1,5)
        if dice_roll == 3:
            new_car = Turtle("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_lane = random.choice(LANES_Y)
            new_car.color(random.choice(COLORS))
            new_car.pencolor("white")
            new_car.goto(300, new_lane)
            self.traffic.append(new_car)
        else:
            pass

    def drive(self):
        for car in self.traffic:
            car.forward(self.speed)

    def drive_faster(self):
        self.speed += MOVE_INCREMENT

