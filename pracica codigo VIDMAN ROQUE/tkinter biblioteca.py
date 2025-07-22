import tkinter as tk
from tkinter import ttk
import csv
from datetime import datetime, timedelta

# ======== LÓGICA DE CLASES ==========

class Persona:
    def __init__(self, nombre, dni):
        self.__nombre = nombre
        self.__dni = dni
    def get_nombre(self): return self.__nombre
    def get_dni(self): return self.__dni

class Libro:
    def __init__(self, titulo, autor, codigo):
        self.__titulo = titulo
        self.__autor = autor
        self.__codigo = codigo
        self.__disponible = True
    def get_titulo(self): return self.__titulo
    def get_autor(self): return self.__autor
    def get_codigo(self): return self.__codigo
    def esta_disponible(self): return self.__disponible
    def reservar(self): self.__disponible = False
    def liberar(self): self.__disponible = True

class Reserva(Persona):
    def __init__(self, nombre, dni, libro):
        super().__init__(nombre, dni)
        self.__libro = libro
        self.__fecha_prestamo = datetime.now()
        self.__fecha_devolucion = self.__fecha_prestamo + timedelta(days=14)
    def get_libro(self): return self.__libro
    def get_fecha_prestamo(self): return self.__fecha_prestamo
    def get_fecha_devolucion(self): return self.__fecha_devolucion

class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__reservas = []
    def registrar_libro(self, titulo, autor, codigo):
        self.__libros.append(Libro(titulo, autor, codigo))
        self.exportar_datos()
    def hacer_reserva(self, nombre, codigo, dni):
        libro = next((l for l in self.__libros if l.get_codigo() == codigo and l.esta_disponible()), None)
        if libro:
            libro.reservar()
            self.__reservas.append(Reserva(nombre, dni, libro))
            self.exportar_datos()
            return True
        return False
    def obtener_libros_disponibles(self):
        return [libro for libro in self.__libros if libro.esta_disponible()]
    def obtener_reservas(self):
        return self.__reservas
    def exportar_datos(self):
        with open("libros.txt", "w") as f:
            for libro in self.__libros:
                estado = "Disponible" if libro.esta_disponible() else "Reservado"
                f.write(f"{libro.get_titulo()} - {libro.get_autor()} - Código: {libro.get_codigo()} - {estado}\n")
        with open("libros.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Título", "Autor", "Código", "Estado"])
            for libro in self.__libros:
                estado = "Disponible" if libro.esta_disponible() else "Reservado"
                writer.writerow([libro.get_titulo(), libro.get_autor(), libro.get_codigo(), estado])

