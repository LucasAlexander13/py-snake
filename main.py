from snake import *
from functions import *
from time import sleep

playing = True

while playing:
    try:
        screen.update()
        sleep(0.2)
        
        for segment in range(len(snake) - 1, 0, -1):
            new_x = snake[segment - 1].xcor()
            new_y = snake[segment - 1].ycor()
            snake[segment].goto(new_x, new_y)
        
        move_snake()

    except:
        break
