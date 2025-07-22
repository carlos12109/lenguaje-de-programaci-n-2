from tkinter import Tk, Label, Button, Entry, StringVar, messagebox
from models.felino import Felino
from models.ave import Ave

class SistemaAnimalesGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Registro de Animales")
        master.geometry("400x400")
        
        self.nombre_var = StringVar()
        self.edad_var = StringVar()
        self.especie_var = StringVar()
        self.color_pelaje_var = StringVar()
        self.tipo_pico_var = StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        Label(self.master, text="Nombre:").pack()
        Entry(self.master, textvariable=self.nombre_var).pack()

        Label(self.master, text="Edad:").pack()
        Entry(self.master, textvariable=self.edad_var).pack()

        Label(self.master, text="Especie:").pack()
        Entry(self.master, textvariable=self.especie_var).pack()

        Label(self.master, text="Color de Pelaje (Felino):").pack()
        Entry(self.master, textvariable=self.color_pelaje_var).pack()

        Label(self.master, text="Tipo de Pico (Ave):").pack()
        Entry(self.master, textvariable=self.tipo_pico_var).pack()

        Button(self.master, text="Registrar Felino", command=self.registrar_felino).pack()
        Button(self.master, text="Registrar Ave", command=self.registrar_ave).pack()
        Button(self.master, text="Mostrar Animales", command=self.mostrar_animales).pack()

        self.animales = []

    def registrar_felino(self):
        nombre = self.nombre_var.get()
        edad = self.edad_var.get()
        especie = self.especie_var.get()
        color_pelaje = self.color_pelaje_var.get()

        if nombre and edad and especie and color_pelaje:
            felino = Felino(nombre, edad, especie, color_pelaje)
            self.animales.append(felino)
            messagebox.showinfo("Éxito", "Felino registrado exitosamente.")
            self.clear_entries()
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def registrar_ave(self):
        nombre = self.nombre_var.get()
        edad = self.edad_var.get()
        especie = self.especie_var.get()
        tipo_pico = self.tipo_pico_var.get()

        if nombre and edad and especie and tipo_pico:
            ave = Ave(nombre, edad, especie, tipo_pico)
            self.animales.append(ave)
            messagebox.showinfo("Éxito", "Ave registrada exitosamente.")
            self.clear_entries()
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def mostrar_animales(self):
        if not self.animales:
            messagebox.showinfo("Información", "No hay animales registrados.")
            return
        
        info = "\n".join(animal.mostrar_info() for animal in self.animales)
        messagebox.showinfo("Animales Registrados", info)

    def clear_entries(self):
        self.nombre_var.set("")
        self.edad_var.set("")
        self.especie_var.set("")
        self.color_pelaje_var.set("")
        self.tipo_pico_var.set("")

def main():
    root = Tk()
    app = SistemaAnimalesGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()