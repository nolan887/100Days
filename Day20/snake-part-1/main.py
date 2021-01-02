from turtle import Turtle, Screen
import time

# Screen Window Setup
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# Initialize variables
game_on = True
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    new_segmenet = Turtle("square")
    new_segmenet.color("yellow")
    new_segmenet.penup()
    new_segmenet.goto(position)
    segments.append(new_segmenet)


while game_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)







screen.exitonclick()