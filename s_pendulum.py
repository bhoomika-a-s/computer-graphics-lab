from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

WINDOW_SIZE = 500
x=0.0
y=0.0
fps=60
angle=250
mode=1


def init():
    glClearColor(0.0,0.0,0.0,0.1)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def drawPendulum():

    global x,y,angle

    glClear(GL_COLOR_BUFFER_BIT)
    
    glBegin(GL_LINES)
    glColor3f(1.0,1.0,0.0)
    glVertex2f(x,y)
    glVertex2f(300*math.cos(angle*math.pi/180)+x,300*math.sin(angle*math.pi/180)+y)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(300*math.cos(angle*math.pi/180)+x,300*math.sin(angle*math.pi/180)+y)
    for i in range(0,360,1):
        glVertex2f(50*math.cos(i*math.pi/180)+300*math.cos(angle*math.pi/180),50*math.sin(i*math.pi/180)+300*math.sin(angle*math.pi/180))
    glEnd()

    glutSwapBuffers()

def animate(temp):

    global angle,mode

    if mode==1:
        angle=angle+1
        if(angle==325):
            mode=0
    if mode==0:
        angle=angle-1
        if(angle==200):
            mode=1

    glutPostRedisplay()
    glutTimerFunc(int(1000/fps),animate,0)

def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(50,50)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("pendulum")
    glutDisplayFunc(drawPendulum)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawPendulum)
    init()
    glutMainLoop()

main()