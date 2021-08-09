from turtle import Screen
from snake import Snake
from score import Score
from food import Food

screen = Screen()
screen.screensize(500, 500) 
screen.bgcolor('black')
screen.title('PySnake')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.update()

screen.listen()
screen.onkeypress(snake.move_up, 'Up')
screen.onkeypress(snake.move_right, 'Right')
screen.onkeypress(snake.move_left, 'Left')
screen.onkeypress(snake.move_down, 'Down')
screen.onkeypress(screen.bye, 'Escape')

while True:
    try:
        snake.move()
        snake.check_limit()

        if snake.snake_head.distance(food) < 15:
            snake.increase_size()
            food.spawn()

        screen.update()

    except:
        break
