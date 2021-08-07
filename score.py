from turtle import Turtle

color = ['orange', 'dark orange', 'firebrick', 'dark red', 'crimson', 'medium violet red', 'dark magenta', 'medium orchid', 'medium purple', 'indigo', 'slate blue']
class Score():
    def __init__(self):
        self.dot = Turtle()
        self.dot.hideturtle()
        self.dot.penup()
        self.points = 0