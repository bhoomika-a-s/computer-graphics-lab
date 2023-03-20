from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

WINDOW_SIZE = 500
GLOBAL_SANGLE = 90
GLOBAL_MANGLE = 90
FPS = 60


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)


# def drawClock():
 #   drawCircle()


def drawCircle():
    i = 0.0
    global GLOBAL_MANGLE
    global GLOBAL_SANGLE

    glColor3f(0.4, 0.6, 0.8)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    for i in range(0, 361, 1):
        glVertex2f(200*math.cos(math.pi*i/180.0),
                   200*math.sin(math.pi*i/180.0))
    glEnd()

    x1 = 180*math.cos(math.pi*GLOBAL_SANGLE/180.0)
    y1 = 180*math.sin(math.pi*GLOBAL_SANGLE/180.0)
    x2 = 150*math.cos(math.pi*GLOBAL_MANGLE/180.0)
    y2 = 150*math.sin(math.pi*GLOBAL_MANGLE/180.0)

    glColor3f(0.8, 0.3, 0.6)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(x1, y1)
    glEnd()
    glColor3f(0.5, 0.8, 0.3)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(x2, y2)
    glEnd()
    glutSwapBuffers()


def animate(temp):
    global GLOBAL_MANGLE
    global GLOBAL_SANGLE
    global FPS

    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS), animate, int(0))

    if GLOBAL_SANGLE == 0:
        GLOBAL_SANGLE = 360
    else:
        GLOBAL_SANGLE = GLOBAL_SANGLE-24

    if GLOBAL_MANGLE == 0:
        GLOBAL_MANGLE = 360
    else:
        GLOBAL_MANGLE = GLOBAL_MANGLE-1


def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("clock")
    glutDisplayFunc(drawCircle)
    glutTimerFunc(0, animate, 0)
    glutIdleFunc(drawCircle)
    init()
    glutMainLoop()


main()