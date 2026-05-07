import random
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
def draw_mouse(row, col):

    x = -1 + col * CELL_SIZE + CELL_SIZE / 2
    y = 1 - row * CELL_SIZE - CELL_SIZE / 2

    glPointSize(10)

    glBegin(GL_POINTS)

    glColor3f(1, 0, 0)

    glVertex2f(x, y)

    glEnd()
def remove_wall(direction, row, col):

    global northWall
    global eastWall

    if direction == "UP":
        northWall[row][col] = 0

    elif direction == "DOWN":
        northWall[row + 1][col] = 0

    elif direction == "LEFT":
        eastWall[row][col] = 0

    elif direction == "RIGHT":
        eastWall[row][col + 1] = 0

def generate_step():

    global current_row
    global current_col

    neighbors = get_neighbors(current_row, current_col)

    if neighbors:

        direction, nr, nc = random.choice(neighbors)

        stack.append((current_row, current_col))

        remove_wall(direction, current_row, current_col)

        current_row = nr
        current_col = nc

        visited[current_row][current_col] = True

    elif stack:

        current_row, current_col = stack.pop()


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
running = True

while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT)

    generate_step()

    draw_maze()

    draw_mouse(current_row, current_col)

    pygame.display.flip()

draw_line()
draw_maze()
draw_mouse()
get_neighbors()
remove_wall()
generate_step()

pygame.quit()