import random
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=500, height=400)
screen_height = screen.window_height()
screen_width = screen.window_width()

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]

turtles = []
for turtle_color in turtle_colors:
    turtle = Turtle(shape="turtle", visible=False)
    turtle.speed("fastest")
    turtle.color(turtle_color)
    turtles.append(turtle)

number_turtles = len(turtles)

turtle_distance = (screen_height - (screen_height * (0.30))) / number_turtles
x_position = -(screen_width / 2) + screen_width * (0.05)
y_position = -(screen_height / 2) + screen_height * (0.2)

for turtle in turtles:
    turtle.up()
    turtle.goto(x=x_position, y=y_position)
    turtle.showturtle()
    y_position += turtle_distance


is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > screen_width / 2:
            is_race_on = False
            winner_color = turtle.color()[1]

            if winner_color == user_bet.lower():
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winner_color} turtle is the winner!")


screen.bye()
