import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

WIDTH = 800
HEIGHT = 800
ROWS = 20
COLS = 20
CELL_SIZE = 2 / ROWS
northWall = [[1 for _ in range(COLS)] for _ in range(ROWS)]
eastWall = [[1 for _ in range(COLS)] for _ in range(ROWS)]

visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
pygame.init()

pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)

glClearColor(0, 0, 0, 1)

running = True
def draw_maze():

    for row in range(ROWS):

        for col in range(COLS):

            x = -1 + col * CELL_SIZE
            y = 1 - row * CELL_SIZE

            # NORTH WALL
            if northWall[row][col]:

                draw_line(
                    x,
                    y,
                    x + CELL_SIZE,
                    y
                )

            # EAST WALL
            if eastWall[row][col]:

                draw_line(
                    x + CELL_SIZE,
                    y,
                    x + CELL_SIZE,
                    y - CELL_SIZE
                )
def draw_grid():

    for row in range(ROWS + 1):

        y = 1 - row * CELL_SIZE

        draw_line(-1, y, 1, y)

    for col in range(COLS + 1):

        x = -1 + col * CELL_SIZE

        draw_line(x, -1, x, 1)
def draw_line(x1, y1, x2, y2):

    glBegin(GL_LINES)

    glColor3f(1, 1, 1)

    glVertex2f(x1, y1)
    glVertex2f(x2, y2)

    glEnd()
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT)
    draw_grid()
    pygame.display.flip()
# LEFT BORDER
draw_line(-1, -1, -1, 1)
# BOTTOM BORDER
draw_line(-1, -1, 1, -1)

pygame.quit()