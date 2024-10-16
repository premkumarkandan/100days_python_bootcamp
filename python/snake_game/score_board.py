from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.update_score()
        self.hideturtle()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def score_count(self):
        self.score += 1
        self.clear()
        self.update_score()


