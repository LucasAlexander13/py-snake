from turtle import Turtle
from time import sleep

SPEED = 0.25
LENGTH = 5


class Snake():
    def __init__(self):
        self.segments = []
        self.speed = SPEED
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        sleep(self.speed)
        for i in range(LENGTH):
            segment = Turtle('square')
            segment.penup()
            segment.color('white')
            segment.goto(0 - i * 20, 0)
            self.segments.append(segment)
    
    # Updates snake segments position following the snake's head
    def move(self):
        sleep(self.speed)
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.snake_head.forward(20)
    
    # Sets a limit for snake movement
    def check_limit(self):
        x_axis = self.snake_head.xcor()
        y_axis = self.snake_head.ycor()

        if x_axis > 330:
            self.snake_head.goto(-330, y_axis)
        elif x_axis < -340:
            self.snake_head.goto(320, y_axis)
        elif y_axis > 285:
            self.snake_head.goto(x_axis, -270)
        elif y_axis < -280:
            self.snake_head.goto(x_axis, 280)
    

    # Methods used to update the snake's direction when pressing a key
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
    
    def increase_size(self):
        last_xcor = self.segments[-1].xcor()
        last_ycor = self.segments[-1].ycor()
        segment = Turtle('square')
        segment.penup()
        segment.color('white')
        segment.goto(last_xcor, last_ycor)
        self.segments.append(segment)

