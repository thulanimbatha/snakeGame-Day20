# Snake game
from snake import Snake
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python: The Snake Game")
screen.tracer(0)    # show no graphics on screen

snake = Snake()
# show graphics now
screen.update()

# TODO Turn Snake
while True:
    snake.move()
    # show changes
    screen.update()
    time.sleep(0.1)
screen.exitonclick()
