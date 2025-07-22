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

    def mostrar_info(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, Especie: {self.__especie}"