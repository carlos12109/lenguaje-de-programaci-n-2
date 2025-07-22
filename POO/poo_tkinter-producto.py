import tkinter as tk
from tkinter import simpledialog
from datetime import datetime

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = float(precio)
        self.stock = int(stock)

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento

    def realizar_venta(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True, self.precio * cantidad
        else:
            return False, 0.0

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Productos")
        self.root.configure(bg="#f0f0f0")
        self.productos = []

        self.crear_widgets()

    def crear_widgets(self):
        # Frame Agregar Producto
        frame_agregar = tk.LabelFrame(self.root, text="Agregar Producto", bg="#e0f7fa", padx=10, pady=10)
        frame_agregar.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        tk.Label(frame_agregar, text="Nombre:", bg="#e0f7fa").grid(row=0, column=0, sticky="w")
        tk.Label(frame_agregar, text="Precio:", bg="#e0f7fa").grid(row=1, column=0, sticky="w")
        tk.Label(frame_agregar, text="Stock:", bg="#e0f7fa").grid(row=2, column=0, sticky="w")

        self.nombre_entry = tk.Entry(frame_agregar)
        self.precio_entry = tk.Entry(frame_agregar)
        self.stock_entry = tk.Entry(frame_agregar)
        self.nombre_entry.grid(row=0, column=1)
        self.precio_entry.grid(row=1, column=1)
        self.stock_entry.grid(row=2, column=1)

        tk.Button(frame_agregar, text="Agregar", bg="#00acc1", fg="white", command=self.agregar_producto).grid(row=3, column=0, columnspan=2, pady=5)

        # Frame Lista Productos
        frame_lista = tk.LabelFrame(self.root, text="Productos", bg="#f1f8e9", padx=10, pady=10)
        frame_lista.grid(row=0, column=1, padx=10, pady=10, sticky="n")

        self.lista_productos = tk.Listbox(frame_lista, width=50, height=10)
        self.lista_productos.grid(row=0, column=0, columnspan=2)

        tk.Button(frame_lista, text="Modificar Precio", bg="#7cb342", fg="white", command=self.modificar_precio).grid(row=1, column=0, pady=5)
        tk.Button(frame_lista, text="Vender Producto", bg="#f57c00", fg="white", command=self.vender_producto).grid(row=1, column=1, pady=5)

        # Mensaje informativo
        self.lbl_mensaje = tk.Label(self.root, text="", font=("Arial", 10, "italic"), bg="#e0f7fa", fg="green")
        self.lbl_mensaje.grid(row=1, column=0, columnspan=2, pady=5, sticky="ew")

    def mostrar_mensaje(self, texto, color="green"):
        self.lbl_mensaje.config(text=texto, fg=color)
        self.lbl_mensaje.after(5000, lambda: self.lbl_mensaje.config(text=""))  # Limpia mensaje tras 5s

    def agregar_producto(self):
        nombre = self.nombre_entry.get()
        try:
            precio = float(self.precio_entry.get())
            stock = int(self.stock_entry.get())
        except ValueError:
            self.mostrar_mensaje("Error: Precio y stock deben ser números.", "red")
            return

        nuevo = Producto(nombre, precio, stock)
        self.productos.append(nuevo)
        self.actualizar_lista()
        self.nombre_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)
        self.mostrar_mensaje(f"Producto '{nombre}' agregado correctamente.", "blue")

    def actualizar_lista(self):
        self.lista_productos.delete(0, tk.END)
        for i, p in enumerate(self.productos):
            self.lista_productos.insert(i, f"{p.nombre} - ${p.precio:.2f} - Stock: {p.stock}")

    def modificar_precio(self):
        seleccion = self.lista_productos.curselection()
        if not seleccion:
            self.mostrar_mensaje("Seleccione un producto para modificar.", "orange")
            return

        index = seleccion[0]
        producto = self.productos[index]

        nuevo_precio = simpledialog.askfloat("Modificar Precio", f"Nuevo precio para {producto.nombre}:")
        if nuevo_precio is not None:
            producto.precio = nuevo_precio
            self.actualizar_lista()
            self.mostrar_mensaje(f"Nuevo precio de {producto.nombre}: ${nuevo_precio:.2f}", "blue")

    def vender_producto(self):
        seleccion = self.lista_productos.curselection()
        if not seleccion:
            self.mostrar_mensaje("Seleccione un producto para vender.", "orange")
            return

        index = seleccion[0]
        producto = self.productos[index]

        cantidad = simpledialog.askinteger("Venta", f"Ingrese cantidad a vender de {producto.nombre}:")
        if cantidad is not None:
            exito, total = producto.realizar_venta(cantidad)
            if exito:
                self.guardar_boleta(producto.nombre, cantidad, producto.precio, total)
                self.actualizar_lista()
                self.mostrar_mensaje(f"Venta realizada. Total: ${total:.2f}", "green")
            else:
                self.mostrar_mensaje(f"Stock insuficiente. Disponible: {producto.stock}", "red")

    def guardar_boleta(self, nombre, cantidad, precio_unitario, total):
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open("boleta.txt", "a") as archivo:
                archivo.write("----- BOLETA DE VENTA -----\n")
                archivo.write(f"Fecha y hora: {fecha_hora}\n")
                archivo.write(f"Producto: {nombre}\n")
                archivo.write(f"Cantidad: {cantidad}\n")
                archivo.write(f"Precio unitario: ${precio_unitario:.2f}\n")
                archivo.write(f"Total: ${total:.2f}\n")
                archivo.write("---------------------------\n\n")
            self.mostrar_mensaje("Boleta guardada en boleta.txt", "blue")
        except Exception as e:
            self.mostrar_mensaje(f"Error al guardar boleta: {e}", "red")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
