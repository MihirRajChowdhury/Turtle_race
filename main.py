import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
colors = ["violet", "blue", "green", "yellow", "orange", "red"]
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Try to guess which turtle is going to win the race")
y = 150
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(-240, y)
    y -= 58
if user_bet:
    is_race_on = True
winning_turtle = ""
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            is_race_on = False
        num = random.random()*10
        turtle.forward(num)

if winning_turtle == user_bet:
    print(f"Yeah won, The {winning_turtle} is the winner")
else:
    print(f"You lose, The {winning_turtle} is the winner")

screen.exitonclick()
