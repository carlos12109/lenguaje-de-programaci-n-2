from tkinter import Tk, Label, Button, Entry, StringVar, messagebox
from figuras.circulo import Circulo
from figuras.rectangulo import Rectangulo
from figuras.triangulo import Triangulo

class Interfaz:
    def __init__(self, master):
        self.master = master
        master.title("Figuras Geométricas")
        master.configure(bg="#f0f8ff")

        self.figuras = []

        self.label = Label(master, text="Registrar Figura", bg="#f0f8ff", font=("Arial", 16))
        self.label.pack(pady=10)

        self.figura_var = StringVar()
        self.figura_var.set("Circulo")  # Default value

        self.figura_label = Label(master, text="Selecciona figura:", bg="#f0f8ff")
        self.figura_label.pack()

        self.figura_entry = Entry(master, textvariable=self.figura_var)
        self.figura_entry.pack(pady=5)

        self.radio_label = Label(master, text="Radio (solo para círculo):", bg="#f0f8ff")
        self.radio_label.pack()

        self.radio_entry = Entry(master)
        self.radio_entry.pack(pady=5)

        self.base_label = Label(master, text="Base (solo para rectángulo):", bg="#f0f8ff")
        self.base_label.pack()

        self.base_entry = Entry(master)
        self.base_entry.pack(pady=5)

        self.altura_label = Label(master, text="Altura (solo para rectángulo):", bg="#f0f8ff")
        self.altura_label.pack()

        self.altura_entry = Entry(master)
        self.altura_entry.pack(pady=5)

        self.register_button = Button(master, text="Registrar Figura", command=self.registrar_figura, bg="#add8e6")
        self.register_button.pack(pady=10)

        self.show_button = Button(master, text="Mostrar Figuras", command=self.mostrar_figuras, bg="#add8e6")
        self.show_button.pack(pady=10)

    def registrar_figura(self):
        figura = self.figura_var.get()
        if figura.lower() == "circulo":
            try:
                radio = float(self.radio_entry.get())
                c = Circulo(radio)
                self.figuras.append(c)
                messagebox.showinfo("Éxito", "Círculo registrado.")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un valor numérico para el radio.")
        elif figura.lower() == "rectangulo":
            try:
                base = float(self.base_entry.get())
                altura = float(self.altura_entry.get())
                r = Rectangulo(base, altura)
                self.figuras.append(r)
                messagebox.showinfo("Éxito", "Rectángulo registrado.")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese valores numéricos para la base y altura.")
        elif figura.lower() == "triangulo":
            # Implementar registro de triángulo aquí
            pass
        else:
            messagebox.showerror("Error", "Figura no válida.")

    def mostrar_figuras(self):
        if not self.figuras:
            messagebox.showinfo("Información", "No hay figuras registradas.")
            return
        info = "\n".join([f"{f.get_nombre()}: Área = {f.calcular_area()}, Perímetro = {f.calcular_perimetro()}" for f in self.figuras])
        messagebox.showinfo("Figuras Registradas", info)

if __name__ == "__main__":
    root = Tk()
    interfaz = Interfaz(root)
    root.mainloop()