# Day 19 Starting file


from turtle import Turtle, Screen

tim= Turtle()

screen = Screen()
screen.listen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.back(10)

def turn_cw():
    tim.right(10)

def turn_ccw():
    tim.left(10)

def shake():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()

screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "d", fun = turn_cw)
screen.onkey(key = "a", fun = turn_ccw)
screen.onkey(key = "c", fun = shake)

screen.exitonclick()