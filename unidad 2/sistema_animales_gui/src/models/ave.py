class Animal:
    def __init__(self, nombre, edad, especie):
        self.__nombre = nombre
        self.__edad = edad
        self.__especie = especie

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_especie(self):
        return self.__especie

    def hacer_sonido(self):
        pass

    def mostrar_info(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, Especie: {self.__especie},"

class Ave(Animal):
    def __init__(self, nombre, edad, especie, tipo_pico):
        super().__init__(nombre, edad, especie)
        self.__tipo_pico = tipo_pico

    def hacer_sonido(self):
        return "Pío pío"

    def mostrar_info(self):
        return super().mostrar_info() + f" Tipo de pico: {self.__tipo_pico}, Sonido: {self.hacer_sonido()}"