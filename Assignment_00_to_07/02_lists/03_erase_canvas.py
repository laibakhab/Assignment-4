# # Problem Statement
# # Implement an 'eraser' on a canvas.

# # The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

# import pygame
# import time

# pygame.init()

# CANVA_WIDTH = 400
# CANVA_HEIGHT = 400
# CELL_SIZE = 40
# ERASER_SIZE = 20

# BLUE = (0,0,225)
# WHITE = (255,255,255)
# PINK = (225,182,193)

# screen = pygame.display.set_mode(CANVA_WIDTH , CANVA_HEIGHT)
# pygame.display.set_caption("Enter effect in pygame")

# grid =[]
# for row in range(0,CANVA_HEIGHT,CELL_SIZE):
#     for col in range(0,CANVA_WIDTH,CELL_SIZE):
#         rect = pygame.Rect(col,row,CELL_SIZE,CELL_SIZE)
#         grid.append(rect)

# eraser = pygame.Rect(200,200,ERASER_SIZE)

# running = True
# while running:
#     screen.fill(WHITE)

#     for rect in grid:
#         pygame.draw.rect(screen,BLUE, rect)

#     mouse_x , mouse_y = pygame.mouse.get_pos()    
#     eraser.topleft = (mouse_x ,mouse_y)

#     new_grid = []
#     for rect in grid:
#         if not eraser.colliderect(rect):
#             new_grid.append(rect)
#     grid = new_grid

#     pygame.draw.rect(screen, PINK , eraser)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     pygame.display.flip()
#     time.sleep(0.05)

# pygame.quit()                    

import pygame
import time

pygame.init()

CANVA_WIDTH = 400
CANVA_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

BLUE = (0, 0, 225)
WHITE = (255, 255, 255)
PINK = (225, 182, 193)

screen = pygame.display.set_mode((CANVA_WIDTH, CANVA_HEIGHT))
pygame.display.set_caption("Eraser Effect in Pygame")

# Grid with color for each cell
grid = []
for row in range(0, CANVA_HEIGHT, CELL_SIZE):
    for col in range(0, CANVA_WIDTH, CELL_SIZE):
        rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
        grid.append((rect, BLUE))  # Each cell has a rect and color

eraser = pygame.Rect(200, 200, ERASER_SIZE, ERASER_SIZE)

running = True
while running:
    screen.fill(WHITE)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser.topleft = (mouse_x, mouse_y)

    new_grid = []
    for rect, color in grid:
        if eraser.colliderect(rect):
            color = WHITE
        pygame.draw.rect(screen, color, rect)
        new_grid.append((rect, color))
    grid = new_grid

    pygame.draw.rect(screen, PINK, eraser)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    time.sleep(0.05)

pygame.quit()
