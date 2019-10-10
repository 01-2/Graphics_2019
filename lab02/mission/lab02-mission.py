from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import *
    

# FLAGS

IsMoving = False
IsZoom = False
##############################################################################
# vertices
##############################################################################

vertices=[#정점의 좌표
        -0.25,-0.25,0.25,
        -0.25,0.25,0.25,
        0.25,0.25,0.25,
        0.25,-0.25,0.25,
        -0.25,-0.25,-0.25,
        -0.25,0.25,-0.25,
        0.25,0.25,-0.25,
        0.25,-0.25,-0.25,
        ]
colors=[#각 정점의 색깔을 정의함 
        0.2,0.2,0.2,
        1.0,0.0,0.0,
        1.0, 1.0, 0.0,
        0.0,1.0,0.0,
        0.0,0.0,1.0,
        1.0,0.0,1.0,
        1.0,1.0,1.0,
        0.0,1.0,1.0,
        ]
indices=[ #정점 리스트 : 6면을 4개의 정점으로 한 면을 정의함
        0,3,2,1,
        2,3,7,6,
        0,4,7,3,
        1,2,6,5,
        4,5,6,7,
        0,1,5,4,
        ]

Angle=0.0
##############################################################################
def init():
    glClearColor (1.0, 1.0, 1.0, 1.0)

def drawAxis():
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex3f(0.0, -1.0, 0.0)
    glVertex3f(0.0, 1, 0.0)
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0,1,0)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(1, 0.0, 0.0)
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0,0,1)
    glVertex3f(0.0, 0.0, -1)
    glVertex3f(0.0, 0.0, 1)
    glEnd()
    
    
def MyTimer(Value):
	global Angle
	if IsMoving:
		Angle += 0.01
	else:
		pass
	glutPostRedisplay()
	glutTimerFunc(40,MyTimer,1)

def reshape_func(w, h):
	glViewport(0,0,w, h)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(60,1.0,0.01,20.0)

def disp_func():
    # clear
	glClear(GL_COLOR_BUFFER_BIT)
	glFrontFace(GL_CCW);
	glEnable(GL_CULL_FACE);
	glEnableClientState(GL_VERTEX_ARRAY)
	glEnableClientState(GL_COLOR_ARRAY)
	glVertexPointer(3, GL_FLOAT, 0, vertices) #정점변수 설정
	glColorPointer(3, GL_FLOAT, 0, colors)#정점색 저장변수 지정

    # view
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	
	zoom_normal = [ 3, 1, 3]
	zoom_high = [ 1, 0.3, 1]

	if IsZoom:
		a = zoom_high[0] * cos(Angle)
		b = zoom_high[1]
		c = zoom_high[2] * sin(Angle)
	else:
		a = zoom_normal[0] * cos(Angle)
		b = zoom_normal[1]
		c = zoom_normal[2] * sin(Angle)

	gluLookAt(a,b,c, #카메라위치->perspective때는허용됨
              0.0, 0.0, 0.0,#초점
              0.0,1.0, 0.0) #카메라방향
	
	drawAxis()
	glPushMatrix()
	glRotatef(30.0, 1.0, 1.0, 1.0)
    
    #for i in range(6):
    #    glDrawElements(GL_POLYGON,4,GL_UNSIGNED_BYTE, indices[4*i])
	glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE,indices)
	glPopMatrix()
    
	glDisableClientState(GL_COLOR_ARRAY)
	glDisableClientState(GL_VERTEX_ARRAY)
	glFlush()


def MyMainMenu(entryID):
	if entryID == 3:
		exit(0)

	glutPostRedisplay()
	return 0

def AniSubMenu(entryID):
	global IsMoving
	if entryID == 1:
		IsMoving = True
	elif entryID == 2:
		IsMoving = False

	glutPostRedisplay()
	return 0

def CamSubMenu(entryID):
	global IsZoom
	if entryID == 1:
		IsZoom = True
	elif entryID == 2:
		IsZoom = False

	glutPostRedisplay()
	return 0


def main():
	glutInit()
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA)
	glutInitWindowSize(600, 600)
	glutCreateWindow(b"Vertex Handling")
	init()    

	AniSubMenuID = glutCreateMenu(AniSubMenu)
	glutAddMenuEntry('Moving cube', 1)
	glutAddMenuEntry('Stop motion', 2)

	CamSubMenuID = glutCreateMenu(CamSubMenu)
	glutAddMenuEntry('Zoom in', 1)
	glutAddMenuEntry('Zoom out',2)

	MyMainMenuID = glutCreateMenu(MyMainMenu)
	glutAddSubMenu('Animation Mode', AniSubMenuID)
	glutAddSubMenu('Camera Position', CamSubMenuID)
	glutAddMenuEntry('Exit', 3)

	glutAttachMenu(GLUT_RIGHT_BUTTON)
	glutDisplayFunc(disp_func)
	glutTimerFunc(40,MyTimer,1)
	glutReshapeFunc(reshape_func)
	
	glutMainLoop()

if __name__=="__main__":
    main()

