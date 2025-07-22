class Vehiculo:
    def __init__(self, marca, modelo, annio):
        self.__marca = marca
        self.__modelo = modelo
        self.__annio = int(annio)
    
    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo
    def get_annio(self):
        return self.__annio

    def calcular_impuesto(self):
        pass
    def mostrar_info(self):
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__annio}, Impuesto: {self.calcular_impuesto()}"
    
class Auto(Vehiculo):
    def __init__(self, marca, modelo, annio, impuesto_base):
        super().__init__(marca, modelo, annio)
        self.__impuesto_base = float(impuesto_base)

    def get_impuesto(self):
        return self.__impuesto_base
    
    def calcular_impuesto(self):
        if self.get_annio() < 2010:
            recargo = 50
        else:
            recargo = 100
        return self.__impuesto_base + recargo

class Moto(Vehiculo):
    def __init__(self, marca, modelo, annio, impuesto_base):
        super().__init__(marca, modelo, annio)
        self.__impuesto_base = float(impuesto_base)

    def get_impuesto(self):
        return self.__impuesto_base
    
    def calcular_impuesto(self):
        return self.__impuesto_base
    

def main():
    lista_vehiculos = []
    while True:
        print(" ")
        print("_________________________________________")
        print("*****Ingrese los datos del vehículo***** \n")
        print("1. Registrar auto")
        print("2. Registrar moto")
        print("3. Mostrar todos los vehículos")
        print("4. Salir\n")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            marca = input("Ingrese la marca del auto: ")
            modelo = input("Ingrese el modelo del auto: ")
            annio = input("Ingrese el año del auto: ")
            impuesto_base = float(input("Ingrese el impuesto base del auto: "))
            a = Auto(marca, modelo, annio, impuesto_base)
            lista_vehiculos.append(a)
            print("\n°°°°°°Auto registrado exitosamente°°°°°\n")
        elif opcion == "2":
            marca = input("Ingrese la marca de la moto: ")
            modelo = input("Ingrese el modelo de la moto: ")
            annio = input("Ingrese el año de la moto: ")
            impuesto_base = float(input("Ingrese el impuesto base de la moto: "))
            r = Moto(marca, modelo, annio, impuesto_base)
            lista_vehiculos.append(r)
            print("\n°°°°°°Moto registrada exitosamente°°°°°\n")
        elif opcion == "3":
            if not lista_vehiculos:
                print("\nNo hay vehículos registrados.\n")
            else:
                for vehiculo in lista_vehiculos:
                    print(vehiculo.mostrar_info())
        elif opcion == "4":
            print(" ")
            print("\nSaliendo del programa.\n")
            break
        else:
            print("\nOpción no válida. Intente de nuevo.\n")

if __name__ == "__main__":
    main()