# ========== INTERFAZ GRÁFICA MODERNA ==========
class InterfazBiblioteca:
    def __init__(self, root):
        self.root = root
        self.root.title("📘 Biblioteca Moderna")
        self.root.geometry("720x540")
        self.root.configure(bg="#f0f4f8")

        self.biblioteca = Biblioteca()

        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook.Tab', font=('Segoe UI', 12), padding=[10, 5])
        style.configure('TLabel', font=('Segoe UI', 11))
        style.configure('TButton', font=('Segoe UI', 10, 'bold'), background='#007acc', foreground='white')
        style.map('TButton', background=[('active', '#005f99')])

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(padx=20, pady=10, fill="both", expand=True)

        self.tabs = {}
        for name in ["Registrar Libro", "Reservar Libro", "Libros Disponibles", "Libros Reservados"]:
            tab = ttk.Frame(self.notebook)
            self.notebook.add(tab, text=name)
            self.tabs[name] = tab

        self.config_tab_registrar()
        self.config_tab_reservar()
        self.config_tab_disponibles()
        self.config_tab_reservados()

        ttk.Button(root, text="Salir", command=self.root.quit).pack(pady=10)

    def entrada(self, parent, texto):
        ttk.Label(parent, text=texto).pack(pady=5)
        entry = ttk.Entry(parent, width=40)
        entry.pack(pady=2)
        return entry

    def mostrar_mensaje(self, parent, texto, color="green"):
        if hasattr(self, 'label_mensaje'):
            self.label_mensaje.destroy()
        self.label_mensaje = ttk.Label(parent, text=texto, foreground=color, font=('Segoe UI', 10, 'italic'))
        self.label_mensaje.pack(pady=5)

    def config_tab_registrar(self):
        frame = self.tabs["Registrar Libro"]
        self.entry_titulo = self.entrada(frame, "Título del libro:")
        self.entry_autor = self.entrada(frame, "Autor:")
        self.entry_codigo = self.entrada(frame, "Código:")
        ttk.Button(frame, text="Registrar Libro", command=self.registrar_libro).pack(pady=15)

    def config_tab_reservar(self):
        frame = self.tabs["Reservar Libro"]
        self.entry_nombre = self.entrada(frame, "Nombre del usuario:")
        self.entry_dni = self.entrada(frame, "DNI:")
        self.entry_codigo_reserva = self.entrada(frame, "Código del libro:")
        ttk.Button(frame, text="Reservar", command=self.reservar_libro).pack(pady=15)

    def config_tab_disponibles(self):
        frame = self.tabs["Libros Disponibles"]
        self.text_disponibles = tk.Text(frame, width=80, height=20, font=("Courier New", 10))
        self.text_disponibles.pack(pady=10)
        ttk.Button(frame, text="Actualizar Lista", command=self.mostrar_disponibles).pack()

    def config_tab_reservados(self):
        frame = self.tabs["Libros Reservados"]
        self.text_reservados = tk.Text(frame, width=80, height=20, font=("Courier New", 10))
        self.text_reservados.pack(pady=10)
        ttk.Button(frame, text="Actualizar Lista", command=self.mostrar_reservados).pack()

    def registrar_libro(self):
        t, a, c = self.entry_titulo.get(), self.entry_autor.get(), self.entry_codigo.get()
        frame = self.tabs["Registrar Libro"]
        if t and a and c:
            self.biblioteca.registrar_libro(t, a, c)
            self.mostrar_mensaje(frame, "📘 Libro registrado con éxito.", "green")
            self.entry_titulo.delete(0, tk.END)
            self.entry_autor.delete(0, tk.END)
            self.entry_codigo.delete(0, tk.END)
        else:
            self.mostrar_mensaje(frame, "⚠️ Por favor, llena todos los campos.", "red")

    def reservar_libro(self):
        n, d, c = self.entry_nombre.get(), self.entry_dni.get(), self.entry_codigo_reserva.get()
        frame = self.tabs["Reservar Libro"]
        if n and d and c:
            exito = self.biblioteca.hacer_reserva(n, c, d)
            if exito:
                self.mostrar_mensaje(frame, "✅ Reserva realizada con éxito.", "green")
                self.entry_nombre.delete(0, tk.END)
                self.entry_dni.delete(0, tk.END)
                self.entry_codigo_reserva.delete(0, tk.END)
            else:
                self.mostrar_mensaje(frame, "❌ Libro no disponible o no encontrado.", "red")
        else:
            self.mostrar_mensaje(frame, "⚠️ Por favor, llena todos los campos.", "red")

    def mostrar_disponibles(self):
        self.text_disponibles.delete("1.0", tk.END)
        libros = self.biblioteca.obtener_libros_disponibles()
        if libros:
            for l in libros:
                self.text_disponibles.insert(tk.END, f"{l.get_titulo():<30} | {l.get_autor():<20} | Código: {l.get_codigo()}\n")
        else:
            self.text_disponibles.insert(tk.END, "No hay libros disponibles.\n")

    def mostrar_reservados(self):
        self.text_reservados.delete("1.0", tk.END)
        reservas = self.biblioteca.obtener_reservas()
        if reservas:
            for r in reservas:
                l = r.get_libro()
                fecha_prestamo = r.get_fecha_prestamo().strftime("%d/%m/%Y")
                fecha_devolucion = r.get_fecha_devolucion().strftime("%d/%m/%Y")
                self.text_reservados.insert(
                    tk.END,
                    f"{l.get_titulo():<30} | Usuario: {r.get_nombre():<20} | DNI: {r.get_dni():<10} | Código: {l.get_codigo():<10} | "
                    f"Préstamo: {fecha_prestamo} | Devolución: {fecha_devolucion}\n"
                )
        else:
            self.text_reservados.insert(tk.END, "No hay libros reservados.\n")

# ========== INICIO ==========
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazBiblioteca(root)
    root.mainloop()
