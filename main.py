from screen import screen
from snake import Snake
from score import Score
from food import Food
from time import sleep

snake = Snake()
food = Food(snake.segments)
score = Score()
screen.update()
playing = True

screen.listen()
screen.onkeypress(snake.move_up, 'Up')
screen.onkeypress(snake.move_right, 'Right')
screen.onkeypress(snake.move_left, 'Left')
screen.onkeypress(snake.move_down, 'Down')
screen.onkeypress(screen.bye, 'Escape')

while playing:
    try:
        score.message()
        snake.move()
        snake.check_limit()
        
        if snake.head.distance(food) < 15:
            snake.increase_size()
            snake.increase_speed(score.score)
            score.score += 1
            food.spawn(snake.segments)

        screen.update()

        for segment in snake.segments:
            if segment == snake.head:
                continue
            else:
                if snake.head.distance(segment) < 10:
                    score.game_over()
                    playing = False
                    sleep(2)

    except:
        raise Exception
