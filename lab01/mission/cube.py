# Draw cube
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

vertices = [[-0.5, 0.5, -0.5],
			[-0.5, 0.5, 0.5],
			[0.5, 0.5, 0.5],
			[0.5, 0.5, -0.5],
			[-0.5, -0.5, -0.5],
			[-0.5, -0.5, 0.5],
			[0.5, -0.5, 0.5],
			[0.5, -0.5, -0.5]]

pattern = [[0,3,2,1],
			[1,2,6,5],
			[3,7,6,2],
			[0,3,7,4],
			[7,4,5,6],
			[4,0,1,5]]

colors = [[1.0, 0.0, 0.0],
			[0.0, 0.0, 1.0],
			[0.0, 1.0, 0.0],
			[1.0, 1.0, 0.0],
			[1.0, 0.0, 1.0],
			[0.0, 1.0, 1.0]]

def MyDisplay():
	glClear(GL_COLOR_BUFFER_BIT) # Buffer clear
	glViewport(0,0,300,300)
	
	glRotatef(30, 1.0, 0.0, 0.0)
	glRotatef(30, 0.0, 0.0, 1.0)
	glBegin(GL_QUADS)
	
	for i in range(len(pattern)):
		glColor3f(colors[i][0], colors[i][1], colors[i][2])
		for j in range(len(pattern[i])):
			glVertex3f(vertices[pattern[i][j]][0],
					vertices[pattern[i][j]][1],
					vertices[pattern[i][j]][2])
	
	glEnd()
	glFlush()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowSize(300,300)
	glutInitWindowPosition(0,0)
	glutCreateWindow(b"LAB01 - CUBE")
	# not only string, put 'b' in front of string
	glClearColor(0.0, 0.0, 0.0, 1.0)

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
	glutDisplayFunc(MyDisplay)
	glutMainLoop()

if __name__ == '__main__' : main()
	
