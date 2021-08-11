from screen import *
from snake import Snake
from score import Score
from food import Food

while True:
    # Defines screen size, color and edge line
    set_screen(screen)
    draw_edge()
    score = Score()

    # put snake and food on screen
    snake = Snake()
    food = Food(snake.segments)

    screen.update()
    playing = True

    # listen to keypress of the player
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
            
            # check if head is eating food and increase snake size and score
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
                        screen.clearscreen()

        except:
            raise Exception
