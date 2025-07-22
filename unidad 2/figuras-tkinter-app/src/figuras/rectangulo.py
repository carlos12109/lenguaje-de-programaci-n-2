class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectangulo")
        self.__base = base
        self.__altura = altura

    def get_base(self):
        return self.__base

    def get_altura(self):
        return self.__altura

    def calcular_area(self):
        return self.__base * self.__altura

    def calcular_perimetro(self):
        return 2 * (self.__base + self.__altura)