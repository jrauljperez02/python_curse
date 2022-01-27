from turtle import Turtle,Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Wich turtle will win the race?: ")
colors = ['red','orange','yellow','green','blue','purple']
y_position = [-70,-40,-10,20,50,80]


all_turtles = []

for index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
else:
    print('Make a bet')

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} is the winner.")
            else:
                print('You have lost')
        turtle.forward(random.randint(1,10))
screen.mainloop()