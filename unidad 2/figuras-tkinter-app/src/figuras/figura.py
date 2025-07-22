class Figura:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

    def mostrar_info(self):
        return f"Figura: {self.__nombre}\nArea: {self.calcular_area()}\nPerimetro: {self.calcular_perimetro()}"