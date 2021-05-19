from turtle import Turtle, Screen
from puddle import Puddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor(0, 0, 0)
screen.title("Pong")
screen.tracer(0)
ball = Ball()
scoreboard = Scoreboard()
r_puddle = Puddle((370, 0))
l_puddle = Puddle((-370, 0))








screen.listen()
screen.onkey(r_puddle.go_up, "Up")
screen.onkey(r_puddle.go_down, "Down")
screen.onkey(l_puddle.go_up, "w")
screen.onkey(l_puddle.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_puddle) < 50 and ball.xcor() > 350 or ball.distance(l_puddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()





screen.exitonclick()