from screen import screen
from snake import Snake
from score import Score
from food import Food

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
        score.message()
        snake.move()
        snake.check_limit()
        
        if snake.snake_head.distance(food) < 15:
            snake.increase_size()
            snake.increase_speed(score.score)
            score.score += 1
            food.spawn()

        screen.update()

    except:
        break
