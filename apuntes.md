# Apuntes de Programación Orientada a Objetos

## 1. Del código al objeto

La Programación Orientada a Objetos (POO) permite organizar el código agrupando los datos y las funciones que trabajan con ellos dentro de estructuras comunes. Estos apuntes utilizan Python 3.13.2.

## 2. Entorno de trabajo

### Crear un entorno virtual

Un entorno virtual (`venv`) es una copia aislada de Python que evita conflictos con las librerías instaladas globalmente.

```bash
python -m venv .venv
```

### Activar el entorno

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Si PowerShell requiere permisos, se puede configurar la política de ejecución con:

```powershell
Set-ExecutionPolicy
```

En macOS o Linux:

```bash
source .venv/bin/activate
```

Cuando el entorno está activo, aparece `(.venv)` al principio de la terminal.

### Configurar VS Code

1. Abrir la carpeta raíz del proyecto.
2. Instalar la extensión de Python.
3. Seleccionar explícitamente el intérprete ubicado dentro de `.venv`.

Esto ayuda a evitar errores causados por utilizar un intérprete diferente al del proyecto.

## 3. Paradigma de la POO y sus ventajas

### Problema del enfoque tradicional

Cuando los datos y las funciones se mantienen separados y sin una estructura común, pueden aparecer:

- Datos desprotegidos.
- Código duplicado.
- Poca cohesión entre las partes del programa.

### Solución mediante POO

La POO reúne los datos y las reglas que los controlan. Esta idea se conoce como **encapsulamiento**.

### Ventajas principales

1. **Cohesión:** los datos y las operaciones relacionadas permanecen juntos.
2. **Seguridad:** el acceso a los datos puede estar controlado.
3. **Reutilización:** la herencia permite aprovechar código existente.
4. **Escalabilidad:** se pueden añadir funcionalidades sin romper todo el sistema.

## 4. Conceptos básicos en Python

### Clase

Es el molde o definición de un tipo de objeto.

```python
class Auto:
	pass
```

### Objeto

Es una instancia concreta creada a partir de una clase. Cada objeto guarda sus propios valores.

### Atributos

Son los datos internos que almacena un objeto. Algunos tipos habituales son `str`, `int`, `float`, `bool`, `date` y `list`.

### Métodos

Son funciones internas de una clase que definen las acciones que puede realizar un objeto. Reciben `self` como primer parámetro, porque representa al propio objeto.

### Constructor

`__init__` es un método especial que se ejecuta automáticamente al crear una instancia. Sirve para recibir y establecer los datos iniciales necesarios.

### Herencia

Permite extender una clase padre mediante una clase hija:

```python
class Camion(Auto):
	pass
```

El método `super().__init__()` ejecuta el constructor de la clase padre y evita duplicar código.

## 5. Del código al diagrama UML

El Lenguaje Unificado de Modelado (UML 2.5.1) permite representar el diseño de un sistema sin tener que revisar todo el código. Un diagrama de clases también facilita discutir el diseño con otras personas y con herramientas de Inteligencia Artificial.

### Notación de una clase

Una clase se representa mediante una caja dividida en tres partes:

1. **Nombre:** en singular y con mayúscula inicial, usando PascalCase.
2. **Atributos:** escritos en camelCase, indicando visibilidad y tipo. Ejemplo: `- patente: str`.
3. **Métodos:** incluyen visibilidad, parámetros tipados y tipo de retorno. Ejemplo: `+ sumarKm(nuevos: float): float`.

Cuando un método no devuelve ningún valor, se indica `: void`.

### Visibilidad y encapsulamiento

- **Privado (`-`):** en Python se representa normalmente con doble guion bajo, por ejemplo `self.__atributo`. Solo la propia clase debería modificarlo.
- **Público (`+`):** los métodos públicos son accesibles desde cualquier clase del sistema y actúan como puertas de entrada al objeto.
- **Protegido (`#`):** en Python se representa con un solo guion bajo, por ejemplo `self._atributo`. Puede ser utilizado por la clase y sus clases herederas.

Como regla práctica, los atributos deberían mantenerse privados y exponerse mediante métodos controlados.

### Relaciones entre clases

#### Asociación

Se representa con una línea simple. Las clases se conocen y colaboran, pero existen de forma independiente. Ejemplo: `Cliente` y `Auto`.

#### Agregación

Se representa con un rombo vacío. Es una relación de "todo-parte" débil: la parte puede sobrevivir si el todo se destruye. Ejemplo: un `Taller` que agrupa a sus `Mecanicos`.

#### Composición

Se representa con un rombo lleno. Es una relación de "todo-parte" fuerte: si el todo desaparece, la parte pierde su sentido o también deja de existir. Ejemplo: un `Auto` y sus `Atenciones`.

El rombo siempre se coloca del lado del objeto contenedor.

#### Generalización

Se representa con una flecha cuyo extremo tiene un triángulo vacío. Indica herencia, es decir, una relación de tipo "es un". La flecha apunta hacia la clase padre.

### Multiplicidad y diseño de sistemas

La multiplicidad indica cuántos objetos participan en cada extremo de una relación. Algunos valores habituales son:

- `1`: exactamente uno.
- `0..1`: cero o uno.
- `1..*`: uno o más.
- `0..*`: cero o más.

La multiplicidad se lee de manera cruzada y debe deducirse estrictamente del enunciado del problema.

En Python, las relaciones suelen representarse guardando listas de objetos dentro del constructor de otra clase:

```python
class Cliente:
	def __init__(self):
		self.autos = []
```

## 6. Uso de IA en la evaluación

Para cumplir con el estándar experto de la asignatura, se debe documentar el proceso de uso de la IA.

### Esquema claro para prompts

Un prompt útil puede incluir los siguientes elementos:

