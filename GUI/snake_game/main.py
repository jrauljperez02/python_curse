from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen= Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('SNAKE GAME')
screen.tracer(0)


#Create a snake
snake= Snake()
food= Food()
scoreboard = Scoreboard()

#lets code the methods to be able to move our snake
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')


while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect when happen a collision with Food
    if snake.head.distance(food) < 18:
        scoreboard.increase_score()
        food.refresh()
    

screen.exitonclick()