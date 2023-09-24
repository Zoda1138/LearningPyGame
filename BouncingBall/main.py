import math
import random

import pygame as py
import time


def mainstream():
    py.init()
    size = 600, 600
    screen = py.display.set_mode(size)
    running = True

    amountX, amountY = random.uniform(0.2, 1.1), random.uniform(0.2, 1.1)
    circX = 300.0
    circY = 300.0
    flagY = True
    flagX = True

    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

        screen.fill((225, 225, 225))

        py.draw.circle(screen, (59, 164, 36), [circX, circY], 70, 0)

        time.sleep(0.0009)

        if circY > 0 and flagY:
            circY -= amountY
        else:
            circY += amountY
        if circY >= 560.0 or circY <= 30.1:
            flagY = not flagY
            amountY = random.uniform(0.2, 0.9)

        if circX > 0 and flagX:
            circX -= amountX
        else:
            circX += amountX
        if circX >= 560.0 or circX <= 30.1:
            flagX = not flagX
            amountX = random.uniform(0.2, 0.9)

        py.display.update()

    py.quit()


if __name__ == '__main__':
    mainstream()