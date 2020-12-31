# Code below was used to extract colors from image.jpg. The extracted_library is copy/pasted from the result.
import colorgram

rgb_colors = []
colors_extracted = colorgram.extract("image.jpg", 15)

for color in colors_extracted:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

extracted_library = rgb_colors

from turtle import Turtle, Screen
import random

paint = Turtle()
paint.pensize(5)
paint.speed(0)
paint.hideturtle()

dot_size = 15
dot_spacing = 25
dot_move = dot_size + dot_spacing

screen = Screen()
screen.colormode(255)
screen.bgcolor(random.choice(extracted_library))

def go_to_start(dia):
    paint.penup()
    paint.setheading(225)
    paint.forward((dia * 5))
    paint.setheading(0)
    paint.pendown()
    return paint.pos()[0]


def paint_row():
    for _ in range(10):
        paint.pencolor(random.choice(extracted_library))
        paint.dot(dot_size)
        paint.penup()
        paint.forward(dot_move)


x_pos = go_to_start(dot_move)

for _ in range(10):
    paint_row()
    paint.setx(x_pos)
    paint.sety(paint.ycor() + dot_move)

screen.exitonclick()
