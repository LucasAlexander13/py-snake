from snake import Snake, screen

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

    except:
        break
