"""
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

    #def actualizar precio
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        print("\nEl precio del producto ha sido actualizado a: ")


    def actualizar_stock(self, nuevo_stock):
        self.stock = nuevo_stock
        print("stock actualizado correctamente: ", self.stock)
        
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
producto1.actualizar_precio(4)
producto1.actualizar_stock(110)

producto1.mostrar_informacion()
"""
import tkinter as tk
from tkinter import messagebox

# Clase Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def actualizar_stock(self, nuevo_stock):
        self.stock = nuevo_stock

# Lista inicial de productos
productos = [
    Producto("Arroz", 3.50, 100),
    Producto("Azúcar", 4.50, 50),
    Producto("Aceite", 8.00, 80),
    Producto("Leche", 4.50, 60)
]

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("📦 Gestión de Productos")
        self.master.geometry("550x600")
        self.master.configure(bg="#f2f2f2")

        self.titulo = tk.Label(master, text="🛒 Gestión de Productos", font=("Helvetica", 18, "bold"), bg="#f2f2f2", fg="#333")
        self.titulo.pack(pady=15)

        self.lista_productos = tk.Listbox(master, font=("Helvetica", 12), width=40, height=6, bg="#ffffff", bd=2, relief="groove", cursor="hand2")
        self.lista_productos.pack(pady=10)
        self.lista_productos.bind("<<ListboxSelect>>", self.mostrar_info_producto)

        self.frame_info = tk.Frame(master, bg="white", bd=2, relief="groove")
        self.frame_info.pack(pady=10)
        self.info = tk.Label(self.frame_info, text="Selecciona un producto", font=("Helvetica", 12), bg="white", justify="left", padx=10, pady=10)
        self.info.pack()

        # Frame para entradas
        self.entry_frame = tk.Frame(master, bg="#f2f2f2")
        self.entry_frame.pack(pady=5)

        self.precio_label = tk.Label(self.entry_frame, text="💲 Precio:", font=("Helvetica", 10), bg="#f2f2f2")
        self.precio_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.precio_entry = tk.Entry(self.entry_frame)
        self.precio_entry.grid(row=0, column=1, padx=5, pady=5)

        self.stock_label = tk.Label(self.entry_frame, text="📦 Stock:", font=("Helvetica", 10), bg="#f2f2f2")
        self.stock_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.stock_entry = tk.Entry(self.entry_frame)
        self.stock_entry.grid(row=1, column=1, padx=5, pady=5)

        # Botones principales
        self.boton_actualizar = tk.Button(master, text="✅ Actualizar", command=self.actualizar_producto,
                                          bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), width=20)
        self.boton_actualizar.pack(pady=5)

        self.boton_eliminar = tk.Button(master, text="🗑️ Eliminar Producto", command=self.eliminar_producto,
                                        bg="#f44336", fg="white", font=("Helvetica", 12, "bold"), width=20)
        self.boton_eliminar.pack(pady=5)

        self.boton_agregar = tk.Button(master, text="➕ Agregar Nuevo Producto", command=self.ventana_agregar,
                                       bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"), width=25)
        self.boton_agregar.pack(pady=10)

        self.cargar_lista()

    def cargar_lista(self):
        self.lista_productos.delete(0, tk.END)
        for p in productos:
            self.lista_productos.insert(tk.END, f"{p.nombre}")

    def mostrar_info_producto(self, event):
        seleccion = self.lista_productos.curselection()
        if seleccion:
            index = seleccion[0]
            p = productos[index]
            self.info.config(text=f"🛍️ Nombre: {p.nombre}\n💲 Precio: ${p.precio:.2f}\n📦 Stock: {p.stock} unidades")
            self.precio_entry.delete(0, tk.END)
            self.stock_entry.delete(0, tk.END)
            self.precio_entry.insert(0, str(p.precio))
            self.stock_entry.insert(0, str(p.stock))

    def actualizar_producto(self):
        seleccion = self.lista_productos.curselection()
        if not seleccion:
            messagebox.showwarning("⚠️", "Selecciona un producto para actualizar.")
            return

        index = seleccion[0]
        try:
            nuevo_precio = float(self.precio_entry.get())
            nuevo_stock = int(self.stock_entry.get())
        except ValueError:
            messagebox.showerror("❌", "Precio o stock inválido.")
            return

        producto = productos[index]
        producto.actualizar_precio(nuevo_precio)
        producto.actualizar_stock(nuevo_stock)
        self.mostrar_info_producto(None)
        messagebox.showinfo("✅", "Producto actualizado correctamente.")

    def eliminar_producto(self):
        seleccion = self.lista_productos.curselection()
        if not seleccion:
            messagebox.showwarning("⚠️", "Selecciona un producto para eliminar.")
            return

        index = seleccion[0]
        producto = productos.pop(index)
        self.cargar_lista()
        self.info.config(text="Selecciona un producto")
        messagebox.showinfo("🗑️", f"{producto.nombre} eliminado correctamente.")

    def ventana_agregar(self):
        ventana = tk.Toplevel(self.master)
        ventana.title("➕ Agregar Producto")
        ventana.geometry("300x250")
        ventana.configure(bg="#f2f2f2")

        tk.Label(ventana, text="Nombre:", font=("Helvetica", 10), bg="#f2f2f2").pack(pady=5)
        nombre_entry = tk.Entry(ventana)
        nombre_entry.pack(pady=5)

        tk.Label(ventana, text="Precio:", font=("Helvetica", 10), bg="#f2f2f2").pack(pady=5)
        precio_entry = tk.Entry(ventana)
        precio_entry.pack(pady=5)

        tk.Label(ventana, text="Stock:", font=("Helvetica", 10), bg="#f2f2f2").pack(pady=5)
        stock_entry = tk.Entry(ventana)
        stock_entry.pack(pady=5)

        def agregar():
            nombre = nombre_entry.get().strip()
            try:
                precio = float(precio_entry.get())
                stock = int(stock_entry.get())
            except ValueError:
                messagebox.showerror("❌", "Datos inválidos")
                return

            if not nombre:
                messagebox.showwarning("⚠️", "El nombre no puede estar vacío")
                return

            productos.append(Producto(nombre, precio, stock))
            self.cargar_lista()
            messagebox.showinfo("✅", f"Producto '{nombre}' agregado correctamente")
            ventana.destroy()

        tk.Button(ventana, text="Agregar", command=agregar, bg="#2196F3", fg="white", font=("Helvetica", 11, "bold")).pack(pady=15)

# Ejecutar app
ventana = tk.Tk()
app = App(ventana)
ventana.mainloop()
