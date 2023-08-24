from random import choice
from turtle import *

from colors import rgb_colors


def choose_color():
    new_color = choice(rgb_colors)
    return new_color


screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.speed("fastest")
timmy.up()
timmy.hideturtle()
timmy.goto(-250, -200)

dots_per_line = 10
lines = 10

for _ in range(lines):
    for _ in range(dots_per_line):
        color = choose_color()
        timmy.forward(50)
        timmy.dot(20, color)
    timmy.goto(-250, timmy.ycor() + 50)

exitonclick()
