from turtle import Turtle
STARTING_POSITIONS = [(-20,0), (-40,0)]
MOVING_DISTANCE = 20

# snake class
class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()

    # create snake body
    def create_snake(self):
        head = Turtle("square")
        head.color("white")
        self.snake_segments.append(head)
        head.penup()

        for position in STARTING_POSITIONS:
            body = Turtle(shape="square")
            body.penup()
            body.color("white")
            body.goto(position)
            self.snake_segments.append(body)

    # move snake
    def move(self):

        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVING_DISTANCE)