from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import sys


def skew_x(point, a):
    skew_x_matrix =  # 2x2 matrix of skew with a as a parameter ##
    point =  # The product of a matrix and point ##
    return point


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Skew triangle")
    glutDisplayFunc(display)
    init()
    glutMainLoop()


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    """ gluOrtho2D(left, right, bottom, top) """
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)    # The coordinate system to draw


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw a red triangle
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    t1 = np.array([-0.75, -0.75])
    t2 = np.array([-0.25, -0.75])
    t3 = np.array([-0.5, 0.5])
    t1 = skew_x(t1, 0.5)
    t2 = skew_x(t2, 0.5)
    t3 = skew_x(t3, 0.5)

    glVertex2f(t1[0], t1[1])
    glVertex2f(t2[0], t2[1])
    glVertex2f(t3[0], t3[1])
    glEnd()

    # Draw a blue square
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    q1 = np.array([0, 0])
    q2 = np.array([0.5, 0])
    q3 = np.array([0.5, 0.5])
    q4 = np.array([0, 0.5])
    q1 = skew_x(q1, 1)
    q2 = skew_x(q2, 1)
    q3 = skew_x(q3, 1)
    q4 = skew_x(q4, 1)

    glVertex2f(q1[0], q1[1])
    glVertex2f(q2[0], q2[1])
    glVertex2f(q3[0], q3[1])
    glVertex2f(q4[0], q4[1])
    glEnd()

    glFlush()


if __name__ == "__main__":
    main()
