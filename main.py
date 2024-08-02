import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong Game")
screen.tracer(0)


screen.listen()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = ScoreBoard()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.Move()
    if ball.ycor() > 278 or ball.ycor() < -278 :
        ball.bounce_y()
    #Ditect collision with paddle
    if ball.distance(r_paddle)< 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Ditect miss r_paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Ditect miss l_paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()