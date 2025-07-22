class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.notas = []

    # método para agregar notas
    def Agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio_notas(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def es_aprobado(self):
        promedio = self.promedio_notas()
        return promedio >= 11

    def mostrar_informacion(self):
        promedio = self.promedio_notas()
        aprobado = 'Sí' if self.es_aprobado() else 'No'
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Carrera:", self.carrera)
        print("Notas:", self.notas)
        print(f"Promedio: {promedio:.2f}")
        print("Aprobado:", aprobado)


lista_estudiantes = []
n = int(input("Cuántos estudiantes deseas ingresar?: "))

# registro de datos por teclado
for i in range(n):
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad: "))
    carrera = input("Ingrese la carrera: ")

    estudiante = Estudiante(nombre, edad, carrera)
    cantidad_notas = int(input("Cuántas notas desea ingresar?: "))

    for j in range(cantidad_notas):
        nota = float(input(f"Ingrese la nota {j + 1}: "))
        estudiante.Agregar_nota(nota)  # Corrected method name

    lista_estudiantes.append(estudiante)

print("\n====== Información de los estudiantes ======")
for estudiante in lista_estudiantes:
    estudiante.mostrar_informacion()