- **Contexto:** información del problema.
- **Labor:** tarea que debe realizar la IA.
- **Alcance:** límites y entregables esperados.
- **Rol:** perspectiva que debe adoptar la IA.
- **Orden:** instrucciones concretas sobre el resultado y el formato.

### Evidencias

Registrar al menos dos iteraciones con la IA:

1. Una propuesta inicial o base.
2. Una propuesta descartada, junto con las razones técnicas del rechazo.

### Tabla de análisis

Clasificar la propuesta de la IA en:

- **Errores:** elementos incorrectos o que no cumplen el enunciado.
- **Diferencias:** alternativas de diseño que se apartan de la solución elegida.
- **Similitudes:** decisiones que coinciden con el diseño final.

Cada decisión debe justificarse técnicamente. Por ejemplo, se puede rechazar una clase `Sistema` o `Gestor` si concentra demasiadas responsabilidades y rompe la separación de responsabilidades.
apunte de POO

Resumen de Archivo 1: Del Código al ObjetoEste primer bloque introduce los fundamentos prácticos de la Programación Orientada a Objetos (POO) utilizando Python 3.13.2.1. Entorno de Trabajo (Pasos Obligatorios)Creación del Entorno Virtual (venv): Copia aislada de Python para evitar conflictos de librerías globales. Se genera con $ python -m venv .venv.Activación: En Windows PowerShell se ejecuta .venv\Scripts\Activate.ps1 (requiere permisos con Set-ExecutionPolicy). En macOS/Linux se usa source .venv/bin/activate. Muestra (.venv) al inicio de la terminal.Configuración en VS Code: Se debe abrir la carpeta raíz, instalar la extensión de Python y seleccionar explícitamente el intérprete que apunta a .venv para evitar errores incomprensibles.2. El Paradigma de la POO y sus VentajasProblema clásico: Datos (variables) y funciones separados de forma suelta. Esto genera desprotección del dato, duplicación de código y falta de cohesión.Solución POO: Guardar juntos los datos y sus reglas mediante una estructura común (Encapsulamiento).4 Ventajas Concretas: Todo junto (cohesión), datos protegidos (seguridad), reutilización de código (herencia) y escalabilidad sin romper lo existente.3. Conceptos Base en Código PythonClase: Es el molde o definición única de un tipo de objeto (ej. class Auto:).Objeto: Caso concreto o instancia creada a partir de la clase, que guarda sus propios valores.Atributos: Los datos internos que guarda el objeto (tipos como str, int, float, bool, date, list).Métodos: Funciones internas de la clase que definen acciones. Reciben siempre self como primer parámetro (representa al objeto mismo).Constructor (__init__): Método especial que se ejecuta automáticamente al instanciar el objeto, obligando a ingresar los datos iniciales necesarios.Herencia: Permite extender una clase padre a una hija colocando el padre entre paréntesis (ej. class Camion(Auto):). El comando super().__init__() ejecuta el constructor padre para no duplicar código.Resumen de Archivo 2: Del Código al DiagramaLa segunda parte se enfoca en el modelado técnico usando el Lenguaje Unificado de Modelado (UML 2.5.1) y la interacción con Inteligencia Artificial.1. La Notación de una Clase en UMLUn diagrama de clases permite discutir diseños de software de un vistazo sin revisar el código. Se representa mediante una caja de tres pisos:Piso 1: Nombre de la clase en singular y con mayúscula inicial (PascalCase).Piso 2: Atributos en camelCase, especificando obligatoriamente su visibilidad y tipo (ej: - patente: str).Piso 3: Métodos con su firma completa: visibilidad, parámetros tipados y tipo de retorno (ej: + sumarKm(nuevos: float): float). Si no retorna nada, se explicita con : void.2. Visibilidad y EncapsulamientoPrivado (-): En Python se escribe con doble guion bajo (self.__atributo). Solo la propia clase puede modificarlo. Los atributos deben ser privados por regla práctica.Público (+): Métodos accesibles por cualquier clase del sistema (las puertas de entrada al objeto).Protegido (#): En Python usa un solo guion bajo (self._atributo). Accesible por la clase y sus herederas.3. Las 4 Relaciones entre ClasesAsociación (Línea simple): Las clases se conocen y colaboran, pero existen de forma independiente (ej. Cliente y Auto).Agregación (Rombo vacío): Relación "todo-parte" débil. La parte sobrevive si el todo se destruye (ej. Taller agrupa a Mecánicos).Composición (Rombo lleno): Relación "todo-parte" fuerte. Si el todo se borra, la parte pierde sentido o muere (ej. Auto y Atenciones). El rombo va siempre del lado del objeto contenedor.Generalización (Flecha con triángulo vacío): Representa la herencia ("Es un") y apunta siempre hacia la clase padre.4. Multiplicidad y Diseño de SistemasIndica cuántos objetos participan en cada extremo de una relación (1, 0..1, 1..*, 0..*). Se lee de manera cruzada y proviene estrictamente del enunciado del problema.En código Python, las relaciones se representan guardando listas de objetos dentro del constructor de otra clase (ej. self.autos = [] dentro de Cliente).5. Uso de IA en la Evaluación (Criterio 1.1.3)Para cumplir con el estándar experto de la asignatura, el estudiante debe documentar:Esquema CLARO para Prompts: Estructura para consultar a la IA que incluye Contexto, Labor, Alcance, Rol y Orden.Evidencias: Registrar dos iteraciones con la IA (una base y una descartada con razones técnicas).Tabla de Análisis: Clasificar la propuesta de la IA en Errores, Diferencias o Similitudes, fundamentando técnicamente cada decisión de diseño tomada (ej. rechazar clases "Sistema/Gestor" que concentran excesivas responsabilidades)