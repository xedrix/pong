from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.player_1_score = 0
        self.player_2_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player_1_score, move=False, align="center", font=("Arial", 70, "normal"))
        self.goto(100, 200)
        self.write(self.player_2_score, move=False, align="center", font=("Arial", 70, "normal"))

    def player_1_scored(self):
        self.player_1_score += 1
        self.update_score()

    def player_2_scored(self):
        self.player_2_score += 1
        self.update_score()
