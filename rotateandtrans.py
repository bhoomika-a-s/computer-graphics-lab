from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math 
x=0
y=0
x1=0
angle=45
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)
def hut():
    global x,y,angle,x1
    glClear(GL_COLOR_BUFFER_BIT)
    x=50*(math.cos(math.pi*(angle/180)))
    y=50*(math.sin(math.pi*(angle/180)))
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(x+x1,y)
    glVertex2f(y+x1,-x)
    glVertex2f(-x+x1,-y)
    glVertex(-y+x1,x)
    
    
    glEnd()
    glutSwapBuffers()
    
def animate(temp):
    global angle ,x,y,x1
    glutTimerFunc(10, animate, 0)
    glutPostRedisplay()
    if(angle>=360):
        angle=0
    angle+=1
    if x1+50>=500:
        x1=-450
    x1+=1
    
    
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(int(10000/60), 100)
    glutCreateWindow("Shapes")
    glutDisplayFunc(hut)
    glutTimerFunc(0, animate, 0)
    glutIdleFunc(hut)
    init()
    glutMainLoop()
main()