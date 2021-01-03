from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ball.new_point()

    def new_point(self):
    #     TODO: reset ball to 0,0, initiate movememtn in a random direction
        print("reset ball and start move")

    def ball_move(self):
        # TODO: make ball move
        print("ball moves")