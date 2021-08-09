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
            arg = f'Score: {self.score}', 
            align ='center', 
            font = ('Comic Sans', 14, 'normal')
            )
