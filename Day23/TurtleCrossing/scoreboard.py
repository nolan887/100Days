from turtle import Turtle

FONT = ("Courier", 18, "normal")
ALIGNMENT = ("center")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.drawlines()
        self.increase_level()
        # self.update_score()

    def drawlines(self):
        # Finish line area
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


        # Starting line area
        self.goto(-300,-270)
        self.pendown()
        self.setheading(0)
        self.forward(600)
        self.penup()
        self.goto(-300,-300)
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
        self.goto(-300, -285)
        self.setheading(0)
        self.pencolor("skyblue")
        self.pendown()
        self.forward(600)
        self.penup()

    def increase_level(self):
        self.score += 1
        self.penup()
        self.clear()
        self.goto(0,285)
        self.pencolor("white")
        self.write("FINISH FINISH FINISH", align = ALIGNMENT, font=FONT)
        self.penup()
        # print level