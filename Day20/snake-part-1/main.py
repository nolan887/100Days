from turtle import Turtle, Screen

# Screen Window Setup
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_segmenet = Turtle("square")
    new_segmenet.color("yellow")
    new_segmenet.goto(position)








screen.exitonclick()