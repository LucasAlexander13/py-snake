from turtle import Screen
from snake import Snake
from score import Score

screen = Screen()
screen.screensize(640, 480)
screen.bgcolor('black')
screen.title('PySnake')
screen.tracer(0)

snake = Snake()
score = Score(snake)
screen.update()

while True:
    try:
        snake.move()
        snake.check_limit()
        screen.update()

        screen.listen()
        screen.onkeypress(snake.move_up, 'Up')
        screen.onkeypress(snake.move_right, 'Right')
        screen.onkeypress(snake.move_left, 'Left')
        screen.onkeypress(snake.move_down, 'Down')
        screen.onkeypress(screen.bye, 'Escape')

    except:
        break
