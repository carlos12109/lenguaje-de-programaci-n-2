import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class TriangleApp:
    def __init__(self):
        self.angle = 0.0
        self.tx = 0.0  # Traslación en X
        self.ty = 0.0  # Traslación en Y
        self.scale = 1.0  # Escalado uniforme

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(self.tx, self.ty, 0.0)
        glRotatef(self.angle, 0.0, 0.0, 1.0)
        glScalef(self.scale, self.scale, 1.0)

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
        elif key == b'a':  # Trasladar a la izquierda
            self.tx -= 0.05
        elif key == b'd':  # Trasladar a la derecha
            self.tx += 0.05
        elif key == b'w':  # Trasladar arriba
            self.ty += 0.05
        elif key == b's':  # Trasladar abajo
            self.ty -= 0.05
        elif key == b'r':  # Rotar sentido antihorario
            self.angle += 5.0
        elif key == b'e':  # Rotar sentido horario
            self.angle -= 5.0
        elif key == b'+':  # Escalar más grande
            self.scale *= 1.1
        elif key == b'-':  # Escalar más pequeño
            self.scale /= 1.1
        glutPostRedisplay()

    def special_keys(self, key, x, y):
        if key == GLUT_KEY_LEFT:
            self.tx -= 0.05
        elif key == GLUT_KEY_RIGHT:
            self.tx += 0.05
        elif key == GLUT_KEY_UP:
            self.ty += 0.05
        elif key == GLUT_KEY_DOWN:
            self.ty -= 0.05
        elif key == GLUT_KEY_F1:
            self.angle += 5.0
        elif key == GLUT_KEY_F2:
            self.angle -= 5.0
        elif key == GLUT_KEY_F3:
            self.scale *= 1.1
        elif key == GLUT_KEY_F4:
            self.scale /= 1.1
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
        glutCreateWindow(b"Triangulo 2D con colores, rotacion, traslacion y escalado")
        glClearColor(1, 1, 1, 1)
        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)
        glutKeyboardFunc(self.keyboard)
        glutSpecialFunc(self.special_keys)
        glutMainLoop()

if __name__ == "__main__":
    app = TriangleApp()
    app.run()