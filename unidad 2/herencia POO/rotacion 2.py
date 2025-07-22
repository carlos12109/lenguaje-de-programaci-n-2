import sys
import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Vertices del triángulo (x, y)
vertices = np.array([
    [0.0,  0.5],
    [-0.5, -0.5],
    [0.5, -0.5]
], dtype=np.float32)

# Colores para cada vértice (r, g, b)
colors = np.array([
    [1.0, 0.0, 0.0],  # Rojo
    [0.0, 1.0, 0.0],  # Verde
    [0.0, 0.0, 1.0]   # Azul
], dtype=np.float32)

angle = 0.0  # Ángulo de rotación en grados

def rotation_matrix(theta_deg):
    theta = np.radians(theta_deg)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    return np.array([
        [cos_t, -sin_t],
        [sin_t,  cos_t]
    ], dtype=np.float32)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Aplicar rotación a los vértices
    rot = rotation_matrix(angle)
    rotated_vertices = np.dot(vertices, rot.T)

    glBegin(GL_TRIANGLES)
    for i in range(3):
        glColor3fv(colors[i])
        glVertex2fv(rotated_vertices[i])
    glEnd()

    glutSwapBuffers()

def keyboard(key, x, y):
    global angle
    if key == b'q' or key == b'\x1b':  # ESC o 'q' para salir
        sys.exit()
    elif key == b'a':  # Rotar a la izquierda
        angle += 5
    elif key == b'd':  # Rotar a la derecha
        angle -= 5
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Triangulo 2D con Rotacion - PyOpenGL")
    glClearColor(1, 1, 1, 1)
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()