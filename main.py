from turtle import Screen
from snake import Snake

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor('black')
screen.title('PySnake')
screen.tracer(0)

snake = Snake()
screen.update()

while True:
    try:
        snake.move()
        screen.update()

        screen.listen()
        screen.onkeypress(snake.move_up, 'Up')
        screen.onkeypress(snake.move_right, 'Right')
        screen.onkeypress(snake.move_left, 'Left')
        screen.onkeypress(snake.move_down, 'Down')
        screen.onkeypress(screen.bye, 'Escape')

    except:
        break
