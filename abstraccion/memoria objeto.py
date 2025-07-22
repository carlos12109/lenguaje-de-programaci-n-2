import sys as sysget

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad= edad

p1=persona("Juan",25)
tamaño = sysget.getsizeof(p1)
print(f"El tamaño de la variable es: {tamaño} bytes")