from snake import *

def clear(): screen.bye()

def move_up(): 
    snake_head.setheading(90)

def move_left(): 
    snake_head.setheading(180)

def move_right(): 
    snake_head.setheading(0)

def move_down(): 
    snake_head.setheading(270)

def move_snake():
    screen.listen()
    screen.onkey(move_up, 'w')
    screen.onkey(move_left, 'a')
    screen.onkey(move_right, 'd')
    screen.onkey(move_down, 's')
    screen.onkey(clear, 'c')
    snake_head.forward(20)
