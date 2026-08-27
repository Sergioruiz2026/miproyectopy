# Informe de Evaluación 1

## EcoTech Solutions: propuesta de sistema orientado a objetos

## 1. Introducción

EcoTech Solutions es una empresa dedicada al desarrollo de tecnologías sostenibles. Durante el último año experimentó un crecimiento acelerado y su información interna quedó distribuida entre hojas de cálculo y sistemas aislados.

Este informe propone un modelo basado en Programación Orientada a Objetos (POO) para centralizar la gestión de empleados, departamentos, proyectos y horas trabajadas. El diseño prioriza la integridad de los datos, la trazabilidad de las operaciones y la protección de la información personal.

## 2. Problema identificado

La situación actual genera los siguientes problemas:

1. Una misma persona puede aparecer registrada más de una vez con datos diferentes.
2. Se puede asignar personal incorrectamente a los proyectos.
3. No existe trazabilidad suficiente de las horas trabajadas ni de las tareas realizadas.
4. Los informes no son confiables porque se construyen a partir de datos inconsistentes.
5. Los datos personales están expuestos a riesgos de seguridad.

La solución debe centralizar la información y establecer reglas que impidan inconsistencias desde el propio modelo.

## 3. Objetivos del sistema

- Mantener un registro único de cada empleado.
- Administrar departamentos, gerentes y empleados.
- Gestionar proyectos y sus asignaciones de personal.
- Registrar las horas trabajadas con fecha, descripción, empleado y proyecto.
- Generar informes de empleados, departamentos, proyectos y registros de tiempo.
- Proteger la información sensible mediante autenticación, autorización, validación y encapsulamiento.

## 4. Propuesta de modelo de clases

### 4.1. Empleado

Representa a una persona contratada por la empresa.

**Atributos:**

- `idEmpleado: int`, asignado automáticamente.
- `nombre: str`.
- `direccion: str`.
- `telefono: str`.
- `correo: str`.
- `fechaContrato: date`.
- `salario: float`.
- `departamento: Departamento`.
- `proyectos: list[Proyecto]`.

Los datos personales deben mantenerse protegidos. En una implementación real, la dirección, el teléfono y el correo deberían almacenarse cifrados y no exponerse como atributos públicos.

**Métodos principales:**

- `actualizarDatos()`.
- `asignarDepartamento()`.
- `asignarProyecto()`.
- `quitarProyecto()`.

### 4.2. Departamento

Agrupa empleados que pertenecen a una misma unidad organizativa.

**Atributos:**

- `idDepartamento: int`.
- `nombre: str`.
- `gerente: Empleado`.
- `empleados: list[Empleado]`.

**Métodos principales:**

- `crear()`.
- `editar()`.
- `buscar()`.
- `eliminar()`.
- `agregarEmpleado()`.
- `quitarEmpleado()`.

### 4.3. Proyecto

Representa una iniciativa de la empresa.

**Atributos:**

- `idProyecto: int`.
- `nombre: str`.
- `descripcion: str`.
- `fechaInicio: date`.
- `empleados: list[Empleado]`.
- `registrosTiempo: list[RegistroTiempo]`.

**Métodos principales:**

- `crear()`.
- `editar()`.
- `eliminar()`.
- `agregarEmpleado()`.
- `quitarEmpleado()`.

### 4.4. RegistroTiempo

Representa el trabajo realizado por un empleado en un proyecto.

**Atributos:**

- `fecha: date`.
- `horas: float`.
- `descripcion: str`.
- `empleado: Empleado`.
- `proyecto: Proyecto`.

**Métodos principales:**

- `validarHoras()`.
- `registrar()`.
- `editar()`.

Un registro solo debe aceptarse si el empleado está asignado al proyecto y si la cantidad de horas es válida.

### 4.5. Usuario y autenticación

Para controlar el acceso al sistema se propone una clase `Usuario` relacionada con `Empleado`.

**Atributos:**

- `idUsuario: int`.
- `nombreUsuario: str`.
- `contrasenaHash: str`.
- `rol: str`.

La contraseña nunca debe almacenarse en texto plano. El sistema debe guardar únicamente un hash seguro y comprobar los permisos antes de permitir el acceso a cada módulo.

## 5. Relaciones y multiplicidades

### Empleados y departamentos

La relación es de uno a muchos:

- Un departamento puede tener cero o muchos empleados: `Departamento 1 --- 0..* Empleado`.
- Un empleado pertenece a un solo departamento a la vez: `Empleado 1 --- 1 Departamento`.

### Empleados y proyectos

La relación es de muchos a muchos:

- Un empleado puede participar en cero o muchos proyectos.
- Un proyecto puede tener cero o muchos empleados.

