from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 270


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.pencolor("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)