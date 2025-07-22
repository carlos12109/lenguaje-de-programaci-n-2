import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class TriangleApp:
    def __init__(self):
        self.angle = 0.0

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        glRotatef(self.angle, 0.0, 0.0, 1.0)

        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)  # Rojo
        glVertex2f(-0.5, -0.5)
        glColor3f(0.0, 1.0, 0.0)  # Verde
        glVertex2f(0.5, -0.5)
        glColor3f(0.0, 0.0, 1.0)  # Azul
        glVertex2f(0.0, 0.5)
        glEnd()

        glutSwapBuffers()

    def keyboard(self, key, x, y):
        if key == b'q' or key == b'\x1b':  # ESC o 'q' para salir
            sys.exit()
        glutPostRedisplay()

    def special_keys(self, key, x, y):
        if key == GLUT_KEY_F1:
            self.angle += 5.0
        elif key == GLUT_KEY_F2:
            self.angle -= 5.0
        glutPostRedisplay()

    def reshape(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-1, 1, -1, 1)
        glMatrixMode(GL_MODELVIEW)

    def run(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
        glutInitWindowSize(500, 500)
        glutCreateWindow(b"Triangulo 2D con colores y rotacion")
        glClearColor(1, 1, 1, 1)
        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)
        glutKeyboardFunc(self.keyboard)
        glutSpecialFunc(self.special_keys)  # Captura teclas especiales
        glutMainLoop()

if __name__ == "__main__":
    app = TriangleApp()
    app.run()