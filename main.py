import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

WIDTH = 800
HEIGHT = 800

pygame.init()

pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)

glClearColor(0, 0, 0, 1)

running = True
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
    draw_line(-0.5, 0, 0.5, 0)
    pygame.display.flip()

pygame.quit()