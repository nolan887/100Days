from turtle import Turtle, Screen
import random

# The below line replaces the line above. * imports everything from 'turtle'.
# This is not advisable because it gets very messy when importing more than one module
# from turtle import *

colors = ["cornflowerblue", "lightskyblue", "teal", "springgreen", "olivedrab", "red", "blue", "black", "coral"]

timmy = Turtle()
timmy.shape("turtle")
timmy.color("olivedrab")


# tommy = Turtle()
# tommy.shape("turtle")
# tommy.color("coral")


# # My first attempt -- code works
# for sides in range(3,10):
#     for x in range (0,sides):
#         timmy.forward(100)
#         timmy.right(360/sides)

# alternatively to above, using a function and a single loop -
def draw_shape(num_sides):
    angle = 360 / num_sides
    timmy.color(random.choice(colors))
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


for shape_sides in range(3, 11):
    draw_shape(shape_sides)

# import turtle as t
#
# tim = t.Turtle()
#
# import heroes
# print(heroes.gen())


screen = Screen()
screen.exitonclick()
