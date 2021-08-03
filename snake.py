from turtle import Turtle, Screen

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor('black')
screen.title('PySnake')
screen.tracer(0)

snake = []

for i in range(3):
    segment = Turtle('square')
    segment.penup()
    segment.color('white')
    segment.goto(0 - i * 20, 0)
    snake.append(segment)

snake_head  = snake[0]

screen.update()
