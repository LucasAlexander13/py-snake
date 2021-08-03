from turtle import Turtle, Screen
from time import sleep

VELOCITY = 0.2

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor('black')
screen.title('PySnake')
screen.tracer(0)

class Snake():
    def __init__(self):
        self.segments = []
        self.speed = 0.2
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        sleep(self.speed)
        for i in range(3):
            segment = Turtle('square')
            segment.penup()
            segment.color('white')
            segment.goto(0 - i * 20, 0)
            self.segments.append(segment)
    
    def move(self):
        sleep(self.speed)
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.snake_head.forward(20)
    
    def move_up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)
    
    def move_right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)
    
    def move_left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)
    
    def move_down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)
