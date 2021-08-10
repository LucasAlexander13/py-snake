from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 250)
        self.score = 0

    def message(self):
        self.clear()
        self.write(
            arg = f'SCORE: {self.score}', 
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
