class Figura:
    def __init__ (self, triangulo):
        self.triangulo=triangulo
    
    def descripcion(self):
        return f"la figura es {self.triangulo}"
    
class triangulo(Figura):
    def __init__ (self, triangulo, base, altura, lado):
        super().__init__(triangulo)
        self.base = base 
        self.altura = altura
        self.lado = lado

    def op_area(self):
        resultado = (self.base * self.altura)/2
        return f"el area es: {resultado}"
    def op_perimetro(self):
        resultado2 = self.base + self.lado + self.lado
        return f"el perimetro es: {resultado2}"
resul = triangulo("",12, 15, 16.16)
print(resul.op_area())
print(resul.op_perimetro())