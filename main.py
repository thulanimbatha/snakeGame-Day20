# Snake game
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python: The Snake Game")
screen.tracer(0)    # show no graphics on screen

starting_positions = [(-20,0), (-40,0)]
snake_segments = []

head = Turtle("square")
head.color("white")
snake_segments.append(head)
head.penup()

for position in starting_positions:
    body = Turtle(shape="square")
    body.penup()
    body.color("white")
    body.goto(position)
    snake_segments.append(body)

# show graphics now
screen.update()

# TODO Turn Snake
while True:
    # move snake
    for seg_num in range(len(snake_segments) - 1, 0, -1):
        new_x = snake_segments[seg_num - 1].xcor()
        new_y = snake_segments[seg_num - 1].ycor()
        snake_segments[seg_num].goto(new_x, new_y)
    snake_segments[0].forward(20)
    # show changes
    screen.update()
    time.sleep(0.1)
screen.exitonclick()
