from turtle import Turtle, Screen
import random

is_race_on = False
turtle_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
all_turtles = []

# Screen setup
screen = Screen()
screen.bgcolor("grey")
screen.setup(width = 900, height = 400)

# User input through text prompt to place bet
user_bet = screen.textinput(title = "BET", prompt = "Which turtle color do you think will win? \n(red, orange, yellow, "
                                                    "green, blue, indigo, violet):")

# do maths based on screen size to set the starting locations (turtle size is 40 x 40)
x_start = ((screen.window_width() / 2) * -1) + 15
y_spacing = (screen.window_height() / 14)
y_start = ((y_spacing * -1) * 3)
x_end = (screen.window_width() / 2) - 50

# create start and finish lines
lines = Turtle()
lines.penup()
lines.goto(x = (x_start + 20), y = (screen.window_height() / 2))
lines.right(90)
lines.pendown()
lines.forward(screen.window_height() + 20)
lines.penup()
lines.goto(x = (x_end + 15), y = screen.window_height() / 2)
lines.pendown()
lines.forward(screen.window_height() + 20)

# generate turtles
for turtle_index in range (0,7):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.penup()
    new_turtle.fillcolor(turtle_colors[turtle_index])
    new_turtle.goto(x = x_start, y = y_start)
    y_start += y_spacing
    all_turtles.append(new_turtle)



# Take the bet
if user_bet:
    is_race_on = True

# Do the race
while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= x_end:
            is_race_on = False
            winning_color = turtle.fillcolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")


screen.exitonclick()