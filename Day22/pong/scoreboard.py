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
        self.pencolor("white")
        self.goto(0, 300)
        self.setheading(270)
        self.forward(600)
        self.goto(0,250)

    def update_score(self):
        self.clear()
        self.centerline()
        self.write(f"{self.l_score}      {self.r_score}", False, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)