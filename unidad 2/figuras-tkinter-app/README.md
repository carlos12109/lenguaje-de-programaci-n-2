# Figuras Tkinter App

Este proyecto es una aplicación de escritorio desarrollada en Python utilizando Tkinter para la creación de una interfaz gráfica. La aplicación permite registrar y mostrar diferentes figuras geométricas, incluyendo círculos, rectángulos, triángulos, pentágonos y hexágonos.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura de archivos:

```
figuras-tkinter-app
├── src
│   ├── main.py                # Punto de entrada de la aplicación
│   ├── figuras
│   │   ├── __init__.py        # Permite que el directorio figuras sea un paquete
│   │   ├── figura.py          # Clase base Figura
│   │   ├── circulo.py         # Clase Circulo
│   │   ├── rectangulo.py      # Clase Rectangulo
│   │   ├── triangulo.py       # Clase Triangulo
│   │   ├── pentagono.py       # Clase Pentagono
│   │   └── hexagono.py        # Clase Hexagono
│   └── ui
│       └── interfaz.py        # Interfaz gráfica de usuario
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Documentación del proyecto
```

## Requisitos

Para ejecutar esta aplicación, asegúrate de tener Python instalado en tu sistema. Además, necesitarás instalar las dependencias listadas en el archivo `requirements.txt`.

## Instalación

1. Clona este repositorio en tu máquina local.
2. Navega al directorio del proyecto.
3. Instala las dependencias ejecutando:

   ```
   pip install -r requirements.txt
   ```

## Ejecución

Para ejecutar la aplicación, utiliza el siguiente comando:

```
python src/main.py
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.