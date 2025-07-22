#clase base o interfaz


class Curso:
    def calcular_nota_final (self):
        pass

#2. clases con comportamiento diferentes POLIMORFISMO
class CursoTeorico(Curso):
    def __init__ (self, examen, tareas):
        self.examen= examen
        self.tareas=tareas

    def calcular_nota_final(self):
        return self.examen * 0.7 + self.tareas * 0.3

class CursoPractico(Curso):
    def __init__ (self, practicas, asistencias):
        self.practicas = practicas
        self.asistencias=asistencias

    def calcular_nota_final(self):
        return 0.8*self.practicas + 0.2 * self.asistencias

class CursoProyecto(Curso):
    def __init__ (self, proyecto, exposicion):
        self.proyecto = proyecto
        self.exposicion = exposicion

    def calcular_nota_final(self):
        return 0.6 * self.proyecto + 0.4 * self.exposicion

#uso polimorfico
cursos = [CursoTeorico(examen=16, tareas=18), CursoPractico(practicas = 17, asistencias=19), CursoProyecto(proyecto=18, exposicion=17)]
for curso in cursos:


    print(f"nota final:  {curso.calcular_nota_final():.2f}")


#def mostrar_perimetro(figura):
#    print(f"Perímetro: {figura.calcular_perimetro():.2f}")

