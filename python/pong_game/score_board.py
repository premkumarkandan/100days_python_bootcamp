from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_score_count(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def r_score_count(self):
        self.r_score += 1
        self.clear()
        self.update_score()


