from tkinter import Tk, Label, Button, Entry, StringVar, messagebox
from figuras.circulo import Circulo
from figuras.rectangulo import Rectangulo
from figuras.triangulo import Triangulo

class FigurasApp:
    def __init__(self, master):
        self.master = master
        master.title("Registro de Figuras Geométricas")
        master.configure(bg="#f0f8ff")

        self.figuras = []

        self.label = Label(master, text="Seleccione una figura:", bg="#f0f8ff")
        self.label.pack()

        self.figura_var = StringVar(master)
        self.figura_var.set("Circulo")  # valor por defecto

        self.circulo_button = Button(master, text="Circulo", command=self.registrar_circulo, bg="#add8e6")
        self.circulo_button.pack()

        self.rectangulo_button = Button(master, text="Rectangulo", command=self.registrar_rectangulo, bg="#add8e6")
        self.rectangulo_button.pack()

        self.triangulo_button = Button(master, text="Triangulo", command=self.registrar_triangulo, bg="#add8e6")
        self.triangulo_button.pack()

        self.mostrar_button = Button(master, text="Mostrar Figuras", command=self.mostrar_figuras, bg="#90ee90")
        self.mostrar_button.pack()

    def registrar_circulo(self):
        radio = self._input_float("Ingrese el radio del círculo:")
        if radio is not None:
            circulo = Circulo(radio)
            self.figuras.append(circulo)
            messagebox.showinfo("Registro", "Círculo registrado.")

    def registrar_rectangulo(self):
        base = self._input_float("Ingrese la base del rectángulo:")
        altura = self._input_float("Ingrese la altura del rectángulo:")
        if base is not None and altura is not None:
            rectangulo = Rectangulo(base, altura)
            self.figuras.append(rectangulo)
            messagebox.showinfo("Registro", "Rectángulo registrado.")

    def registrar_triangulo(self):
        base = self._input_float("Ingrese la base del triángulo:")
        altura = self._input_float("Ingrese la altura del triángulo:")
        if base is not None and altura is not None:
            triangulo = Triangulo(base, altura)
            self.figuras.append(triangulo)
            messagebox.showinfo("Registro", "Triángulo registrado.")

    def mostrar_figuras(self):
        if not self.figuras:
            messagebox.showinfo("Mostrar Figuras", "No hay figuras registradas.")
            return
        info = "\n".join([f"{figura.get_nombre()}: Área = {figura.calcular_area()}, Perímetro = {figura.calcular_perimetro()}" for figura in self.figuras])
        messagebox.showinfo("Figuras Registradas", info)

    def _input_float(self, message):
        input_value = simpledialog.askstring("Input", message)
        try:
            return float(input_value)
        except (ValueError, TypeError):
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")
            return None

if __name__ == "__main__":
    root = Tk()
    app = FigurasApp(root)
    root.mainloop()