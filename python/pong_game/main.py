import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score_board import Scorecard

wall_1_y_limit = 300
wall_2_y_limit = -300
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)
screen.title("Pong")

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))

ball = Ball()
scoreboard = Scorecard()

screen.listen()
screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")
screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")


game_is_on = True
place_y = 325
for _ in range(15):
    place_y -= 40
    place = (0, place_y)
    t = Turtle()
    t.shape("square")
    t.shapesize(stretch_wid=1, stretch_len=0.5)
    t.color("white")
    t.pu()
    t.goto(place)
while game_is_on:
    time.sleep(ball.ball_motion_speed)
    screen.update()
    ball.ball_motion()

    # detect collision with wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.ball_bounce_y()

    # detect collision with paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.ball_bounce_x()
        ball.ball_color_change()

    # detect when right paddle misses
    if ball.xcor() > 380:
        scoreboard.l_score_count()
        ball.ball_out_of_bounds()
    if ball.xcor() < -380:
        scoreboard.r_score_count()
        ball.ball_out_of_bounds()

screen.exitonclick()
