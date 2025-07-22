class Felino(Animal):
    def __init__(self, nombre, edad, especie, color_pelaje):
        super().__init__(nombre, edad, especie)
        self.__color_pelaje = color_pelaje

    def hacer_sonido(self):
        return "Grrr"

    def mostrar_info(self):
        return super().mostrar_info() + f" Color de pelaje: {self.__color_pelaje}, Sonido: {self.hacer_sonido()}"