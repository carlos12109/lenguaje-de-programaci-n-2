import csv  # Importamos módulo para exportar en formato CSV

# === HERENCIA ===
class Persona:
    def __init__(self, nombre, dni):
        self.__nombre = nombre #Atributos encapsulados
        self.__dni = dni

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_dni(self):
        return self.__dni
    """
    #setters para modificar atributos
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_dni(self, nuevo_dni):
        self.__dni = nuevo_dni
    """
# === ENCAPSULAMIENTO ===
class Libro:
    def __init__(self, titulo, autor, codigo):
        self.__titulo = titulo
        self.__autor = autor
        self.__codigo = codigo
        self.__disponible = True

    def __del__(self):
        print(f"Destructor de Libro: '{self.__titulo}' ha sido eliminado.")

    def get_titulo(self): return self.__titulo
    def get_autor(self): return self.__autor
    def get_codigo(self): return self.__codigo
    def esta_disponible(self): return self.__disponible

    def reservar(self): self.__disponible = False
    def liberar(self): self.__disponible = True

# Reserva hereda de Persona
class Reserva(Persona):
    def __init__(self, nombre, dni, libro):
        super().__init__(nombre, dni)
        self.__libro = libro

    def __del__(self):
        print(f"Destructor de Reserva: Reserva de {self.get_nombre()} eliminada.")

    def get_libro(self): return self.__libro

# codigo biblioteca
class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__reservas = []

    # Destructor de objetos
    def __del__(self):
        print("Destructor de Biblioteca: Recursos liberados correctamente.")

    def registrar_libro(self, titulo, autor, codigo):
        libro = Libro(titulo, autor, codigo)
        self.__libros.append(libro)
        print("Libro registrado correctamente.")

    def hacer_reserva(self, nombre_usuario, codigo, dni):
        libro = next((l for l in self.__libros if l.get_codigo() == codigo and l.esta_disponible()), None)
        if libro:
            libro.reservar()
            reserva = Reserva(nombre_usuario, dni, libro)
            self.__reservas.append(reserva)
            print("Reserva realizada con éxito.")
        else:
            print("Error: libro no disponible o no encontrado.")

    def mostrar_libros_disponibles(self):
        disponibles = [libro for libro in self.__libros if libro.esta_disponible()]
        if disponibles:
            print("\nLibros disponibles:")
            for libro in disponibles:
                print(f"{libro.get_titulo()} - {libro.get_autor()} - Código: {libro.get_codigo()}")
        else:
            print("No hay libros disponibles.")

    def mostrar_libros_reservados(self):
        if self.__reservas:
            print("\nLibros reservados:")
            for reserva in self.__reservas:
                libro = reserva.get_libro()
                print(f"Título del libro: {libro.get_titulo()} - Nombre: {reserva.get_nombre()} - DNI: {reserva.get_dni()} - Código: {libro.get_codigo()}")
        else:
            print("No hay libros reservados.")

    def exportar_txt(self, nombre_archivo="libros.txt"):
        with open(nombre_archivo, "w") as f:
            f.write("Listado de Libros:\n")
            for libro in self.__libros:
                estado = "Disponible" if libro.esta_disponible() else "Reservado"
                f.write(f"{libro.get_titulo()} - {libro.get_autor()} - Código: {libro.get_codigo()} - {estado}\n")
        print(f"Datos exportados a {nombre_archivo}")

    def exportar_csv(self, nombre_archivo="libros.csv"):
        with open(nombre_archivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Título", "Autor", "Código", "Estado"])
            for libro in self.__libros:
                estado = "Disponible" if libro.esta_disponible() else "Reservado"
                writer.writerow([libro.get_titulo(), libro.get_autor(), libro.get_codigo(), estado])
        print(f"Datos exportados a {nombre_archivo}")

# Menu principal
#instancia de la biblioteca
def menu():
    biblioteca = Biblioteca()   
    while True:
        print("\n---BIBLIOTECA UNIVERSITARIA ---")
        print("1. Registrar libro")
        print("2. Hacer reserva")
        print("3. Mostrar libros disponibles")
        print("4. Mostrar libros reservados")
        print("5. Exportar a TXT")
        print("6. Exportar a CSV")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            codigo = input("Código: ")
            biblioteca.registrar_libro(titulo, autor, codigo)

        elif opcion == "2":
            nombre_usuario = input("Nombre y Apellido: ")
            dni = input("DNI: ")
            codigo = input("Código de Libro: ")
            biblioteca.hacer_reserva(nombre_usuario, codigo, dni)

        elif opcion == "3":
            biblioteca.mostrar_libros_disponibles()

        elif opcion == "4":
            biblioteca.mostrar_libros_reservados()

        elif opcion == "5":
            biblioteca.exportar_txt()

        elif opcion == "6":
            biblioteca.exportar_csv()

        elif opcion == "7":
            print("¡Hasta pronto!")
            del biblioteca
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
