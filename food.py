from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(8.5, 8.5)
        self.speed('fastest')