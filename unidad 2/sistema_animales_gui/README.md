# Sistema de Registro de Animales

Este proyecto es una aplicación de escritorio para el registro de animales, que permite a los usuarios registrar felinos y aves, así como visualizar la información de los animales registrados. La aplicación cuenta con una interfaz gráfica amigable y colorida, diseñada para facilitar la interacción del usuario.

## Estructura del Proyecto

El proyecto está organizado en la siguiente estructura de directorios:

```
sistema_animales_gui
├── src
│   ├── main.py          # Punto de entrada de la aplicación
│   ├── gui.py           # Definición de la interfaz gráfica
│   ├── models           # Contiene las definiciones de las clases de animales
│   │   ├── animal.py    # Clase base para todos los animales
│   │   ├── felino.py    # Clase para felinos
│   │   └── ave.py       # Clase para aves
│   └── utils            # Utilidades para el proyecto
│       └── styles.py    # Estilos visuales para la interfaz gráfica
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Documentación del proyecto
```

## Instalación

1. Clona este repositorio en tu máquina local.
2. Navega al directorio del proyecto.
3. Instala las dependencias necesarias ejecutando:

```
pip install -r requirements.txt
```

## Uso

Para ejecutar la aplicación, utiliza el siguiente comando:

```
python src/main.py
```

Esto abrirá la interfaz gráfica donde podrás registrar felinos y aves, así como visualizar la información de los animales registrados.

## Funcionalidades

- Registrar felinos con nombre, edad, especie y color de pelaje.
- Registrar aves con nombre, edad, especie y tipo de pico.
- Mostrar la lista de todos los animales registrados con su información correspondiente.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.