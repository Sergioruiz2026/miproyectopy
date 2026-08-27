# Modelado de una solución en UML

**Evaluación Sumativa N.º 1**  
**Asignatura:** POO Seguro  
**Docente:** Rubén Schnettler  
**Institución:** INACAP Valparaíso  
**Carrera:** Analista Programador  

## 1. Información general

- **Modalidad:** individual.
- **Ponderación:** 20 % de la asignatura.
- **Instrumento:** Rúbrica N.º 1, con 20 indicadores distribuidos en 4 criterios.
- **Formato:** documento único en PDF, con los diagramas incrustados como imágenes.
- **Entrega:** Ambiente de Aprendizaje INACAP, hasta las 23:00 horas de la fecha indicada.

### Distribución de la evaluación

- **Informe técnico:** 68 % de la nota.
- **Defensa oral:** 32 % de la nota.

La defensa oral utiliza la misma rúbrica del informe. Un informe correcto, pero sin defensa, no alcanza la aprobación.

## 2. Caso de evaluación: EcoTech Solutions

EcoTech Solutions es una empresa dedicada al desarrollo de tecnologías sostenibles. Durante el último año tuvo un crecimiento acelerado, lo que provocó desorden en la administración de su información interna.

Actualmente utiliza hojas de cálculo y sistemas aislados para gestionar:

- Empleados.
- Departamentos.
- Proyectos.
- Horas trabajadas.

La gerencia decidió reemplazar estos sistemas por una solución construida con Programación Orientada a Objetos.

### 2.1. Problemas actuales

1. Una misma persona aparece registrada dos veces con datos distintos.
2. Se producen errores al asignar personal a los proyectos.
3. No existe trazabilidad de las horas trabajadas.
4. Los reportes no son confiables debido a datos inconsistentes.
5. Existen riesgos de seguridad relacionados con los datos personales.

### 2.2. Requisitos del sistema

#### Registro de empleados

El sistema debe registrar:

- Nombre.
- Dirección.
- Teléfono.
- Correo electrónico.
- Fecha de contrato.
- Salario.
- Identificador asignado automáticamente.

#### Gestión de departamentos

El sistema debe permitir:

- Crear departamentos.
- Editar departamentos.
- Buscar departamentos.
- Eliminar departamentos.
- Asociar un gerente.
- Asociar empleados.

Un empleado pertenece a un solo departamento a la vez.

#### Gestión de proyectos

El sistema debe permitir:

- Crear proyectos.
- Editar proyectos.
- Eliminar proyectos.
- Registrar nombre, descripción y fecha de inicio.
- Asociar empleados.

Un empleado puede participar en uno o varios proyectos.

#### Registro de tiempo

Cada registro debe incluir:

- Fecha.
- Cantidad de horas.
- Descripción.
- Empleado asociado.
- Proyecto asociado.

#### Generación de informes

El sistema debe generar informes de:

- Empleados.
- Proyectos.
- Departamentos.
- Registros de tiempo.

Los informes deben poder exportarse a PDF o a una planilla.

### 2.3. Requisitos de seguridad

El sistema debe considerar:

- **Autenticación:** uso de contraseñas seguras.
- **Autorización:** cada usuario accede solo a los módulos permitidos.
- **Cifrado:** protección de los datos personales.
- **Validación:** revisión de toda entrada del usuario.
- **Encapsulamiento:** protección de los atributos sensibles.

La seguridad debe modelarse desde el inicio y no agregarse al final.

## 3. Pasos y criterios de evaluación

| Paso | Criterio | Producto esperado | Ponderación |
|---|---|---|---:|
| 1 | 1.1.1 | Análisis del problema desde la POO | 27 % |
| 2 | 1.1.2 | Diagrama de clases UML | 26 % |
| 3 | 1.1.3 | Evaluación crítica y ajuste del modelo generado con IA | 25 % |
| 4 | 1.1.4 | Solución final y matriz de trazabilidad | 22 % |

