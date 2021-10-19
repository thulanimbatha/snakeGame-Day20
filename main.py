# Snake game
from snake import Snake
from turtle import Screen, Turtle
import time

game_over = False

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python: The Snake Game")
screen.tracer(0)    # show no graphics on screen

snake = Snake()

# controlling the snake movements
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# TODO Turn Snake
while not game_over:
    snake.move()
    # show changes
    screen.update()
    time.sleep(0.1)
screen.exitonclick()
