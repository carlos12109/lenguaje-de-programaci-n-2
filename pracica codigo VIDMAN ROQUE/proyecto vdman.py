#crear una aplicacion que permite gestionar libros y reservas en una bibilioteca 
#universitaria usando pogramacion orientada a objetos.

#requisitos del proyecto
#1. definir clases como libro, usuario y reserva
#2. aplicar encapsulamiento para proteger los atributos de las clases
#3. usar contenedores y destructores
#4. implementar metodos para reguistrar libros, hacer reservas y mostrar libros disponibles
#5. crear un menu de opciones para interactuar con el usuario
#6. permitir listar libros disponibles y libros reservados
#7. usar erencias

class Libro:
    def __init__(self, titulo, autor, año):
        self.__titulo = titulo
        self.__autor = autor
        self.__año = año
        self.__reservado = False

    def reservar(self):
        if not self.__reservado:
            self.__reservado = True
            return True
        return False

    def liberar(self):
        self.__reservado = False

    def esta_reservado(self):
        return self.__reservado

    def get_info(self):
        estado = "Reservado" if self.__reservado else "Disponible"
        return f"Título: {self.__titulo}, Autor: {self.__autor}, año: {self.__año}, Estado: {estado}"
    

#llamado de metodos
#mostrar libros disponibles
lib = Libro("El Quijote", "Miguel de Cervantes", 1605)
print(lib.get_info())
#reservar libro