Los cuatro pasos deben utilizarse como estructura principal del informe.

## 4. Paso 1: análisis del problema desde la POO

El informe debe:

1. Identificar al menos cuatro entidades relevantes del dominio.
2. Describir cuatro elementos indicando:
   - Atributos.
   - Objetos posibles.
   - Una responsabilidad.
3. Relacionar tres conceptos de POO con el problema:
   - Encapsulamiento.
   - Abstracción.
   - Herencia.
4. Explicar cómo el enfoque orientado a objetos estructura la solución.
5. Clasificar y jerarquizar las entidades según el nivel de interacción entre ellas.
6. Exponer oralmente el análisis utilizando vocabulario técnico.

## 5. Paso 2: diseño del modelo estructural en UML

El informe debe:

1. Identificar y definir al menos tres clases principales.
2. Especificar los atributos con:
   - Visibilidad.
   - Nombre.
   - Tipo de dato.
3. Especificar los métodos con:
   - Visibilidad.
   - Parámetros.
   - Tipo de retorno.
4. Definir al menos tres relaciones indicando:
   - Tipo de relación.
   - Multiplicidad en ambos extremos.
5. Elaborar un diagrama UML organizado, legible y correctamente estructurado.
6. Explicar verbalmente la arquitectura y el propósito de cada relación.

### Consideración importante

Un diagrama sin modificadores de visibilidad ni tipos de dato se considera elemental, aunque el resto esté correcto.

## 6. Paso 3: evaluación y ajuste del modelo generado con IA

El informe debe incluir:

1. Al menos dos iteraciones de propuestas generadas con IA.
2. Dos prompts documentados con:
   - Contexto del problema.
   - Tarea solicitada.
   - Alcance.
   - Formato esperado.
3. Los resultados obtenidos en cada iteración.
4. El análisis de al menos cuatro elementos, clasificados como:
   - Errores.
   - Similitudes.
   - Diferencias.
5. Los ajustes aplicados a la propuesta inicial.
6. La justificación técnica de cada corrección.
7. La aplicación de criterios de diseño orientado a objetos.

No es suficiente presentar únicamente el resultado generado por la IA. Se debe demostrar análisis crítico y participación en el diseño.

## 7. Paso 4: construcción y validación de la solución final

El informe debe incluir:

1. El diagrama final con las mejoras incorporadas.
2. La aplicación de tres principios de diseño:
   - Cohesión.
   - Responsabilidad única.
   - Encapsulamiento.
3. Una matriz de trazabilidad que relacione al menos tres requerimientos con sus clases.
4. La relación entre requerimientos, clases, atributos y métodos.
5. La fundamentación técnica de las decisiones de diseño.
6. La explicación de la viabilidad técnica del modelo en Python.
7. La defensa oral de la solución final.

## 8. Secciones exigidas en el informe

El documento debe contener:

1. Portada.
2. Índice.
3. Introducción.
4. Análisis del problema.
5. Diseño del sistema.
6. Uso de herramientas de IA.
7. Mejoras aplicadas.
8. Matriz de trazabilidad.
9. Conclusiones.
10. Referencias.
11. Numeración de páginas.

## 9. Matriz de trazabilidad

| Requisito | Clases relacionadas | Atributos y métodos |
|---|---|---|
| Registrar empleados con identificador automático | `Empleado` | `idEmpleado`, constructor, datos personales |
| Asociar un empleado a un departamento | `Empleado`, `Departamento` | `departamento`, `empleados`, `asignarEmpleado()` |
| Registrar horas por empleado y proyecto | `RegistroTiempo`, `Empleado`, `Proyecto` | `fecha`, `horas`, `registrarHoras()` |
| Proteger datos sensibles | `Empleado`, `Usuario` | atributos privados, cifrado, hash |
| Validar entradas del usuario | `RegistroTiempo`, `Usuario` | validaciones, excepciones, `ValueError` |

