from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Brick:
    def __init__(self):
        self.all_bricks = []

    def create_wall(self):
        for row in range(6):
            for col in range(12):
                new_brick = Turtle("square")
                new_brick.penup()
                new_brick.shapesize(stretch_wid=2, stretch_len=3)
                new_brick.color(COLORS[row])

                x = -362 + (col * 65)
                y = 240 - (row * 45)

                new_brick.goto(x, y)
                self.all_bricks.append(new_brick)


