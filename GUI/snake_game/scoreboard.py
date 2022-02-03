from turtle import Turtle

class Scoreboard(Turtle):
    #INITIAL_POSITION = (0,265)

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto((0,265))
        self.color('white')
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f'Score {self.score}',align='center',font=('Arial',24,'normal'))

    
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()


    def GameOver(self):
        self.goto((0,0))
        self.write(f'Game Over {self.score}',align='center',font=('Arial',24,'normal'))





