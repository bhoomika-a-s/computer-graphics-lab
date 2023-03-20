from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

WINDOW_SIZE=500
X=0.0
Y=0.0
angle=0.0
fps=60

def init():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def drawCircle():
    global X,Y,angle

    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0,0.0,1.0)
    glVertex2f(X,Y)
    for i in range(0,361,1):
        glVertex2f(100*math.cos(i*math.pi/180)+X,100*math.sin(i*math.pi/180)+Y)
    glEnd()

    glColor3f(1.0,0.0,0.)
    glBegin(GL_LINES)
    glVertex2f(100*math.cos(math.pi*angle/180)+X,100*math.sin(math.pi*angle/180)+Y)
    glVertex2f(-100*math.cos(math.pi*angle/180)+X,-100*math.sin(math.pi*angle/180)+Y)
    glEnd()

    glColor3f(1.0,0.0,0.)
    glBegin(GL_LINES)
    glVertex2f(100*math.sin(math.pi*angle/180)+X,-100*math.cos(math.pi*angle/180)+Y)
    glVertex2f(-100*math.sin(math.pi*angle/180)+X,100*math.cos(math.pi*angle/180)+Y)
    glEnd()
    
    glutSwapBuffers()

def animate(temp):
    global fps,angle,X
    if(X+100>=500):
        X=-400
    X+=1
    if angle<=0:
        angle=360
    angle-=1

    glutPostRedisplay()
    glutTimerFunc(6,animate,int(0))
    
def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(50,50)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("circle")
    glutDisplayFunc(drawCircle)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawCircle)
    init()
    glutMainLoop()

main()