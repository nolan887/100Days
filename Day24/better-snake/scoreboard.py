from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Menlo", 14, "normal")
HIGH_SCORE_LOG = "high_score.txt"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("whitesmoke")
        self.goto(0,280)
        self.score = -1
        with open(HIGH_SCORE_LOG) as data:
            self.high_score = int(data.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE: {self.score} | HIGH SCORE: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(HIGH_SCORE_LOG, mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = -1
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("red")
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
