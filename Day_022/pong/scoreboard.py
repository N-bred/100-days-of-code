from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.set_scores()

    def write_score(self, score):
        self.write(score, align=ALIGNMENT, font=FONT)

    def set_scores(self):
        self.clear()
        self.goto(-100, 200)
        self.write_score(self.l_score)
        self.goto(100, 200)
        self.write_score(self.r_score)

    def l_point(self):
        self.set_scores()
        self.l_score += 1

    def r_point(self):
        self.set_scores()
        self.r_score += 1
