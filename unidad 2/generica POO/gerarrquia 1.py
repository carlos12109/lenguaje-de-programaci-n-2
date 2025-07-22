#clase base 1
class Base:
    def __init__(self, base):
        self.base = base

#clase base 2
class Altura:
    def __init__(self, altura):
        self.altura=altura

#clase hija, herencia de base y altura
class Triangulo(Base, Altura):
    def __init__(self, base, altura):
        Base.__init__(self,base)
        Altura.__init__(self,altura)

    def area(self):
        return (self.base*self.altura)/2
    

t = Triangulo(10, 5)
print(f"base: {t.base}")
print(f"altura: {t.altura}")

print(f"area del triangulo: {t.area()} unidades al cuadrado")
