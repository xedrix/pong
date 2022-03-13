from turtle import Turtle
import random

WIDTH = 20
HEIGHT = 20
X_POS = 0
Y_POS = 0


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(1, 1)
        self.penup()
        self.setposition(X_POS, Y_POS)
        self.setheading(random.randint(0, 359))
        self.speed("fastest")
        self.pace = 10
        self.movement_speed = 0.1

    def move(self):
        self.forward(self.pace)

    def bounce(self, wall_or_paddle):
        if wall_or_paddle == "paddle":
            self.setheading(180 - self.heading())
            self.forward(self.pace)
            self.movement_speed *= 0.9
        elif wall_or_paddle == "wall":
            self.setheading(-self.heading())
            self.forward(self.pace)

    def reset_ball(self, xcor):
        self.setposition(X_POS, Y_POS)
        if xcor > 380:
            h1 = random.randint(100, 260)
            self.setheading(h1)
        else:
            h1 = random.randint(280, 359)
            h2 = random.randint(0, 80)
            headings = [h1, h2]
            self.setheading(random.choice(headings))
        self.movement_speed = 0.1
        self.forward(self.pace)
