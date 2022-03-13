import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT, startx=0, starty=0)
screen.title("Pong")
screen.tracer(0)

player_1 = Paddle(1)
player_2 = Paddle(2)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_1.move_up, "w")
screen.onkey(player_1.move_down, "s")
screen.onkey(player_2.move_up, "Up")
screen.onkey(player_2.move_down, "Down")

game_over = False
while not game_over:
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce(wall_or_paddle="wall")

    if ball.distance(player_1) < 50 and ball.xcor() < -330 or ball.xcor() > 330 and ball.distance(player_2) < 50:
        ball.bounce(wall_or_paddle="paddle")

    if ball.xcor() > 380:
        ball.reset_ball(ball.xcor())  # re-centers ball and sends it opposite direction of who got scored on
        scoreboard.player_2_scored()

    if ball.xcor() < -380:
        ball.reset_ball(ball.xcor())
        scoreboard.player_1_scored()
    time.sleep(ball.movement_speed)

screen.exitonclick()
