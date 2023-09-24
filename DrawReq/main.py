import pygame as py
from pygame.locals import *


def mein():
    py.init()
    running = True
    screen = py.display.set_mode((600, 600))

    start = (0, 0)
    size = (0, 0)
    drawing = False
    amountOfShapes = 0
    shapesPos = []

    while running:
        for event in py.event.get():
            if event.type == QUIT:
                running = False

            elif event.type == py.KEYDOWN and event.key == py.K_BACKSPACE:  # Remove (FIFO) req
                shapesPos.pop()
                amountOfShapes -= 1

            elif event.type == MOUSEBUTTONDOWN:  # Beginning to hold
                start = event.pos
                size = 0, 0
                drawing = True

            elif event.type == MOUSEBUTTONUP:  # Not holding anymore
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
                drawing = False
                amountOfShapes += 1
                shapesPos.append([start, size])

            elif event.type == MOUSEMOTION and drawing:  # Still holding
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
                py.draw.rect(screen, (0, 111, 0), (start, size), 2)


            py.display.update()

        screen.fill((255, 255, 255))

        for i in range(amountOfShapes):  # draw all the drawn shapes
            if i + 1 == amountOfShapes:
                py.draw.rect(screen, (0, 0, 0), shapesPos[i], 2)  # New
            else:
                py.draw.rect(screen, (0, 100, 0), shapesPos[i], 2)  # Old

        py.display.update()

    py.quit()


if __name__ == '__main__':
    mein()