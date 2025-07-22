class Rectangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def calcular_area(self):
        return self.__base * self.__altura
    
    def calcular_perimetro(self):
        return 2 * (self.__base + self.__altura)

    # Setter para altura
    def nueva_altura(self, nueva_altura):
        if nueva_altura > 0:
            self.__altura = nueva_altura
        else:
            print("Error, la altura no puede ser negativa o cero")

    # Setter para base
    def nueva_base(self, nueva_base):
        if nueva_base > 0:
            self.__base = nueva_base
        else:
            print("Error, la base no puede ser negativa o cero")
    
    def consultar_datos(self):
        print(f"Base: {self.__base} | Altura: {self.__altura}")


# Objetos y pruebas
rectangulo1 = Rectangulo(5, 10)
rectangulo1.consultar_datos()
print(f"Área: {rectangulo1.calcular_area()}")
print(f"Perímetro: {rectangulo1.calcular_perimetro()}")

print("\n---- Modificado ----")
rectangulo1.nueva_base(6)
rectangulo1.nueva_altura(8)
rectangulo1.consultar_datos()
print(f"Area: {rectangulo1.calcular_area()}")
print(f"Perímetro: {rectangulo1.calcular_perimetro()}")

