"""
EcoTech Solutions - Sistema de Gestión OOP Seguro
Módulo Principal: Implementación de Clases UML

Curso: POO Seguro - INACAP Valparaíso
Evaluación Sumativa 1
"""

from datetime import date
import hashlib
import hmac
from typing import List, Optional


class Empleado:
    """
    Representa un empleado de la empresa EcoTech Solutions.
    
    Atributos:
        idEmpleado (int): Identificador único del empleado
        nombre (str): Nombre completo del empleado
        direccion (str): Dirección del empleado
        telefono (str): Número de teléfono de contacto
        correo (str): Correo electrónico del empleado
        fechaContrato (date): Fecha de inicio del contrato
        salario (float): Salario mensual del empleado
        departamento (Departamento): Departamento al que pertenece
        proyectos (List[Proyecto]): Proyectos asignados
    """
    
    def __init__(self, idEmpleado: int, nombre: str, direccion: str,
                 telefono: str, correo: str, fechaContrato: date, salario: float):
        """Inicializa un empleado con sus datos básicos."""
        self.idEmpleado = idEmpleado
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fechaContrato = fechaContrato
        self.salario = salario
        self.departamento: Optional['Departamento'] = None
        self.proyectos: List['Proyecto'] = []
    
    def actualizarDatos(self, **kwargs) -> bool:
        """
        Actualiza los datos del empleado.
        
        Args:
            **kwargs: Pares clave-valor de atributos a actualizar
            
        Returns:
            bool: True si la actualización fue exitosa
        """
        atributos_permitidos = {
            'nombre', 'direccion', 'telefono', 'correo', 'salario'
        }
        
        for clave, valor in kwargs.items():
            if clave in atributos_permitidos:
                setattr(self, clave, valor)
            else:
                print(f"Atributo {clave} no permitido")
                return False
        
        return True
    
    def asignarDepartamento(self, departamento: 'Departamento') -> bool:
        """
        Asigna el empleado a un departamento específico.
        
        Args:
            departamento (Departamento): Departamento a asignar
            
        Returns:
            bool: True si la asignación fue exitosa
        """
        if departamento is None:
            print("Error: Departamento no válido")
            return False
        
        if self.departamento is departamento:
            return False

        if self.departamento is not None and self in self.departamento.empleados:
            self.departamento.empleados.remove(self)

        self.departamento = departamento
        if self not in departamento.empleados:
            departamento.empleados.append(self)
        
        return True
    
    def asignarProyecto(self, proyecto: 'Proyecto') -> bool:
        """
        Asigna un proyecto al empleado.
        
        Args:
            proyecto (Proyecto): Proyecto a asignar
            
        Returns:
            bool: True si la asignación fue exitosa
        """
        if proyecto is None:
            print("Error: Proyecto no válido")
            return False
        
        if proyecto not in self.proyectos:
            self.proyectos.append(proyecto)
            if self not in proyecto.empleados:
                proyecto.empleados.append(self)
        
        return True
    
    def quitarProyecto(self, proyecto: 'Proyecto') -> bool:
        """
        Remueve un proyecto del empleado.
        
        Args:
            proyecto (Proyecto): Proyecto a remover
            
        Returns:
            bool: True si la remoción fue exitosa
        """
        if proyecto in self.proyectos:
            self.proyectos.remove(proyecto)
            if self in proyecto.empleados:
                proyecto.empleados.remove(self)
            return True
        
        return False
    
    def __str__(self) -> str:
        """Representación en string del empleado."""
        return (f"Empleado(id={self.idEmpleado}, nombre='{self.nombre}', "
                f"correo='{self.correo}', salario={self.salario})")


