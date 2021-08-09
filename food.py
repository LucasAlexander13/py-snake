from turtle import Turtle
from random import choice, randint

color = ['orange', 'dark orange', 'firebrick', 'dark red', 'crimson', 'medium violet red', 'dark magenta', 'medium orchid', 'medium purple', 'indigo', 'slate blue']
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed('fastest')
        self.pick_color()
        self.random_spawn()

    def pick_color(self):
        random_color = choice(color)
        self.color(random_color)
    
    def random_spawn(self):
        x_random = randint(-200, 200)
        y_random = randint(-200, 200)
        self.goto(x_random, y_random)
