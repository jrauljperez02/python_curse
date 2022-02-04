from turtle import Screen
from paddles import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong GAME')



r_paddle = Paddle((360,0))
l_paddle = Paddle((-360,0))


#lets define what is going to do both paddles
screen.listen()
#right player
screen.onkey(r_paddle.up,'Up')
screen.onkey(r_paddle.down,'Down')

#left player
screen.onkey(l_paddle.up,'w')
screen.onkey(l_paddle.down,'s')


#lets create our scoreboard object
scoreboard = Scoreboard()
scoreboard.update_scoreboard()
for _ in range(5):
    scoreboard.increase_r_score()

screen.mainloop()