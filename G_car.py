from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

WINDOW_SIZE = 500
X = 0.0
Y = 0.0
FPS=60
angle=90.0
limit=0

def init():
    glClearColor(0.0,0.0,0.0,0.1)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def drawCube(): # function to draw a cube 
    global X,Y,angle
    glClear(GL_COLOR_BUFFER_BIT) # to clear the window

    glBegin(GL_QUADS)
    glColor3f(1.0,1.0,0.0)
    glVertex2f(X+50,Y-25)
    glVertex2f(X+50,Y+25)
    glVertex2f(X-50,Y+25)
    glVertex2f(X-50,Y-25)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(X-20,Y-20)
    for i in range(0,360,1):
        glVertex2f(13*math.cos(i*math.pi/180)+X-20, 13*math.sin(i*math.pi/180)+Y-20)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(X+20,Y-20)
    for i in range(0,360,1):
        glVertex2f(13*math.cos(i*math.pi/180)+X+20, 13*math.sin(i*math.pi/180)+Y-20)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(1.0,1.0,0.0)
    glVertex2f(X-20,Y-20)
    glVertex2f(13*math.cos(angle*math.pi/180)+X-20, 13*math.sin(angle*math.pi/180)+Y-20)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(1.0,1.0,0.0)
    glVertex2f(X+20,Y-20)
    glVertex2f(13*math.cos(angle*math.pi/180)+X+20, 13*math.sin(angle*math.pi/180)+Y-20)
    glEnd()

    glutSwapBuffers()

def animate(key):
    global WINDOW_SIZE
    global X,Y,FPS,angle
    global limit
    #if(key=='d'):
     #  if(X+50>=WINDOW_SIZE):
      #      X=-WINDOW_SIZE+50
       # else:
        #    X=X+1
        #angle = angle -1
    #elif(key=='a'):
     #   if(X+50<=-WINDOW_SIZE):
      #      X=WINDOW_SIZE-50
       # else:
        #    X=X-1
       # angle = angle + 1

    if limit == 0 :
        angle=angle-1  
        X=X+1      
        if(X+50 >= WINDOW_SIZE):
            limit = 1
    if limit == 1:
        angle=angle+1  
        X=X-1      
        if(X+50 <= -WINDOW_SIZE):
            limit = 0

    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,int(0))

def keyboard(key,X,Y):
    key=key.decode()
    if(key=='a'):
       animate('a')
    elif(key=='d'):
       animate('d')



def main():
    #X = int(input("Enter the first coordinate with which uou want to draw a square: "))
    #Y = int(input("Enter the first coordinate with which uou want to draw a square: "))

    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("moving cube")
    glutKeyboardFunc(keyboard)
    glutDisplayFunc(drawCube)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawCube)
    init()
    glutMainLoop()

main()