#crear un codigo python con opengl para mostrarun grafico eD (tetera) debe teber rotacion con el teclado. ademas, iluminacion
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# Variables de rotación
rot_x = 0
rot_y = 0

def init():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    # Configuración de la luz
    light_pos = [5.0, 100.0, 0.0, 20.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 0.8, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5.0)
    glRotatef(rot_x, 1.0, 0.0, 0.0)
    glRotatef(rot_y, 0.0, 1.0, 0.0)
    glColor3f(0.7, 0.0, 0.0)
    #glutSolidTeapot(1.0)
    #glutSolidSphere(1, 40, 40)
    #glutWireSphere(1, 40, 40)
    #glutSolidCone(1.0, 2.0, 40, 20)
    glutWireRhombicDodecahedron()
    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(w)/float(h or 1), 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    global rot_x, rot_y
    if key == b'\x1b':  # ESC
        sys.exit()
    elif key == b'a':
        rot_y -= 5
    elif key == b'd':
        rot_y += 5
    elif key == b'w':
        rot_x -= 5
    elif key == b's':
        rot_x += 5
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Tetera 3D con Rotacion e Iluminacion")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()