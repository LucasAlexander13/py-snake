from turtle import Turtle
from time import sleep

with open('./score.txt', 'r') as file:
    high_score = int(file.read())
    file.close()

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 230)
        self.score = 0
        self.get_highscore()

    def get_highscore(self):
        with open('./score.txt', 'r') as file:
            self.high_score = int(file.read())
            file.close()
    
    def set_highscore(self):
        if self.score > self.high_score:
            with open('score.txt', 'w') as file:
                file.write(f'{self.score}')
                file.close()

    def show_score(self):
        self.clear()
        self.write(
            arg = f'    SCORE: {self.score}\nHIGHSCORE: {self.high_score}', 
            align ='center', 
            font = ('Comic Sans', 14, 'normal')
            )

    def game_over(self):
        self.goto(0, 0)
        self.write(
            arg = 'GAME OVER', 
            align ='center', 
            font = ('Comic Sans', 14, 'normal')
            )
        self.set_highscore()
        sleep(2.5)
