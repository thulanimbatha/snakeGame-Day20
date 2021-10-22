# Snake game
from scoreboard import Scoreboard
from snake import Snake
from food import Food
from turtle import Screen
import time


game_over = False

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python: The Snake Game")
screen.tracer(0)    # show no graphics on screen

snake = Snake()
food = Food()   # initialise food
scoreboard = Scoreboard()

# controlling the snake movements
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# TODO Turn Snake
while not game_over:
    # show changes
    screen.update()
    time.sleep(0.1)
    snake.move()

    #TODO detect collision with food
    if snake.head.distance(food) < 15:
        # set new food coordinates
        food.refresh()
        scoreboard.increase_score()

screen.exitonclick()
