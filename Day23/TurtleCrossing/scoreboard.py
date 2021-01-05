from turtle import Turtle

FONT = ("Courier", 18, "normal")


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
        self.goto(-300, 270)
        self.pendown()
        self.pencolor("black")
        self.setheading(0)
        self.forward(600)
        self.penup()
        self.goto(-300, 300)
        self.pendown()
        self.setheading(0)
        self.forward(600)
        self.penup()

        # Starting line area
        self.goto(-300, -270)
        self.pendown()
        self.setheading(0)
        self.forward(600)
        self.penup()
        self.goto(-300, -300)
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

        # Starting Line
        self.goto(-300, -285)
        self.setheading(0)
        self.pencolor("skyblue")
        self.pendown()
        self.forward(600)
        self.penup()

        # Highway
        self.goto(-300, 0)
        self.pendown()
        self.pensize(540)
        self.pencolor("gray10")
        self.forward(600)
        self.penup()
        self.pensize(1)

        # Highway Lanes
        self.new_y = -240
        for _ in range(17):
            self.pencolor("yellow")
            self.goto(-300, self.new_y)
            while self.xcor() < 300:
                self.pendown()
                self.forward(10)
                self.penup()
                self.forward(5)
            self.new_y += 30

    def increase_level(self):
        self.score += 1
        self.penup()
        self.clear()
        self.drawlines()
        self.goto(-290, 275)
        self.pencolor("black")
        self.pensize(2)
        self.write(f"Level: {self.score}", align="left", font=FONT)
        self.pensize(1)
        self.goto(-175, 275)
        self.pencolor("darkseagreen")
        self.write("FINISH FINISH FINISH FINISH FINISH FINISH FINISH FINISH", align="left", font=FONT)
        self.goto(0, -295)
        self.pencolor("dodgerblue")
        self.write("START START START START START START START START START START", align="center", font=FONT)
        self.penup()

    def game_over(self):
        self.goto(0, 0)
        self.pencolor("red")
        self.write("G A M E    O V E R", align="center", font=FONT)
