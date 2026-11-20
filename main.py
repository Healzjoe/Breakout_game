import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)


paddle = Paddle((0, -250))
ball = Ball()
scoreboard = Scoreboard()
bricks = Brick()
bricks.create_wall()
screen.update()


screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.03)
    screen.update()
    ball.move()

    # side walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # top wall
    if ball.ycor() > 280:
        ball.bounce_y()

    # paddle
    if ball.distance(paddle) < 50 and ball.y_move < 0:
        ball.bounce_y()

    # ball fell past the paddle
    if ball.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False


    # paddle
    if ball.distance(paddle) < 50 and ball.y_move < 0:
        ball.bounce_y()

    # bricks
    for brick in bricks.all_bricks[:]:
        if ball.distance(brick) < 30:
            brick.hideturtle()
            bricks.all_bricks.remove(brick)
            ball.bounce_y()
            scoreboard.increase_score()
            break

    # win
    if not bricks.all_bricks:
        game_is_on = False







screen.exitonclick()