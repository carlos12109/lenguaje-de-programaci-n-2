from tkinter import Tk, Frame, Label, Button, Entry, StringVar, messagebox
from models.felino import Felino
from models.ave import Ave

class AnimalRegistrationApp:
    def __init__(self, master):
        self.master = master
        master.title("Registro de Animales")
        master.geometry("400x400")
        master.configure(bg="#f0f8ff")

        self.title_label = Label(master, text="Registro de Animales", font=("Helvetica", 16), bg="#f0f8ff")
        self.title_label.pack(pady=10)

        self.animal_type = StringVar()
        self.animal_type.set("felino")

        self.felino_frame = Frame(master, bg="#f0f8ff")
        self.ave_frame = Frame(master, bg="#f0f8ff")

        self.create_felino_widgets()
        self.create_ave_widgets()

        self.felino_frame.pack(pady=10)

        self.switch_button = Button(master, text="Registrar Ave", command=self.toggle_frames, bg="#add8e6")
        self.switch_button.pack(pady=5)

        self.register_button = Button(master, text="Registrar", command=self.register_animal, bg="#90ee90")
        self.register_button.pack(pady=5)

    def create_felino_widgets(self):
        Label(self.felino_frame, text="Nombre:", bg="#f0f8ff").grid(row=0, column=0)
        self.felino_name = Entry(self.felino_frame)
        self.felino_name.grid(row=0, column=1)

        Label(self.felino_frame, text="Edad:", bg="#f0f8ff").grid(row=1, column=0)
        self.felino_age = Entry(self.felino_frame)
        self.felino_age.grid(row=1, column=1)

        Label(self.felino_frame, text="Especie:", bg="#f0f8ff").grid(row=2, column=0)
        self.felino_species = Entry(self.felino_frame)
        self.felino_species.grid(row=2, column=1)

        Label(self.felino_frame, text="Color de Pelaje:", bg="#f0f8ff").grid(row=3, column=0)
        self.felino_color = Entry(self.felino_frame)
        self.felino_color.grid(row=3, column=1)

    def create_ave_widgets(self):
        Label(self.ave_frame, text="Nombre:", bg="#f0f8ff").grid(row=0, column=0)
        self.ave_name = Entry(self.ave_frame)
        self.ave_name.grid(row=0, column=1)

        Label(self.ave_frame, text="Edad:", bg="#f0f8ff").grid(row=1, column=0)
        self.ave_age = Entry(self.ave_frame)
        self.ave_age.grid(row=1, column=1)

        Label(self.ave_frame, text="Especie:", bg="#f0f8ff").grid(row=2, column=0)
        self.ave_species = Entry(self.ave_frame)
        self.ave_species.grid(row=2, column=1)

        Label(self.ave_frame, text="Tipo de Pico:", bg="#f0f8ff").grid(row=3, column=0)
        self.ave_beak_type = Entry(self.ave_frame)
        self.ave_beak_type.grid(row=3, column=1)

    def toggle_frames(self):
        if self.felino_frame.winfo_ismapped():
            self.felino_frame.pack_forget()
            self.ave_frame.pack(pady=10)
            self.switch_button.config(text="Registrar Felino")
        else:
            self.ave_frame.pack_forget()
            self.felino_frame.pack(pady=10)
            self.switch_button.config(text="Registrar Ave")

    def register_animal(self):
        if self.felino_frame.winfo_ismapped():
            name = self.felino_name.get()
            age = self.felino_age.get()
            species = self.felino_species.get()
            color = self.felino_color.get()
            animal = Felino(name, age, species, color)
        else:
            name = self.ave_name.get()
            age = self.ave_age.get()
            species = self.ave_species.get()
            beak_type = self.ave_beak_type.get()
            animal = Ave(name, age, species, beak_type)

        # Here you would typically save the animal to a list or database
        messagebox.showinfo("Registro Exitoso", f"{animal.get_nombre()} registrado exitosamente.")

def main():
    root = Tk()
    app = AnimalRegistrationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()