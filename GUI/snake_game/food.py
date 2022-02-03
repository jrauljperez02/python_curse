from turtle import *
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.refresh()


    def refresh(self):
        random_x= random.randint(-290,290)
        random_y= random.randint(-290,290)
        self.goto(random_x,random_y)
