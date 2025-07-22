import tkinter as tk
from tkinter import messagebox, ttk

# Clase del doctor
class Doctor:
    def __init__(self, nombre, especialidad, experiencia):
        self.nombre = nombre
        self.especialidad = especialidad
        self.experiencia = experiencia
        self.pacientes_atendidos = []
    
    def mostrar_informacion(self):
        return (
            f"👨‍⚕️ Nombre del doctor: {self.nombre}\n"
            f"🩺 Especialidad: {self.especialidad}\n"
            f"📅 Años de experiencia: {self.experiencia}"
        )
    
    def atender_paciente(self, paciente):
        self.pacientes_atendidos.append(paciente)
        return f"🧑‍⚕️ El doctor {self.nombre} está atendiendo al paciente {paciente}."
    
    def calcular_salario(self):
        salario_base = 2000
        bono_experiencia = self.experiencia * 150
        salario_total = salario_base + bono_experiencia
        return f"💰 El salario mensual del Dr. {self.nombre} es ${salario_total}"
    
    def recetar_medicamento(self, medicamento):
        return f"💊 El doctor {self.nombre} receta: {medicamento}"

    def mostrar_pacientes_atendidos(self):
        if not self.pacientes_atendidos:
            return "No se han atendido pacientes aún."
        return "Pacientes atendidos:\n" + "\n".join(self.pacientes_atendidos)

# Crear objetos Doctor
doctores = [
    Doctor("Carlos Perez", "Cardiología", 10),
    Doctor("Diñooo", "Dentista", 1),
    Doctor("Vidman", "Dermatólogo", 6)
]

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Doctores")
ventana.geometry("550x550")
ventana.configure(bg="#e6f2ff")

# Estilo para ttk
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=6)
style.configure("TLabel", background="#e6f2ff", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TMenubutton", font=("Helvetica", 12))

# Variables
doctor_var = tk.StringVar()
doctor_var.set("Carlos Perez")

# --- Frame Superior: Selección del doctor ---
frame_superior = tk.Frame(ventana, bg="#cce6ff", bd=2, relief="groove", padx=10, pady=10)
frame_superior.pack(pady=15, fill="x", padx=20)

ttk.Label(frame_superior, text="Selecciona un doctor:").pack()
opciones = [doc.nombre for doc in doctores]
ttk.OptionMenu(frame_superior, doctor_var, *opciones).pack(pady=5)

# --- Frame Medio: Entrada de datos ---
frame_datos = tk.Frame(ventana, bg="#e6f2ff", padx=10, pady=10)
frame_datos.pack(pady=10, fill="x", padx=20)

ttk.Label(frame_datos, text="👤 Nombre del paciente:").pack(anchor="w")
entrada_paciente = ttk.Entry(frame_datos, width=40)
entrada_paciente.pack(pady=5)

ttk.Label(frame_datos, text="💊 Medicamento:").pack(anchor="w")
entrada_medicamento = ttk.Entry(frame_datos, width=40)
entrada_medicamento.pack(pady=5)

# --- Funciones para botones ---
def obtener_doctor_seleccionado():
    nombre = doctor_var.get()
    for d in doctores:
        if d.nombre == nombre:
            return d
    return None

def mostrar_info():
    doctor = obtener_doctor_seleccionado()
    messagebox.showinfo("Información del Doctor", doctor.mostrar_informacion())

def atender():
    doctor = obtener_doctor_seleccionado()
    paciente = entrada_paciente.get()
    if paciente:
        resultado = doctor.atender_paciente(paciente)
        messagebox.showinfo("Atención al Paciente", resultado)
    else:
        messagebox.showwarning("Falta información", "Por favor, ingresa el nombre del paciente.")

def salario():
    doctor = obtener_doctor_seleccionado()
    resultado = doctor.calcular_salario()
    messagebox.showinfo("Salario", resultado)

def recetar():
    doctor = obtener_doctor_seleccionado()
    medicamento = entrada_medicamento.get()
    if medicamento:
        resultado = doctor.recetar_medicamento(medicamento)
        messagebox.showinfo("Receta", resultado)
    else:
        messagebox.showwarning("Falta información", "Por favor, ingresa el medicamento.")

def mostrar_pacientes_atendidos():
    doctor = obtener_doctor_seleccionado()
    resultado = doctor.mostrar_pacientes_atendidos()
    messagebox.showinfo("Pacientes Atendidos", resultado)

# --- Frame Inferior: Botones ---
frame_botones = tk.Frame(ventana, bg="#e6f2ff", pady=10)
frame_botones.pack(pady=10)

ttk.Button(frame_botones, text="📋 Mostrar Información", command=mostrar_info).grid(row=0, column=0, padx=10, pady=5)
ttk.Button(frame_botones, text="🩺 Atender Paciente", command=atender).grid(row=0, column=1, padx=10, pady=5)
ttk.Button(frame_botones, text="💰 Calcular Salario", command=salario).grid(row=1, column=0, padx=10, pady=5)
ttk.Button(frame_botones, text="💊 Recetar Medicamento", command=recetar).grid(row=1, column=1, padx=10, pady=5)

# --- Botón extra: Mostrar pacientes atendidos ---
tk.Button(
    ventana,
    text="📑 Mostrar Pacientes Atendidos",
    command=mostrar_pacientes_atendidos,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=5
).pack(pady=10)

# Pie de página
tk.Label(ventana, text="🧑‍⚕️ Sistema de Gestión de Doctores", bg="#cce6ff", font=("Helvetica", 10, "italic")).pack(side="bottom", fill="x")

ventana.mainloop()
