class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_informacion(self):
        print("\n---informacion del producto---")
        print("nombre: ",self.nombre)
        print("precio: ", self.precio)
        print("stock: ",self.stock)
        print("-----------------------------")

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        print("\nEl precio del producto ha sido actualizado a: ")


    def actualizar_stock(self, nuevo_stock):
        self.stock = nuevo_stock
        print("stock actualizado correctamente: ", self.stock)

    #metodo para aplicar descuento
    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        print(f"el descuento del {porcentaje}% palicado. Nuevo precio $ {self.precio}")

    #metodo para realizar venta
    def realizar_venta(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Venta realizada. unidades vendidas: {cantidad}: precio total: {self.precio*cantidad}")

            print(f"stock restante para realizar la venta: {self.stock}")
        else:
            print("No hay suficiente stock para realizar la venta.")
            print("Stock disponible: ", self.stock)
            print("Cantidad solicitada: ", cantidad)
            print("Venta no realizada.")

#crear objeto de la clase Producto
producto1 = Producto("Arroz", 3.50, 100)
producto2 = Producto("zucar", 4.50, 50)
producto3 = Producto("aciete", 8.00, 80)
producto4 = Producto("leche", 4.50, 60)

#mostrar la informacion de los productos
producto1.mostrar_informacion()
producto2.mostrar_informacion()
producto3.mostrar_informacion()
producto4.mostrar_informacion()

#modificar el precio de un producto
#producto1.actualizar_precio()
#producto1.actualizar_stock()

#aplicar descuento y mostrar la nueva informacion
producto1.aplicar_descuento(10) #aplicar el descuento del 10%
producto1.mostrar_informacion()

#realizar venta
producto1.realizar_venta(20) #realiza la venta de 20 unidades
producto1.mostrar_informacion()

#intentr vender mas unidades de las que hay en stock
producto1.realizar_venta(90) #intenta vender 90 unidades pero no hay suficiente stock