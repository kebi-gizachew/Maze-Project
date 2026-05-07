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
stack = []
current_row = 0
current_col = 0

visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
visited[current_row][current_col] = True
pygame.init()

pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)

glClearColor(0, 0, 0, 1)

running = True
import random

def get_neighbors(row, col):

    neighbors = []

    # UP
    if row > 0 and not visited[row - 1][col]:
        neighbors.append(("UP", row - 1, col))

    # DOWN
    if row < ROWS - 1 and not visited[row + 1][col]:
        neighbors.append(("DOWN", row + 1, col))

    # LEFT
    if col > 0 and not visited[row][col - 1]:
        neighbors.append(("LEFT", row, col - 1))

    # RIGHT
    if col < COLS - 1 and not visited[row][col + 1]:
        neighbors.append(("RIGHT", row, col + 1))

    return neighbors

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