# Problem Statement
# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

import pygame
import time

pygame.init()

CANVA_WIDTH = 400
CANVA_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

BLUE = (0,0,225)
WHITE = (255,255,255)
PINK = (225,182,193)

screen = pygame.display.set_mode(CANVA_WIDTH , CANVA_HEIGHT)