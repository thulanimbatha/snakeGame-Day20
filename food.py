'''FOOD CLASS'''
from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        # inherit from super class
        super().__init__()
        # now create the snake food
        self.shape("circle")
        self.penup()
        # auto size is 20 x 20, so we want 10 x 10
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        # now set its coordinates -> multiples of 20(from snake)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

