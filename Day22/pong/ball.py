from turtle import Turtle
import random

BALL_START_ANGLES = [15, 30, 45, 135, 150, 165, 195, 210, 225, 315, 330, 345]
GO_RIGHT_ANGLES = [15, 30, 45, 315, 330, 345]
GO_LEFT_ANGLES = [135, 150, 165, 195, 210, 225]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.move_angle = BALL_START_ANGLES
        self.shape("circle")
        self.color("grey")
        self.penup()
        self.new_point("RANDOM")
        self.new_direction = 0


    def new_point(self, dir):
        self.goto(0, 0)
        if dir == "left":
            self.move_angle = GO_LEFT_ANGLES
        elif dir == "right":
            self.move_angle = GO_RIGHT_ANGLES
        self.new_direction = random.choice(self.move_angle)
        self.setheading(self.new_direction)
        self.ballspeed = 10

    def moving(self):
        self.forward(self.ballspeed)

    def reverse(self):
        self.setheading((self.heading()) + 180)
        self.ballspeed += 1

    def mirror(self):
        self.setheading((self.heading() * -1) + 180)
        self.ballspeed += 1