class Departamento:
    """
    Representa un departamento de EcoTech Solutions.
    
    Atributos:
        idDepartamento (int): Identificador único del departamento
        nombre (str): Nombre del departamento
        gerente (Empleado): Gerente responsable del departamento
        empleados (List[Empleado]): Lista de empleados del departamento
    """
    
    def __init__(self, idDepartamento: int, nombre: str):
        """Inicializa un departamento."""
        self.idDepartamento = idDepartamento
        self.nombre = nombre
        self.gerente: Optional[Empleado] = None
        self.empleados: List[Empleado] = []
    
    def crear(self) -> bool:
        """
        Crea/registra el departamento en el sistema.
        
        Returns:
            bool: True si la creación fue exitosa
        """
        if not self.nombre:
            print("Error: Nombre de departamento requerido")
            return False
        
        print(f"Departamento '{self.nombre}' creado exitosamente")
        return True
    
    def editar(self, **kwargs) -> bool:
        """
        Edita los datos del departamento.
        
        Args:
            **kwargs: Pares clave-valor de atributos a actualizar
            
        Returns:
            bool: True si la edición fue exitosa
        """
        atributos_permitidos = {'nombre', 'gerente'}
        
        for clave, valor in kwargs.items():
            if clave in atributos_permitidos:
                setattr(self, clave, valor)
            else:
                print(f"Atributo {clave} no permitido")
                return False
        
        return True
    
    def buscar(self, criterio: str, valor: str) -> Optional[Empleado]:
        """
        Busca un empleado dentro del departamento.
        
        Args:
            criterio (str): Campo por el que buscar (nombre, correo, etc)
            valor (str): Valor a buscar
            
        Returns:
            Optional[Empleado]: Empleado encontrado o None
        """
        for empleado in self.empleados:
            if hasattr(empleado, criterio) and getattr(empleado, criterio) == valor:
                return empleado
        
        return None
    
    def eliminar(self) -> bool:
        """
        Elimina el departamento del sistema.
        
        Returns:
            bool: True si la eliminación fue exitosa
        """
        if self.empleados:
            print("Error: No se puede eliminar un departamento con empleados")
            return False
        
        print(f"Departamento '{self.nombre}' eliminado")
        return True
    
    def agregarEmpleado(self, empleado: Empleado) -> bool:
        """
        Agrega un empleado al departamento.
        
        Args:
            empleado (Empleado): Empleado a agregar
            
        Returns:
            bool: True si la adición fue exitosa
        """
        if empleado not in self.empleados:
            return empleado.asignarDepartamento(self)
        
        return False
    
    def quitarEmpleado(self, empleado: Empleado) -> bool:
        """
        Remueve un empleado del departamento.
        
        Args:
            empleado (Empleado): Empleado a remover
            
        Returns:
            bool: True si la remoción fue exitosa
        """
        if empleado in self.empleados:
            self.empleados.remove(empleado)
            if empleado.departamento is self:
                empleado.departamento = None
            return True
        
        return False
    
    def __str__(self) -> str:
        """Representación en string del departamento."""
        return (f"Departamento(id={self.idDepartamento}, nombre='{self.nombre}', "
                f"empleados={len(self.empleados)})")


class Proyecto:
    """
    Representa un proyecto de EcoTech Solutions.
    
    Atributos:
        idProyecto (int): Identificador único del proyecto
        nombre (str): Nombre del proyecto
        descripcion (str): Descripción del proyecto
        fechaInicio (date): Fecha de inicio del proyecto
        empleados (List[Empleado]): Empleados asignados al proyecto
        registrosTiempo (List[RegistroTiempo]): Registros de tiempo del proyecto
    """
    
    def __init__(self, idProyecto: int, nombre: str, descripcion: str, fechaInicio: date):
        """Inicializa un proyecto."""
        self.idProyecto = idProyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaInicio = fechaInicio
        self.empleados: List[Empleado] = []
        self.registrosTiempo: List['RegistroTiempo'] = []
    
    def crear(self) -> bool:
        """
        Crea/registra el proyecto en el sistema.
        
        Returns:
            bool: True si la creación fue exitosa
        """
        if not self.nombre or not self.descripcion:
            print("Error: Nombre y descripción del proyecto requeridos")
            return False
        
        print(f"Proyecto '{self.nombre}' creado exitosamente")
        return True
    
    def editar(self, **kwargs) -> bool:
        """
        Edita los datos del proyecto.
        
        Args:
            **kwargs: Pares clave-valor de atributos a actualizar
            
        Returns:
            bool: True si la edición fue exitosa
        """
        atributos_permitidos = {'nombre', 'descripcion', 'fechaInicio'}
        
        for clave, valor in kwargs.items():
            if clave in atributos_permitidos:
                setattr(self, clave, valor)
            else:
                print(f"Atributo {clave} no permitido")
                return False
        
        return True
    
    def eliminar(self) -> bool:
        """
        Elimina el proyecto del sistema.
        
        Returns:
            bool: True si la eliminación fue exitosa
        """
        if self.registrosTiempo:
            print("Error: No se puede eliminar un proyecto con registros de tiempo")
            return False
        
        print(f"Proyecto '{self.nombre}' eliminado")
        return True
    
    def agregarEmpleado(self, empleado: Empleado) -> bool:
        """
        Agrega un empleado al proyecto.
        
        Args:
            empleado (Empleado): Empleado a agregar
            
        Returns:
            bool: True si la adición fue exitosa
        """
        if empleado not in self.empleados:
            self.empleados.append(empleado)
            empleado.asignarProyecto(self)
            return True
        
        return False
    
    def quitarEmpleado(self, empleado: Empleado) -> bool:
        """
        Remueve un empleado del proyecto.
        
        Args:
            empleado (Empleado): Empleado a remover
            
        Returns:
            bool: True si la remoción fue exitosa
        """
        if empleado in self.empleados:
            self.empleados.remove(empleado)
            empleado.quitarProyecto(self)
            return True
        
        return False
    
    def __str__(self) -> str:
        """Representación en string del proyecto."""
        return (f"Proyecto(id={self.idProyecto}, nombre='{self.nombre}', "
                f"empleados={len(self.empleados)})")