En Python, esta relación puede representarse con una lista de proyectos en `Empleado` y una lista de empleados en `Proyecto`. La asignación debe actualizar ambos lados para evitar inconsistencias.

### Empleados, proyectos y registros de tiempo

Cada `RegistroTiempo` se asocia con exactamente un empleado y un proyecto. Un empleado y un proyecto pueden tener cero o muchos registros de tiempo.

```text
Empleado 1 -------- 0..* RegistroTiempo 0..* -------- 1 Proyecto
Departamento 1 ---- 0..* Empleado
Empleado 0..* ----- 0..* Proyecto
```

## 6. Reglas de negocio

1. El identificador de un empleado debe ser único y asignarse automáticamente.
2. Un empleado no puede pertenecer simultáneamente a dos departamentos.
3. Un empleado solo puede registrar horas en proyectos a los que está asignado.
4. Las horas deben ser mayores que cero y respetar un límite razonable por registro.
5. No se debe eliminar un departamento si todavía tiene empleados sin reasignar.
6. No se debe eliminar un proyecto si existen registros de tiempo que perderían su trazabilidad.
7. Los informes deben generarse a partir de los datos validados y centralizados.
8. Solo los usuarios autorizados pueden consultar o modificar datos sensibles.

## 7. Seguridad y encapsulamiento

La seguridad debe formar parte del diseño desde el comienzo:

- **Autenticación:** comprobar la identidad mediante credenciales protegidas.
- **Autorización:** limitar cada usuario a los módulos que corresponden a su rol.
- **Cifrado:** proteger los datos personales almacenados.
- **Validación:** revisar los datos recibidos antes de guardarlos.
- **Encapsulamiento:** ocultar los atributos sensibles y permitir su modificación mediante métodos controlados.
- **Trazabilidad:** conservar quién registró o modificó cada dato relevante.

Una clase `Sistema` o `Gestor` no debería concentrar todas las responsabilidades. Es preferible que cada clase controle sus propios datos y que servicios específicos coordinen operaciones entre varias clases.

## 8. Generación de informes

El sistema debe permitir generar informes de:

- Empleados y departamentos.
- Proyectos y sus integrantes.
- Horas trabajadas por empleado.
- Horas trabajadas por proyecto.
- Registros filtrados por fecha.

Los informes deben poder exportarse a PDF o a una planilla. Antes de exportarlos, se deben validar los datos de origen y aplicar los permisos del usuario que realiza la consulta.

## 9. Aplicación de los conceptos de POO

- **Clases:** representan empleados, departamentos, proyectos y registros de tiempo.
- **Objetos:** son las instancias concretas de esas clases.
- **Atributos:** almacenan la información de cada objeto.
- **Métodos:** implementan las operaciones y reglas de negocio.
- **Encapsulamiento:** protege los datos personales y controla su modificación.
- **Asociación:** conecta empleados con departamentos y proyectos.
- **Composición:** puede utilizarse entre un proyecto y sus registros de tiempo cuando estos no tengan sentido fuera del proyecto.

## 10. Estado actual del repositorio

El archivo `main.py` implementa las cinco clases principales del modelo: `Empleado`, `Departamento`, `Proyecto`, `RegistroTiempo` y `Usuario`.

La implementación incluye creación y edición de entidades, asignaciones bidireccionales entre empleados, departamentos y proyectos, validación de horas, restricciones para eliminar entidades con dependencias y autorización básica por roles. La persistencia en base de datos, el cifrado de datos personales, el hash real de contraseñas y los informes exportables quedan como etapas posteriores del proyecto.

## 11. Uso de Inteligencia Artificial

Para documentar el uso responsable de IA, cada consulta debe conservar:

1. El contexto entregado.
2. La tarea solicitada.
3. La respuesta obtenida.
4. Las decisiones aceptadas y descartadas.
5. La justificación técnica de cada modificación.

Las propuestas generadas por IA deben clasificarse como errores, diferencias o similitudes. No se debe aceptar automáticamente una solución que concentre responsabilidades en una clase genérica como `Sistema` o `Gestor`.

## 12. Conclusión

Un sistema orientado a objetos permite a EcoTech Solutions reemplazar información dispersa por un modelo centralizado, coherente y extensible. La distinción entre la relación uno a muchos de departamentos y la relación muchos a muchos de proyectos es fundamental para evitar errores de asignación.

El diseño también incorpora seguridad, validación y trazabilidad como responsabilidades del sistema, en lugar de tratarlas como funciones añadidas al final. La siguiente etapa sería implementar las clases propuestas, añadir persistencia, crear pruebas automatizadas y desarrollar los módulos de autenticación y generación de informes.
