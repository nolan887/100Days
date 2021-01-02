from turtle import Screen
from snake import Snake
from food import Food
import time

# Screen Window Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()

game_on = True

# Player controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#     Detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()


screen.exitonclick()
