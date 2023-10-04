from turtle import Screen
import time
from scoreboard import Scoreboard
from food import Food
from snake import Snake

scoreboard = Scoreboard()
food = Food()
snake = Snake()
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -295 or snake.head.ycor() > 290 or snake.head.ycor() < -295:
        scoreboard.reset()
        snake.reset()

    # Detect if hitting itself
    for i in snake.segments[1:]:
        if snake.head.distance(i) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()


