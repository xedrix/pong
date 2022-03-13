from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.width = 20
        self.height = 100
        if player == 1:
            self.setposition(-350, 0)
        else:
            self.setposition(350, 0)
        self.setheading(90)
        self.color("white")
        self.shape("square")
        self.shapesize(1, 5)
        self.penup()

    def move_up(self):
        if not self.ycor() > 240:
            self.forward(20)

    def move_down(self):
        if not self.ycor() < -220:
            self.back(20)
