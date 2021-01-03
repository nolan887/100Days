from turtle import Turtle

STARTING_PLAYER_RIGHT = [(380,0)]
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, coords):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(coords)

    def pad_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)

    def pad_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)