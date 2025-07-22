import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Ángulos de rotación
rot_x = 0
rot_y = 0

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5.0)
    glRotatef(rot_x, 1.0, 0.0, 0.0)
    glRotatef(rot_y, 0.0, 1.0, 0.0)
    glColor3f(0.5, 0.8, 0.9)
    #glutSolidTeapot(1.0)
    #glutWireSphere(1, 20, 20) (1, 20, 20)
    #glutSolidSphere(1, 20, 20)  # Cambiado a glutWireTeapot para una tetera alámbrica
    #glutSolidTorus(0.3, 0.8, 20, 20)
    #glutWireIcosahedron()
    #glutWireOctahedron()
    #glutWireTetrahedron()
    #glutWireCube(1.0)  # Cubo alámbrico
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    global rot_x, rot_y
    if key == b'\x1b':  # ESC
        sys.exit()
    elif key == b'w':
        rot_x -= 5
    elif key == b's':
        rot_x += 5
    elif key == b'a':
        rot_y -= 5
    elif key == b'd':
        rot_y += 5
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Tetera 3D con rotacion - OpenGL")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()