#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generar diagrama UML de EcoTech Solutions usando matplotlib
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

fig, ax = plt.subplots(figsize=(16, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Colores
color_empleado = '#d4e6f1'
color_dept = '#d5f4e6'
color_proy = '#fdebd0'
color_reg = '#fadbd8'
color_user = '#ebf5fb'

def create_class_box(ax, x, y, width, height, title, attributes, methods, color):
    """Crear una caja de clase UML"""
    # Caja principal
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                          boxstyle="round,pad=0.1", 
                          edgecolor='#333333', facecolor=color, linewidth=2)
    ax.add_patch(box)
    
    # Título (en negrita)
    ax.text(x, y + height/2 - 0.2, title, ha='center', va='top', 
            fontsize=11, fontweight='bold', family='monospace')
    
    # Línea separadora título-atributos
    ax.plot([x - width/2 + 0.1, x + width/2 - 0.1], 
            [y + height/2 - 0.45, y + height/2 - 0.45], 
            'k-', linewidth=1)
    
    # Atributos
    attr_y = y + height/2 - 0.6
    for attr in attributes:
        ax.text(x - width/2 + 0.15, attr_y, attr, ha='left', va='top',
                fontsize=8, family='monospace')
        attr_y -= 0.2
    
    # Línea separadora atributos-métodos
    ax.plot([x - width/2 + 0.1, x + width/2 - 0.1], 
            [attr_y + 0.1, attr_y + 0.1], 
            'k-', linewidth=1)
    
    # Métodos
    method_y = attr_y - 0.1
    for method in methods:
        ax.text(x - width/2 + 0.15, method_y, method, ha='left', va='top',
                fontsize=8, family='monospace')
        method_y -= 0.15

# CLASE EMPLEADO (superior izquierda)
emp_attrs = [
    '- idEmpleado: int',
    '- nombre: str',
    '- direccion: str',
    '- telefono: str',
    '- correo: str',
    '- fechaContrato: date',
    '- salario: float',
]
emp_methods = [
    '+ actualizarDatos()',
    '+ asignarDepartamento()',
    '+ asignarProyecto()',
    '+ quitarProyecto()',
]
create_class_box(ax, 1.5, 7, 2, 2.8, 'Empleado', emp_attrs, emp_methods, color_empleado)

# CLASE DEPARTAMENTO (superior centro)
dept_attrs = [
    '- idDepartamento: int',
    '- nombre: str',
    '- gerente: Empleado',
    '- empleados: list',
]
dept_methods = [
    '+ crear()',
    '+ editar()',
    '+ buscar()',
    '+ eliminar()',
    '+ agregarEmpleado()',
    '+ quitarEmpleado()',
]
create_class_box(ax, 5, 7, 2.2, 2.8, 'Departamento', dept_attrs, dept_methods, color_dept)

# CLASE PROYECTO (superior derecha)
proy_attrs = [
    '- idProyecto: int',
    '- nombre: str',
    '- descripcion: str',
    '- fechaInicio: date',
    '- empleados: list',
]
proy_methods = [
    '+ crear()',
    '+ editar()',
    '+ eliminar()',
    '+ agregarEmpleado()',
    '+ quitarEmpleado()',
]
create_class_box(ax, 8.5, 7, 2, 2.6, 'Proyecto', proy_attrs, proy_methods, color_proy)

# CLASE REGISTRO TIEMPO (inferior centro)
reg_attrs = [
    '- fecha: date',
    '- horas: float',
    '- descripcion: str',
    '- empleado: Empleado',
    '- proyecto: Proyecto',
]
reg_methods = [
    '+ validarHoras()',
    '+ registrar()',
    '+ editar()',
]
create_class_box(ax, 5, 3, 2, 2.2, 'RegistroTiempo', reg_attrs, reg_methods, color_reg)

# CLASE USUARIO (inferior izquierda)
user_attrs = [
    '- idUsuario: int',
    '- nombreUsuario: str',
    '- contrasenaHash: str',
    '- rol: str',
]
user_methods = [
    '+ autenticar()',
    '+ autorizar()',
]
create_class_box(ax, 1.5, 2.5, 2, 1.8, 'Usuario', user_attrs, user_methods, color_user)

# RELACIONES
# Departamento -> Empleado (1 a 0..*)
arrow1 = FancyArrowPatch((4.1, 6.8), (2.4, 6.2),
                        arrowstyle='<-', mutation_scale=20, linewidth=1.5, color='#333333')
ax.add_patch(arrow1)
ax.text(3.2, 6.6, '1', fontsize=9, fontweight='bold')
ax.text(2.8, 6.4, '0..*', fontsize=9, fontweight='bold')

# Empleado -> Proyecto (0..* a 0..*)
arrow2 = FancyArrowPatch((2.8, 6.8), (7.2, 6.8),
                        arrowstyle='<->', mutation_scale=20, linewidth=1.5, color='#333333')
ax.add_patch(arrow2)
ax.text(5, 7.0, 'participa en (0..* a 0..*)', fontsize=8, ha='center')

# Empleado -> RegistroTiempo (1 a 0..*)
arrow3 = FancyArrowPatch((2, 5.4), (4.2, 4.2),
                        arrowstyle='<-', mutation_scale=20, linewidth=1.5, color='#333333')
ax.add_patch(arrow3)
ax.text(2.8, 4.9, '1', fontsize=9, fontweight='bold')
ax.text(4.0, 4.4, '0..*', fontsize=9, fontweight='bold')

# Proyecto -> RegistroTiempo (1 a 0..*)
arrow4 = FancyArrowPatch((8, 5.4), (5.8, 4.2),
                        arrowstyle='<-', mutation_scale=20, linewidth=1.5, color='#333333')
ax.add_patch(arrow4)
ax.text(7.2, 4.9, '1', fontsize=9, fontweight='bold')
ax.text(5.8, 4.4, '0..*', fontsize=9, fontweight='bold')

# Usuario -> Empleado (asociación)
arrow5 = FancyArrowPatch((2.5, 3.7), (1.8, 5.6),
                        arrowstyle='--', mutation_scale=15, linewidth=1.5, 
                        color='#333333', linestyle='dashed')
ax.add_patch(arrow5)
ax.text(2.8, 4.7, 'asociado a', fontsize=8, ha='left', style='italic')

# Título
ax.text(5, 9.5, 'EcoTech Solutions - Diagrama de Clases UML', 
        fontsize=16, fontweight='bold', ha='center')

plt.tight_layout()
plt.savefig('c:\\miproyectopy\\diagrama_uml_ecotech.png', dpi=150, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print("✓ Diagrama generado: diagrama_uml_ecotech.png")
print("✓ Ubicación: c:\\miproyectopy\\diagrama_uml_ecotech.png")
