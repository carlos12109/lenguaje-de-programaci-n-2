import tkinter as tk
from tkinter import ttk
import csv
from datetime import datetime, timedelta

# === CLASES Y LÓGICA ===

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
    def __init__(self, nombre, dni, libro, fecha_reserva, fecha_entrega):
        super().__init__(nombre, dni)
        self.__libro = libro
        self.__fecha_reserva = fecha_reserva
        self.__fecha_entrega = fecha_entrega

    def get_libro(self): return self.__libro
    def get_fecha_reserva(self): return self.__fecha_reserva
    def get_fecha_entrega(self): return self.__fecha_entrega

class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__reservas = []

    def registrar_libro(self, titulo, autor, codigo):
        libro = Libro(titulo, autor, codigo)
        self.__libros.append(libro)
        self.exportar_datos()

    def hacer_reserva(self, nombre_usuario, codigo, dni):
        libro = next((l for l in self.__libros if l.get_codigo() == codigo and l.esta_disponible()), None)
        if libro:
            libro.reservar()
            fecha_reserva = datetime.now()
            fecha_entrega = fecha_reserva + timedelta(days=7)
            reserva = Reserva(nombre_usuario, dni, libro, fecha_reserva, fecha_entrega)
            self.__reservas.append(reserva)
            self.exportar_datos()
            return reserva
        return None

    def cancelar_reserva(self, codigo, dni):
        reserva = next((r for r in self.__reservas if r.get_libro().get_codigo() == codigo and r.get_dni() == dni), None)
        if reserva:
            reserva.get_libro().liberar()
            self.__reservas.remove(reserva)
            self.exportar_datos()
            return True
        return False

    def get_libros_disponibles(self):
        return [libro for libro in self.__libros if libro.esta_disponible()]

    def get_reservas(self):
        return self.__reservas

    def exportar_datos(self):
        self.exportar_txt()
        self.exportar_csv()

    def exportar_txt(self, nombre_archivo="libros.txt"):
        with open(nombre_archivo, "w") as f:
            f.write("Listado de Libros:\n")
            for libro in self.__libros:
                estado = "Disponible" if libro.esta_disponible() else "Reservado"
                f.write(f"{libro.get_titulo()} - {libro.get_autor()} - Código: {libro.get_codigo()} - {estado}\n")

    def exportar_csv(self, nombre_archivo="libros.csv"):
        with open(nombre_archivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Título", "Autor", "Código", "Estado"])
            for libro in self.__libros:
                estado = "Disponible" if libro.esta_disponible() else "Reservado"
                writer.writerow([libro.get_titulo(), libro.get_autor(), libro.get_codigo(), estado])

# === INTERFAZ GRÁFICA ===

# ... (el resto de tus imports y clases permanece igual)

class BibliotecaGUI:
    def __init__(self, root):
        self.biblioteca = Biblioteca()
        self.root = root
        self.root.title("Biblioteca Universitaria")
        self.root.geometry("950x700")  # AJUSTADO

        # Colores y fuentes
        self.color_primario = "#2c3e50"
        self.color_secundario = "#2980b9"
        self.color_fondo = "#f0f4f8"
        self.color_boton = "#3498db"
        self.color_texto = "#ffffff"

        self.font_titulo = ("Arial", 15, "bold")
        self.font_label = ("Arial", 11)
        self.font_texto = ("Arial", 11)

        # Frames
        self.frame_registrar = tk.LabelFrame(root, text="Registrar Libro", bg=self.color_fondo, fg=self.color_primario, font=self.font_titulo)
        self.frame_registrar.place(x=20, y=20, width=350, height=180)

        self.frame_reservar = tk.LabelFrame(root, text="Hacer Reserva", bg=self.color_fondo, fg=self.color_primario, font=self.font_titulo)
        self.frame_reservar.place(x=20, y=220, width=350, height=200)  # AJUSTADO

        self.frame_cancelar = tk.LabelFrame(root, text="Cancelar Reserva", bg=self.color_fondo, fg=self.color_primario, font=self.font_titulo)
        self.frame_cancelar.place(x=20, y=440, width=350, height=160)  # AJUSTADO

        self.frame_listados = tk.LabelFrame(root, text="Libros y Reservas", bg=self.color_fondo, fg=self.color_primario, font=self.font_titulo)
        self.frame_listados.place(x=400, y=20, width=530, height=630)  # AJUSTADO

        # Registrar Libro
        tk.Label(self.frame_registrar, text="Título:", bg=self.color_fondo, fg=self.color_primario, font=self.font_label).place(x=10, y=10)
        self.entry_titulo = tk.Entry(self.frame_registrar, font=self.font_texto)
        self.entry_titulo.place(x=100, y=10, width=220)

        tk.Label(self.frame_registrar, text="Autor:", bg=self.color_fondo, fg=self.color_primario, font=self.font_label).place(x=10, y=50)
        self.entry_autor = tk.Entry(self.frame_registrar, font=self.font_texto)
        self.entry_autor.place(x=100, y=50, width=220)

        tk.Label(self.frame_registrar, text="Código:", bg=self.color_fondo, fg=self.color_primario, font=self.font_label).place(x=10, y=90)
        self.entry_codigo = tk.Entry(self.frame_registrar, font=self.font_texto)
        self.entry_codigo.place(x=100, y=90, width=220)

        self.lbl_msg_registrar = tk.Label(self.frame_registrar, text="", bg=self.color_fondo, fg="green", font=self.font_label)
        self.lbl_msg_registrar.place(x=10, y=125)

        btn_registrar = tk.Button(self.frame_registrar, text="Registrar", bg=self.color_boton, fg=self.color_texto, font=self.font_label, command=self.registrar_libro)
        btn_registrar.place(x=250, y=115, width=70)

        # Hacer Reserva
        tk.Label(self.frame_reservar, text="Nombre y Apellido:", bg=self.color_fondo, fg=self.color_primario, font=self.font_label).place(x=10, y=10)
        self.entry_nombre_reserva = tk.Entry(self.frame_reservar, font=self.font_texto)
        self.entry_nombre_reserva.place(x=150, y=10, width=180)

        tk.Label(self.frame_reservar, text="DNI:", bg=self.color_fondo, fg=self.color_primario, font=self.font_label).place(x=10, y=50)
        self.entry_dni_reserva = tk.Entry(self.frame_reservar, font=self.font_texto)
        self.entry_dni_reserva.place(x=150, y=50, width=180)

        tk.Label(self.frame_reservar, text="Código de Libro:", bg=self.color_fondo, fg=self.color_primario, font=self.font_label).place(x=10, y=90)
        self.entry_codigo_reserva = tk.Entry(self.frame_reservar, font=self.font_texto)
        self.entry_codigo_reserva.place(x=150, y=90, width=180)

        self.lbl_msg_reserva = tk.Label(self.frame_reservar, text="", bg=self.color_fondo, fg="green", font=self.font_label)
        self.lbl_msg_reserva.place(x=10, y=130)  # AJUSTADO

        btn_reservar = tk.Button(self.frame_reservar, text="Reservar", bg=self.color_boton, fg=self.color_texto, font=self.font_label, command=self.hacer_reserva)
        btn_reservar.place(x=260, y=120, width=70)  # AJUSTADO

        # Cancelar Reserva
        tk.Label(self.frame_cancelar, text="Código Libro:", bg=self.color_fondo, fg=self.color_primario, font=self.font_label).place(x=10, y=10)
        self.entry_codigo_cancelar = tk.Entry(self.frame_cancelar, font=self.font_texto)
        self.entry_codigo_cancelar.place(x=130, y=10, width=200)

        tk.Label(self.frame_cancelar, text="DNI:", bg=self.color_fondo, fg=self.color_primario, font=self.font_label).place(x=10, y=50)
        self.entry_dni_cancelar = tk.Entry(self.frame_cancelar, font=self.font_texto)
        self.entry_dni_cancelar.place(x=130, y=50, width=200)

        self.lbl_msg_cancelar = tk.Label(self.frame_cancelar, text="", bg=self.color_fondo, fg="red", font=self.font_label)
        self.lbl_msg_cancelar.place(x=10, y=80)  # AJUSTADO

        btn_cancelar = tk.Button(self.frame_cancelar, text="Cancelar", bg="#e74c3c", fg=self.color_texto, font=self.font_label, command=self.cancelar_reserva)
        btn_cancelar.place(x=260, y=80, width=70)  # AJUSTADO

        # Listados
        self.tree_libros = ttk.Treeview(self.frame_listados, columns=("Autor", "Código", "Estado"), show="headings")
        self.tree_libros.heading("Autor", text="Autor")
        self.tree_libros.heading("Código", text="Código")
        self.tree_libros.heading("Estado", text="Estado")
        self.tree_libros.column("Autor", width=120)
        self.tree_libros.column("Código", width=60, anchor="center")
        self.tree_libros.column("Estado", width=80, anchor="center")
        self.tree_libros.place(x=10, y=10, width=500, height=250)

        tk.Label(self.frame_listados, text="Libros Registrados", bg=self.color_fondo, fg=self.color_primario, font=self.font_label).place(x=10, y=260)

        self.tree_reservas = ttk.Treeview(self.frame_listados, columns=("Nombre", "DNI", "Reserva", "Entrega"), show="headings")
        self.tree_reservas.heading("Nombre", text="Nombre")
        self.tree_reservas.heading("DNI", text="DNI")
        self.tree_reservas.heading("Reserva", text="Fecha Reserva")
        self.tree_reservas.heading("Entrega", text="Fecha Entrega")
        self.tree_reservas.column("Nombre", width=90)
        self.tree_reservas.column("DNI", width=60, anchor="center")
        self.tree_reservas.column("Reserva", width=75, anchor="center")
        self.tree_reservas.column("Entrega", width=75, anchor="center")
        self.tree_reservas.place(x=10, y=300, width=500, height=250)

        tk.Label(self.frame_listados, text="Reservas Activas", bg=self.color_fondo, fg=self.color_primario, font=self.font_label).place(x=10, y=550)

        self.actualizar_listados()

    def registrar_libro(self):
        titulo = self.entry_titulo.get().strip()
        autor = self.entry_autor.get().strip()
        codigo = self.entry_codigo.get().strip()

        if not titulo or not autor or not codigo:
            self.lbl_msg_registrar.config(text="Complete todos los campos.", fg="red")
            return

        # Verificar código único
        for libro in self.biblioteca._Biblioteca__libros:
            if libro.get_codigo() == codigo:
                self.lbl_msg_registrar.config(text="Código ya registrado.", fg="red")
                return

        self.biblioteca.registrar_libro(titulo, autor, codigo)
        self.lbl_msg_registrar.config(text="Libro registrado con éxito.", fg="green")

        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_codigo.delete(0, tk.END)

        self.actualizar_listados()

    def hacer_reserva(self):
        nombre = self.entry_nombre_reserva.get().strip()
        dni = self.entry_dni_reserva.get().strip()
        codigo = self.entry_codigo_reserva.get().strip()

        if not nombre or not dni or not codigo:
            self.lbl_msg_reserva.config(text="Complete todos los campos.", fg="red")
            return

        reserva = self.biblioteca.hacer_reserva(nombre, codigo, dni)
        if reserva:
            fecha_res = reserva.get_fecha_reserva().strftime("%d/%m/%Y %H:%M")
            fecha_ent = reserva.get_fecha_entrega().strftime("%d/%m/%Y")
            self.lbl_msg_reserva.config(text=f"Reservado. Entrega: {fecha_ent}", fg="green")

            self.entry_nombre_reserva.delete(0, tk.END)
            self.entry_dni_reserva.delete(0, tk.END)
            self.entry_codigo_reserva.delete(0, tk.END)
            self.actualizar_listados()
        else:
            self.lbl_msg_reserva.config(text="Libro no disponible o no encontrado.", fg="red")

    def cancelar_reserva(self):
        codigo = self.entry_codigo_cancelar.get().strip()
        dni = self.entry_dni_cancelar.get().strip()

        if not codigo or not dni:
            self.lbl_msg_cancelar.config(text="Complete todos los campos.", fg="red")
            return

        exito = self.biblioteca.cancelar_reserva(codigo, dni)
        if exito:
            self.lbl_msg_cancelar.config(text="Reserva cancelada con éxito.", fg="green")
            self.entry_codigo_cancelar.delete(0, tk.END)
            self.entry_dni_cancelar.delete(0, tk.END)
            self.actualizar_listados()
        else:
            self.lbl_msg_cancelar.config(text="Reserva no encontrada.", fg="red")

    def actualizar_listados(self):
        # Limpiar tablas
        for i in self.tree_libros.get_children():
            self.tree_libros.delete(i)
        for i in self.tree_reservas.get_children():
            self.tree_reservas.delete(i)

        # Mostrar libros
        for libro in self.biblioteca._Biblioteca__libros:
            estado = "Disponible" if libro.esta_disponible() else "Reservado"
            self.tree_libros.insert("", "end", values=(libro.get_autor(), libro.get_codigo(), estado))

        # Mostrar reservas
        for reserva in self.biblioteca.get_reservas():
            self.tree_reservas.insert("", "end", values=(
                reserva.get_nombre(),
                reserva.get_dni(),
                reserva.get_fecha_reserva().strftime("%d/%m/%Y %H:%M"),
                reserva.get_fecha_entrega().strftime("%d/%m/%Y"),
            ))

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaGUI(root)
    root.mainloop()
