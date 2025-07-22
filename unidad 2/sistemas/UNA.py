from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

def dibujar_contornos():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 20, 0, 0, 0, 0, 1, 0)

    glColor3f(1, 1, 0)  # Amarillo

    # Letra U
    glBegin(GL_LINE_STRIP)
    glVertex3f(-7, 3, 0)
    glVertex3f(-7, -3, 0)
    glVertex3f(-3, -3, 0)
    glVertex3f(-3, 3, 0)
    glEnd()

    # Letra N 
    glBegin(GL_LINE_STRIP)
    glVertex3f(-2, -3, 0)
    glVertex3f(-2, 3, 0)
    glVertex3f(2, -3, 0)
    glVertex3f(2, 3, 0)
    glEnd()

    # Letra A
    glBegin(GL_LINE_STRIP)
    glVertex3f(3, -3, 0)
    glVertex3f(5, 3, 0)
    glVertex3f(7, -3, 0)
    glEnd()

    glBegin(GL_LINE_LOOP)  # barra horizontal
    glVertex3f(3.666, -1, 0)
    glVertex3f(6.333, -1, 0)
    glEnd()

    glutSwapBuffers()

def redimensionar(ancho, alto):
    if alto == 0:
        alto = 1
    glViewport(0, 0, ancho, alto)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, ancho / alto, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Contornos de UNA")
    glutDisplayFunc(dibujar_contornos)
    glutReshapeFunc(redimensionar)
    glutMainLoop()

if __name__ == "__main__":
    main()