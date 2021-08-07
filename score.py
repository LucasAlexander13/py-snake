from turtle import Turtle
from random import randint, choice

color = ['orange', 'dark orange', 'firebrick', 'dark red', 'crimson', 'medium violet red', 'dark magenta', 'medium orchid', 'medium purple', 'indigo', 'slate blue']
class Score():
    def __init__(self, snake):
        self.dot = Turtle()
        self.dot.hideturtle()
        self.dot.penup()
        self.set_position(snake)
        self.points = 0

    def set_position(self, snake):
        random_x = randint(-32, 32) * 10
        random_y = randint(-24, 24) * 10
        self.dot.goto(random_x, random_y)
        for segment in snake.segments:
            if self.dot.position == segment.position:
                return self.set_position(snake)
        self.dot.pendown()
        self.dot.dot(20, choice(color))
        self.dot.penup()