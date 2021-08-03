from snake import *
from functions import *
from time import sleep

playing = True

while playing:
    try:
        sleep(0.2)
        for segment in snake:
            segment.forward(20)

        screen.update()
    except:
        break
