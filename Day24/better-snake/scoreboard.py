from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Menlo", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("whitesmoke")
        self.goto(0,280)
        self.score = -1
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