class RegistroTiempo:
    """
    Representa un registro de tiempo de trabajo.
    
    Atributos:
        fecha (date): Fecha del registro
        horas (float): Número de horas trabajadas
        descripcion (str): Descripción del trabajo realizado
        empleado (Empleado): Empleado que registró el tiempo
        proyecto (Proyecto): Proyecto en el que se trabajó
    """
    
    def __init__(self, fecha: date, horas: float, descripcion: str,
                 empleado: Empleado, proyecto: Proyecto):
        """Inicializa un registro de tiempo."""
        self.fecha = fecha
        self.horas = horas
        self.descripcion = descripcion
        self.empleado = empleado
        self.proyecto = proyecto
    
    def validarHoras(self) -> bool:
        """
        Valida que el número de horas sea válido.
        
        Returns:
            bool: True si las horas son válidas (entre 0 y 24)
        """
        if 0 < self.horas <= 24:
            return True
        
        print(f"Error: Horas inválidas ({self.horas}). Deben estar entre 0 y 24")
        return False
    
    def registrar(self) -> bool:
        """
        Registra el tiempo de trabajo.
        
        Returns:
            bool: True si el registro fue exitoso
        """
        if not self.validarHoras():
            return False

        if self not in self.proyecto.registrosTiempo:
            self.proyecto.registrosTiempo.append(self)
        else:
            print("Error: El registro ya fue registrado")
            return False

        print(f"Registro de tiempo creado: {self.empleado.nombre} - "
              f"{self.horas}h en {self.proyecto.nombre}")
        return True
    
    def editar(self, **kwargs) -> bool:
        """
        Edita los datos del registro.
        
        Args:
            **kwargs: Pares clave-valor de atributos a actualizar
            
        Returns:
            bool: True si la edición fue exitosa
        """
        atributos_permitidos = {'fecha', 'horas', 'descripcion'}
        
        if any(clave not in atributos_permitidos for clave in kwargs):
            print("Error: Atributo no permitido")
            return False

        horas_originales = self.horas
        for clave, valor in kwargs.items():
            setattr(self, clave, valor)

        if not self.validarHoras():
            self.horas = horas_originales
            if 'horas' in kwargs:
                return False
        
        return True
    
    def __str__(self) -> str:
        """Representación en string del registro."""
        return (f"RegistroTiempo(fecha={self.fecha}, horas={self.horas}, "
                f"empleado={self.empleado.nombre}, proyecto={self.proyecto.nombre})")


