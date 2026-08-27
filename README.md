# Gestión de socios

Ejemplo sencillo en Python para registrar socios, contabilizar sus visitas y comprobar si pueden acceder según su estado de pago.

## Requisitos

- Python 3.8 o superior

El proyecto no utiliza dependencias externas.

## Ejecución

Desde la carpeta raíz del repositorio, ejecuta:

```bash
python main.py
```

En Windows también puedes usar:

```powershell
py main.py
```

## Cómo funciona

La clase `Socio` contiene:

- `nombre`: nombre del socio.
- `numero_socio`: identificador del socio.
- `al_dia`: indica si sus pagos están al día.
- `visitas`: número de visitas registradas.

Además, ofrece dos operaciones principales:

- `registrar_visita()`: suma una visita al socio.
- `puede_entrar()`: devuelve si el socio tiene permitido el acceso.

El script crea tres socios de ejemplo, registra sus visitas y muestra sus datos junto con el permiso de entrada.

## Ejemplo de salida

```text
-------------------------
Nombre: Juan Pérez
Número de socio: 101
Visitas: 2
Puede entrar: Sí
```

La salida completa incluye también a María González y Pedro Soto.

## Estructura

```text
.
├── main.py       # Programa principal
├── apuntes.md    # Apuntes del proyecto
├── informe.txt   # Informe del proyecto
└── README.md     # Documentación
```

## Licencia

Este proyecto es un ejercicio educativo y no incluye una licencia específica.
