# Draw pentagon
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def MyDisplay():
	glClear(GL_COLOR_BUFFER_BIT) # Buffer clear
	glViewport(0,0,300,300)
	glColor3f(1.0, 1.0, 1.0)
	glBegin(GL_POLYGON)

	for i in range(0, 5):
		glVertex3f(0.5 * math.sin(i * 72 * math.pi/180), 
				0.5 * math.cos(i * 72 * math.pi /180), 0,0)

	glEnd()
	glFlush()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowSize(300,300)
	glutInitWindowPosition(0,0)
	glutCreateWindow(b"LAB01 - PENTAGON")
	# not only string, put 'b' in front of string
	glClearColor(0.0, 0.0, 0.0, 1.0)

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
	glutDisplayFunc(MyDisplay)
	glutMainLoop()

if __name__ == '__main__' : main()
	
