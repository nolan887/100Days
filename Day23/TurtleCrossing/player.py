from turtle import Turtle

STARTING_POSITION = (0, -290)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 270


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.pencolor("white")
        self.setheading(90)
        self.penup()
        self.reset()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)

    def is_finished(self):
        if (self.ycor() + 10) >= FINISH_LINE_Y:
            return True
        return False