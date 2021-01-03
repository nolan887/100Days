from turtle import Turtle
import random

BALL_START_ANGLES = [15, 30, 45, 135, 150, 165, 195, 210, 225, 315, 330, 345]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("grey")
        self.penup()
        self.new_point()
        self.new_direction = 0

    def new_point(self):
        self.goto(0, 0)
        self.new_direction = random.choice(BALL_START_ANGLES)
        self.setheading(self.new_direction)

    def moving(self):
        self.forward(10)

    def reverse(self):
        self.setheading((self.heading()) + 180)

    def mirror(self):
        self.setheading((self.heading() * -1) + 180)
