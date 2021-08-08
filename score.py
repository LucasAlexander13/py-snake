from turtle import Turtle
from random import randint, choice

color = ['orange', 'dark orange', 'firebrick', 'dark red', 'crimson', 'medium violet red', 'dark magenta', 'medium orchid', 'medium purple', 'indigo', 'slate blue']
class Score():
    def __init__(self, snake):
        self.food = Turtle()
        self.food.hideturtle()
        self.food.penup()
        self.spawn_food(snake)
        self.points = 0

    def spawn_food(self, snake):
        random_x = randint(-32, 32) * 10
        random_y = randint(-24, 24) * 10
        self.food.goto(random_x, random_y)
        self.get_position(snake)

    def get_position(self, snake):
        for segment in snake.segments:
            if self.food.position == segment.position:
                return self.get_position(snake)
        self.food.pendown()
        self.food.dot(10, choice(color))
        self.food.penup()