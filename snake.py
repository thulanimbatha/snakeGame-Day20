from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# snake class
class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    '''CREATE SNAKE BODY'''
    def create_snake(self):

        for position in STARTING_POSITIONS:
            segment = Turtle(shape="square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.snake_segments.append(segment)

    '''MOVE SNAKE'''
    def move(self):
        # move last segment first
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            # get coordinates(x,y) of segment before the current segment
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            # move current segment to new coordinates (x,y)
            self.snake_segments[seg_num].goto(new_x, new_y)
        # finally, move the head
        self.head.forward(MOVING_DISTANCE)

    '''CONTROL THE SNAKE'''
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)