class Usuario:
    """
    Representa un usuario del sistema (asociado a un Empleado).
    
    Atributos:
        idUsuario (int): Identificador único del usuario
        nombreUsuario (str): Nombre de usuario para login
        contrasenaHash (str): Hash de la contraseña (nunca almacenar en texto plano)
        rol (str): Rol del usuario (admin, supervisor, empleado)
        empleado (Empleado): Empleado asociado a este usuario
    """
    
    def __init__(self, idUsuario: int, nombreUsuario: str, contrasenaHash: str, rol: str):
        """Inicializa un usuario del sistema."""
        self.idUsuario = idUsuario
        self.nombreUsuario = nombreUsuario
        self.contrasenaHash = contrasenaHash
        self.rol = rol
        self.empleado: Optional[Empleado] = None

    @staticmethod
    def generarHash(contrasena: str) -> str:
        """Genera el hash SHA-256 de una contraseña para la demostración."""
        return hashlib.sha256(contrasena.encode('utf-8')).hexdigest()
    
    def autenticar(self, nombreUsuario: str, contrasena_ingresada: str) -> bool:
        """
        Autentica un usuario verificando credenciales.
        
        Args:
            nombreUsuario (str): Nombre de usuario ingresado
            contrasena_ingresada (str): Contraseña ingresada
            
        Returns:
            bool: True si las credenciales son válidas
        """
        hash_ingresado = self.generarHash(contrasena_ingresada)
        if (self.nombreUsuario == nombreUsuario and
            hmac.compare_digest(self.contrasenaHash, hash_ingresado)):
            print(f"Usuario {nombreUsuario} autenticado exitosamente")
            return True
        
        print("Error: Credenciales inválidas")
        return False
    
    def autorizar(self, recurso: str) -> bool:
        """
        Verifica si el usuario tiene autorización para acceder a un recurso.
        
        Args:
            recurso (str): Recurso a acceder (reportes, configuracion, etc)
            
        Returns:
            bool: True si el usuario está autorizado
        """
        permisos_por_rol = {
            'admin': ['reportes', 'configuracion', 'usuarios', 'empleados', 'proyectos'],
            'supervisor': ['reportes', 'empleados', 'proyectos'],
            'empleado': ['reportes']
        }
        
        permisos = permisos_por_rol.get(self.rol, [])
        
        if recurso in permisos:
            print(f"Usuario {self.nombreUsuario} autorizado para {recurso}")
            return True
        
        print(f"Error: Usuario {self.nombreUsuario} no autorizado para {recurso}")
        return False
    
    def __str__(self) -> str:
        """Representación en string del usuario."""
        return f"Usuario(id={self.idUsuario}, nombre='{self.nombreUsuario}', rol='{self.rol}')"


# ============= EJEMPLO DE USO =============

if __name__ == "__main__":
    print("=" * 60)
    print("EcoTech Solutions - Sistema OOP Seguro")
    print("=" * 60)
    
    # Crear un departamento
    dept_desarrollo = Departamento(1, "Desarrollo de Software")
    dept_desarrollo.crear()
    
    # Crear empleados
    emp1 = Empleado(101, "Juan Pérez", "Calle Principal 123",
                   "+56912345678", "juan.perez@ecotech.cl",
                   date(2022, 1, 15), 3500000)
    emp2 = Empleado(102, "María García", "Calle Secundaria 456",
                   "+56987654321", "maria.garcia@ecotech.cl",
                   date(2021, 6, 1), 3800000)
    
    # Asignar empleados al departamento
    dept_desarrollo.agregarEmpleado(emp1)
    dept_desarrollo.agregarEmpleado(emp2)
    
    print(f"\nDepartamento: {dept_desarrollo}")
    print(f"Empleados: {[str(e) for e in dept_desarrollo.empleados]}")
    
    # Crear un proyecto
    proyecto_sostenible = Proyecto(501, "Sistema de Gestión Sostenible",
                                  "Aplicación para monitoreo de recursos ecológicos",
                                  date(2024, 1, 1))
    proyecto_sostenible.crear()
    
    # Asignar empleados al proyecto
    proyecto_sostenible.agregarEmpleado(emp1)
    proyecto_sostenible.agregarEmpleado(emp2)
    
    print(f"\nProyecto: {proyecto_sostenible}")
    
    # Crear registros de tiempo
    hoy = date.today()
    registro1 = RegistroTiempo(hoy, 8.5, "Desarrollo de módulo autenticación",
                              emp1, proyecto_sostenible)
    
    if registro1.validarHoras():
        registro1.registrar()
    
    # Crear usuario y verificar autorización
    usuario1 = Usuario(1001, "jperez", Usuario.generarHash("contraseña"), "supervisor")
    usuario1.empleado = emp1
    usuario1.autenticar("jperez", "contraseña")
    usuario1.autorizar("reportes")
    usuario1.autorizar("configuracion")
    
    print("\n" + "=" * 60)
    print("Demostración completada exitosamente")
    print("=" * 60)