Se recomienda incluir al menos un requerimiento relacionado con seguridad.

## 10. Instrumento de evaluación

La rúbrica considera cinco niveles por indicador:

1. Ausente.
2. Inicial.
3. Elemental.
4. Competente.
5. Experto.

La diferencia principal entre el nivel competente y el experto consiste en justificar técnicamente las decisiones y explicar sus consecuencias.

### Indicadores evaluados en la defensa oral

| Indicador | Aspecto evaluado | Ponderación |
|---|---|---:|
| 1.1.1.I.5 | Exponer el análisis conceptual y justificar las entidades | 8 % |
| 1.1.2.I.10 | Explicar la arquitectura y las relaciones del diagrama | 8 % |
| 1.1.3.I.15 | Justificar las correcciones realizadas al modelo de IA | 8 % |
| 1.1.4.I.20 | Defender la viabilidad técnica y postura crítica frente a la IA | 8 % |

En total, el 32 % del instrumento depende de la defensa oral.

## 11. Criterios para alcanzar el nivel experto

### Entidades

- **Competente:** identifica y clasifica tres entidades.
- **Experto:** identifica cuatro entidades y las jerarquiza según su interacción.

### Fundamentos de POO

- **Competente:** relaciona tres conceptos con el problema.
- **Experto:** explica también sus implicancias para la seguridad del software.

### Relaciones

- **Competente:** define tres relaciones con tipo y multiplicidad.
- **Experto:** explica el efecto de las dependencias fuertes sobre el acoplamiento.

### Uso de IA

- **Competente:** presenta un prompt con contexto y formato.
- **Experto:** presenta dos o más prompts y demuestra la evolución de las instrucciones.

### Principios de diseño

- **Competente:** aplica dos principios en la mayoría de las clases.
- **Experto:** aplica tres principios en todas las clases y deja registro documental.

## 12. Estructura de la defensa oral

La defensa tiene una duración aproximada de diez minutos.

### Bloque 1: problema y entidades — 2 minutos

- Explicar la situación de EcoTech Solutions.
- Presentar las cuatro entidades.
- Justificar la selección.

### Bloque 2: diagrama UML — 3 minutos

- Recorrer las clases.
- Explicar las relaciones.
- Justificar los tipos y multiplicidades.

### Bloque 3: trabajo con IA — 3 minutos

- Explicar los prompts utilizados.
- Presentar los resultados.
- Indicar qué se aceptó y qué se descartó.
- Justificar al menos dos correcciones técnicas.

### Bloque 4: viabilidad y postura crítica — 2 minutos

- Mostrar la viabilidad del diseño en Python.
- Explicar los principios aplicados.
- Defender un uso crítico y responsable de la IA.

## 13. Lista de verificación

- [ ] Cuatro entidades relevantes.
- [ ] Cuatro elementos con atributos, objetos y responsabilidades.
- [ ] Tres conceptos de POO relacionados con el problema.
- [ ] Tres clases principales.
- [ ] Atributos con visibilidad y tipo.
- [ ] Métodos con parámetros y tipo de retorno.
- [ ] Tres relaciones con tipo y multiplicidad.
- [ ] Diagrama UML legible.
- [ ] Dos iteraciones con IA.
- [ ] Dos prompts documentados con sus resultados.
- [ ] Cuatro elementos analizados críticamente.
- [ ] Modelo final ajustado.
- [ ] Tres principios de diseño aplicados.
- [ ] Matriz de trazabilidad.
- [ ] Al menos tres requerimientos cruzados con clases.
- [ ] Portada e índice.
- [ ] Referencias.
- [ ] Numeración de páginas.
- [ ] Diagramas incrustados en el PDF.

## 14. Entrega

El informe debe entregarse:

- En un único documento PDF.
- Con los diagramas incrustados como imágenes.
- Mediante el Ambiente de Aprendizaje INACAP.
- Antes de la fecha y hora publicadas.

