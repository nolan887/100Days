from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.drawlines()
        # self.update_score()

    def drawlines(self):
        self.goto(-300,270)
        self.pendown()
        self.setheading(0)
        self.forward(600)
        self.penup()
        self.goto(-300,300)
        self.pendown()
        self.setheading(0)
        self.forward(600)
        self.penup()


        # TODO: FIGURE OUT STARTING LINE / SETUP
        self.goto(-300,-270)
        self.pendown()
        self.setheading(0)
        self.forward(600)
        self.penup()

        # Finish Line
        self.pensize(29)
        self.goto(-300, 285)
        self.setheading(0)
        self.pencolor("palegreen")
        self.pendown()
        self.forward(600)
        self.penup()
        # self.goto(-300,-270)
        # self.pendown()
        # self.pencolor("skyblue")
        # self.forward(600)
