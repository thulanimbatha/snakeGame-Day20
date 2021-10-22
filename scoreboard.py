'''SCOREBOARD CLASS'''
from turtle import Turtle
ALIGNMENT = "Center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        # display the text
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        # increment, clear the text, the write text with new score
        self.score += 1
        self.clear()
        self.update_scoreboard()