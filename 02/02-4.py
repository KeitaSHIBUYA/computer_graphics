from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH)
    glutInitWindowSize(300, 300)     # window size
    glutInitWindowPosition(100, 100)  # window position
    glutCreateWindow("2-4課題")      # show window
    glutDisplayFunc(display)         # draw callback function
    glutReshapeFunc(reshape)         # resize callback function
    init(300, 300)
    glutMainLoop()


def init(width, height):
    """ initialize """
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)  # enable shading

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # set perspective
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)


def display():
    """ display """
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 1.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0, 0, 5)
    glVertex3f(0, 0, -5)

    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)

    glVertex3f(0, 5, 0)
    glVertex3f(0, -5, 0)

    glEnd()

    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(5, 0, 0)
    glVertex3f(0, 0, 0)

    glEnd()

    # set camera
    gluLookAt(0.0, 1.0, 15.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    # draw a yellow teapot
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glTranslatef(0, 5, 0)
    glColor3f(1.0, 0.945, 0.0)
    glutWireTeapot(1.0)   # wireframe
    glPopMatrix()

    # draw a cyaan teapot
    glPushMatrix()
    glTranslatef(0, 5, 0)
    glRotatef(90, 1, 0, 0)
    glColor3f(0.0, 0.945, 1.0)
    glutWireTeapot(1.0)   # wireframe
    glPopMatrix()

    glFlush()  # enforce OpenGL command


def reshape(width, height):
    """callback function resize window"""
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)


if __name__ == "__main__":
    main()
