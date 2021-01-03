from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Menlo", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.centerline()
        self.update_score()

    def centerline(self):
        self.penup()
        self.pencolor("yellow")
        self.goto(0, 300)
        self.pendown()
        self.setheading(270)
        self.forward(600)
        self.penup()
        self.sidelines()

    def sidelines(self):
        self.color("red")
        self.goto(400, 300)
        self.pendown()
        self.setheading(270)
        self.forward(600)
        self.setheading(180)
        self.forward(800)
        self.setheading(90)
        self.forward(600)
        self.setheading(0)
        self.forward(800)
        self.penup()

    def update_score(self):
        self.clear()
        self.centerline()
        self.goto(0, 250)
        self.pencolor("green")
        self.write(f"{self.l_score}      {self.r_score}", False, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_over(self, winner):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER, {winner} WINS!", align=ALIGNMENT, font=FONT)
