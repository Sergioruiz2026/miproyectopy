#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generar diagrama UML de EcoTech Solutions
"""

from graphviz import Digraph

# Crear el grafo
g = Digraph('EcoTech Solutions UML', format='png', engine='dot')
g.attr(rankdir='TB')
g.attr('graph', bgcolor='white', pad='0.5', nodesep='0.5', ranksep='1.2')
g.attr('node', shape='box', style='filled', fillcolor='lightblue', 
       fontname='Arial', fontsize='10', margin='0.2,0.1')
g.attr('edge', fontname='Arial', fontsize='9')

# Definir los colores para cada clase
colors = {
    'Empleado': '#d4e6f1',
    'Departamento': '#d5f4e6',
    'Proyecto': '#fdebd0',
    'RegistroTiempo': '#fadbd8',
    'Usuario': '#ebf5fb'
}

# Clase Empleado
empleado = '''Empleado
—————————
- idEmpleado: int
- nombre: str
- direccion: str
- telefono: str
- correo: str
- fechaContrato: date
- salario: float
- departamento: Dept
- proyectos: list
—————————
+ actualizarDatos()
+ asignarDepartamento()
+ asignarProyecto()
+ quitarProyecto()'''

# Clase Departamento
departamento = '''Departamento
—————————
- idDepartamento: int
- nombre: str
- gerente: Empleado
- empleados: list
—————————
+ crear()
+ editar()
+ buscar()
+ eliminar()
+ agregarEmpleado()
+ quitarEmpleado()'''

# Clase Proyecto
proyecto = '''Proyecto
—————————
- idProyecto: int
- nombre: str
- descripcion: str
- fechaInicio: date
- empleados: list
- registrosTiempo: list
—————————
+ crear()
+ editar()
+ eliminar()
+ agregarEmpleado()
+ quitarEmpleado()'''

# Clase RegistroTiempo
registro = '''RegistroTiempo
—————————
- fecha: date
- horas: float
- descripcion: str
- empleado: Empleado
- proyecto: Proyecto
—————————
+ validarHoras()
+ registrar()
+ editar()'''

# Clase Usuario
usuario = '''Usuario
—————————
- idUsuario: int
- nombreUsuario: str
- contrasenaHash: str
- rol: str
—————————
+ autenticar()
+ autorizar()'''

# Agregar nodos
g.node('Empleado', label=empleado, fillcolor=colors['Empleado'], shape='box')
g.node('Departamento', label=departamento, fillcolor=colors['Departamento'], shape='box')
g.node('Proyecto', label=proyecto, fillcolor=colors['Proyecto'], shape='box')
g.node('RegistroTiempo', label=registro, fillcolor=colors['RegistroTiempo'], shape='box')
g.node('Usuario', label=usuario, fillcolor=colors['Usuario'], shape='box')

# Agregar relaciones
# Departamento 1 -- 0..* Empleado
g.edge('Departamento', 'Empleado', label='1         0..*', dir='both', arrowhead='crow', arrowtail='none')

# Empleado 0..* -- 0..* Proyecto
g.edge('Empleado', 'Proyecto', label='0..*      0..*', dir='both', arrowhead='crow', arrowtail='crow')

# Empleado 1 -- 0..* RegistroTiempo
g.edge('Empleado', 'RegistroTiempo', label='1         0..*', dir='both', arrowhead='crow', arrowtail='none')

# Proyecto 1 -- 0..* RegistroTiempo
g.edge('Proyecto', 'RegistroTiempo', label='1         0..*', dir='both', arrowhead='crow', arrowtail='none')

# Usuario -- Empleado
g.edge('Usuario', 'Empleado', label='asociado a', style='dashed')

# Guardar
g.render('diagrama_uml_ecotech', directory='c:\\miproyectopy', cleanup=True)
print("✓ Diagrama generado: diagrama_uml_ecotech.png")
