from turtle import Turtle, Screen
from snake import Snake


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My snake game')

#Create a snake
snake = Snake()



#lets code the methods to be able to move our snake
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')



screen.mainloop()