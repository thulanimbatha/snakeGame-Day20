# Snake game
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python: The Snake Game")

# TODO Create snake body
head = Turtle("square")
head.color("white")
head.penup()

body = Turtle("square")
body.color("white")
body.penup()
body.goto(-20,0)

tail = Turtle("square")
tail.color("white")
tail.penup()
tail.goto(-40,0)



screen.exitonclick()