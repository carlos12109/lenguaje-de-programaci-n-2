class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.valido = True
        if anio < 1980 or anio > 2025:
            print("Año invalido:", anio)
            print ("El año debe estar entre 1980 y 2025\n")

            self.valido = False
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def mostrar_info(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Año:", self.anio)

    def calcular_impuesto(self):
        return 0

class Auto(Vehiculo):
    def calcular_impuesto(self):
        return 0.05 * (2025 - self.anio)

class Motocicleta(Vehiculo):
    def calcular_impuesto(self):
        return 0.03 * (2025 - self.anio)

class Camioneta(Vehiculo):
    def calcular_impuesto(self):
        if self.anio > 2015:
            return 500
        else:
            return 300

vehiculos = []

datos = [
    ("Toyota", "corolla", 2010, Auto),
    ("Yamaha", "mt09", 2019, Motocicleta),
    ("Ford", "export", 2030, Camioneta),
    ("toyota", "jailux", 2018, Camioneta),
    ("yamaha", "r1M", -2018, Motocicleta),
]

for marca, modelo, anio, clase in datos:
    dato = clase(marca, modelo, anio)
    if dato.valido:
        vehiculos.append(dato)

for i in vehiculos:
    print("=" * 30)
    i.mostrar_info()
    print("Impuesto:", i.calcular_impuesto())
    print("=" * 30)
