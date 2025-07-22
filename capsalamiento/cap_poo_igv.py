class producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
    #getter
    def obtener_nombre(self):
        return self.__nombre

    def obtener_precio(self):
        return self.__precio

    #setter
    def establecer_precio(self, nuevo_precio):
        if nuevo_precio >=0:
            self.__precio = nuevo_precio
        else:
            print("El precio no puede ser negativo")


    def calcular_igv(self):
        return self.__precio * 1.18

    def mostrar_informacion(self):
        print(f"Nombre del producto: {self.__nombre}")
        print(f"Precio con igv: S/. {self.calcular_igv(): .2f}")


#uso de la clase preducto
producto1= producto("Laptop", 1000)
producto1.mostrar_informacion()

print("\n--------modificado---------")
producto1.establecer_precio(3000)
producto1.mostrar_informacion()