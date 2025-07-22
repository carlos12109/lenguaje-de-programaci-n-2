class Triangulo:
    def _init_(self):
        self.base = int(input("ingrese la base"))
        self.altura = int(input("ingrese la altura"))
        self.area = (self.base * self.altura)/2
        self.perimetro = self.base + self.altura + (self.base*2 + self.altura2)*(1/2)
        print(f"Constructor ; se creo el perimetro y area  de {self.base} y {self.altura} ")

    def  mostrar_resultado(self):
        print(f"El resultado del area es : {self.area}")
        print(f"El resultado del perimetro es : {self.perimetro}")
    def _del_(self):
        print(f"Destructor: se elimino el perimetro y area  de {self.base} y {self.altura} ")

triangulo = Triangulo()

triangulo.mostrar_resultado()
triangulo._del_()