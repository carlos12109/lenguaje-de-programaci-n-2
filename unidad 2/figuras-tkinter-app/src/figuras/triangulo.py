class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Triangulo")
        self.__base = base
        self.__altura = altura

    def get_base(self):
        return self.__base

    def get_altura(self):
        return self.__altura

    def calcular_area(self):
        return (self.__base * self.__altura) / 2

    def calcular_perimetro(self, lado1, lado2):
        return self.__base + lado1 + lado2

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Base: {self.__base}")
        print(f"Altura: {self.__altura}")