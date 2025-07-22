import tkinter as tk
from tkinter import ttk

class Rectangulo:
    def __init__(self, base, altura, color):
        self.base = base
        self.altura = altura
        self.color = color

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def mostrar_info(self):
        return (f"Color: {self.color}, Base: {self.base}, Altura: {self.altura}\n"
                f"Área: {self.area():.2f}, Perímetro: {self.perimetro():.2f}")

def calcular_y_dibujar():
    try:
        # Leer entradas
        base1 = float(entry_base1.get())
        altura1 = float(entry_altura1.get())
        color1 = entry_color1.get()

        base2 = float(entry_base2.get())
        altura2 = float(entry_altura2.get())
        color2 = entry_color2.get()

        rect1 = Rectangulo(base1, altura1, color1)
        rect2 = Rectangulo(base2, altura2, color2)

        # Mostrar resultados
        resultado_texto.set(
            f"--- Rectángulo 1 ---\n{rect1.mostrar_info()}\n\n"
            f"--- Rectángulo 2 ---\n{rect2.mostrar_info()}"
        )

        # Limpiar canvas
        canvas.delete("all")

        # Escalar dimensiones para que quepan en el canvas
        escala = 5
        x_offset = 50
        y_offset = 20

        # Rectángulo 1
        canvas.create_rectangle(
            x_offset, y_offset,
            x_offset + rect1.base * escala, y_offset + rect1.altura * escala,
            fill=rect1.color, outline="black"
        )
        canvas.create_text(x_offset + rect1.base * escala / 2, y_offset + rect1.altura * escala + 10,
                           text="Rectángulo 1", font=("Arial", 10))

        # Rectángulo 2 (al lado)
        x2 = x_offset + rect1.base * escala + 60
        canvas.create_rectangle(
            x2, y_offset,
            x2 + rect2.base * escala, y_offset + rect2.altura * escala,
            fill=rect2.color, outline="black"
        )
        canvas.create_text(x2 + rect2.base * escala / 2, y_offset + rect2.altura * escala + 10,
                           text="Rectángulo 2", font=("Arial", 10))

    except ValueError:
        resultado_texto.set("❌ Por favor, ingrese valores numéricos válidos en base y altura.")

# Crear ventana
root = tk.Tk()
root.title("Rectángulos con Colores y Gráfica")
root.geometry("600x500")
root.configure(bg="#f4f4f4")

# Marco de entrada
frame = ttk.Frame(root, padding=10)
frame.pack()

# Inputs para Rectángulo 1
ttk.Label(frame, text="Rectángulo 1").grid(row=0, column=0, columnspan=2)
ttk.Label(frame, text="Base:").grid(row=1, column=0)
entry_base1 = ttk.Entry(frame)
entry_base1.grid(row=1, column=1)

ttk.Label(frame, text="Altura:").grid(row=2, column=0)
entry_altura1 = ttk.Entry(frame)
entry_altura1.grid(row=2, column=1)

ttk.Label(frame, text="Color (nombre o #hex):").grid(row=3, column=0)
entry_color1 = ttk.Entry(frame)
entry_color1.grid(row=3, column=1)

# Inputs para Rectángulo 2
ttk.Label(frame, text="Rectángulo 2").grid(row=4, column=0, columnspan=2, pady=(10, 0))
ttk.Label(frame, text="Base:").grid(row=5, column=0)
entry_base2 = ttk.Entry(frame)
entry_base2.grid(row=5, column=1)

ttk.Label(frame, text="Altura:").grid(row=6, column=0)
entry_altura2 = ttk.Entry(frame)
entry_altura2.grid(row=6, column=1)

ttk.Label(frame, text="Color (nombre o #hex):").grid(row=7, column=0)
entry_color2 = ttk.Entry(frame)
entry_color2.grid(row=7, column=1)

# Botón
ttk.Button(frame, text="Mostrar Resultados y Dibujar", command=calcular_y_dibujar).grid(row=8, column=0, columnspan=2, pady=10)

# Área de resultados
resultado_texto = tk.StringVar()
tk.Label(root, textvariable=resultado_texto, bg="#f4f4f4", font=("Arial", 10), justify="left").pack(pady=5)

# Canvas para dibujo
canvas = tk.Canvas(root, width=560, height=200, bg="white", relief="solid", bd=1)
canvas.pack(pady=10)

root.mainloop()
