from abc import ABC, abstractmethod
from typing import List

# -------------------- VEHICULOS --------------------
class Vehiculo(ABC):
    """
    Clase base abstracta para representar un vehículo.
    Aplica los principios SRP y LSP.
    """
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def obtener_datos(self) -> str:
        """Método que debe ser implementado para obtener información específica del vehículo."""
        pass

class Auto(Vehiculo):
    """
    Representa un automóvil con número de pasajeros.
    """
    def __init__(self, marca: str, modelo: str, pasajeros: int):
        super().__init__(marca, modelo)
        self.pasajeros = pasajeros

    def obtener_datos(self) -> str:
        return f"Auto - Marca: {self.marca}, Modelo: {self.modelo}, Pasajeros: {self.pasajeros}"

class Camion(Vehiculo):
    """
    Representa un camión con capacidad de carga.
    """
    def __init__(self, marca: str, modelo: str, carga_max: float):
        super().__init__(marca, modelo)
        self.carga_max = carga_max

    def obtener_datos(self) -> str:
        return f"Camion - Marca: {self.marca}, Modelo: {self.modelo}, Carga Máx: {self.carga_max} kg"

class Moto(Vehiculo):
    """
    Representa una motocicleta con tipo.
    """
    def __init__(self, marca: str, modelo: str, tipo: str):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def obtener_datos(self) -> str:
        return f"Moto - Marca: {self.marca}, Modelo: {self.modelo}, Tipo: {self.tipo}"

# -------------------- INTERFACES DE REPORTE --------------------
class Reporte(ABC):
    """
    Interfaz para los distintos tipos de reporte.
    Aplica el principio ISP.
    """
    @abstractmethod
    def generar(self, vehiculos: List[Vehiculo]) -> None:
        pass

class ReporteConsola(Reporte):
    """
    Implementación concreta del reporte por consola.
    """
    def generar(self, vehiculos: List[Vehiculo]) -> None:
        print("Reporte por Consola:")
        autos = [v for v in vehiculos if isinstance(v, Auto)]
        camiones = [v for v in vehiculos if isinstance(v, Camion)]
        motos = [v for v in vehiculos if isinstance(v, Moto)]

        print("\n--- AUTOS ---")
        for v in autos:
            print(v.obtener_datos())
        print("\n--- CAMIONES ---")
        for v in camiones:
            print(v.obtener_datos())
        print("\n--- MOTOS ---")
        for v in motos:
            print(v.obtener_datos())

class ReporteArchivoTexto(Reporte):
    """
    Implementación concreta del reporte en archivo de texto.
    """
    def generar(self, vehiculos: List[Vehiculo]) -> None:
        autos = sorted([v for v in vehiculos if isinstance(v, Auto)], key=lambda v: (v.marca, v.modelo))
        camiones = sorted([v for v in vehiculos if isinstance(v, Camion)], key=lambda v: (v.marca, v.modelo))
        motos = sorted([v for v in vehiculos if isinstance(v, Moto)], key=lambda v: (v.marca, v.modelo))

        with open("reporte_vehiculos.txt", "w", encoding="utf-8") as archivo:
            archivo.write("Reporte en archivo de texto :\n")
            archivo.write("\n--- AUTOS ---\n")
            for v in autos:
                archivo.write(v.obtener_datos() + "\n")
                print(v.obtener_datos())
            archivo.write("\n--- CAMIONES ---\n")
            for v in camiones:
                archivo.write(v.obtener_datos() + "\n")
                print(v.obtener_datos())
            archivo.write("\n--- MOTOS ---\n")
            for v in motos:
                archivo.write(v.obtener_datos() + "\n")
                print(v.obtener_datos())

class ReportePDF(Reporte):
    """
    Implementación simulada del reporte en formato PDF.
    """
    def generar(self, vehiculos: List[Vehiculo]) -> None:
        print("(Simulado) Reporte generado como PDF:")
        for vehiculo in vehiculos:
            print(vehiculo.obtener_datos())

# -------------------- GENERADOR DE REPORTES --------------------
class GeneradorReportes:
    """
    Clase que utiliza inyección de dependencias para generar reportes.
    Aplica DIP y composición para delegar responsabilidades.
    """
    def __init__(self, reporte: Reporte):
        self.reporte = reporte

    def generar_reporte(self, vehiculos: List[Vehiculo]) -> None:
        self.reporte.generar(vehiculos)

# -------------------- EJECUCIÓN --------------------
if __name__ == "__main__":
    # Lista de vehículos con sus datos específicos
    vehiculos: List[Vehiculo] = [
        Auto("Toyota", "Corolla", 5),
        Camion("Volvo", "FH16", 25000),
        Moto("Yamaha", "FZ", "Deportiva"),
        Auto("Honda", "Civic", 4),
        Camion("Mercedes-Benz", "Actros", 18000),
        Moto("Suzuki", "GSX-R", "Deportiva"),
        Auto("Chevrolet", "Onix", 5),
        Camion("Scania", "R500", 30000),
        Moto("Kawasaki", "Ninja", "Sport"),
        Camion("MAN", "TGX", 20000),
        Moto("Honda", "CBR600RR", "Sport")
    ]

    # Ordenar por marca y luego por modelo
    vehiculos_ordenados = sorted(vehiculos, key=lambda v: (v.marca, v.modelo))

    print("--- Reporte Consola ---")
    GeneradorReportes(ReporteConsola()).generar_reporte(vehiculos_ordenados)

    print("\n--- Reporte Archivo de Texto (y Consola) ---")
    GeneradorReportes(ReporteArchivoTexto()).generar_reporte(vehiculos_ordenados)
