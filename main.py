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
head.penup()

for position in starting_positions:
    body = Turtle(shape="square")
    body.penup()
    body.color("white")
    body.goto(position)
    snake_segments.append(body)

# show graphics now
screen.update()

# TODO Move Snake
while True:
    # move snake
    head.forward(20)
    for segment in snake_segments:
        segment.forward(20)
    # show changes
    screen.update()
    time.sleep(0.2)
screen.exitonclick()
