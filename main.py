# Cear clase

class Socio:
    def __init__(self, nombre, numero_socio, al_dia):
        self.nombre = nombre
        self.numero_socio = numero_socio
        self.al_dia = al_dia
        self.visitas = 0

    def registrar_visita(self):
        self.visitas += 1

    def puede_entrar(self):
        return self.al_dia


# Crear tres socios
socio1 = Socio("Juan Pérez", 101, True)
socio2 = Socio("María González", 102, False)
socio3 = Socio("Pedro Soto", 103, True)

# Registrar visitas
socio1.registrar_visita()
socio1.registrar_visita()

socio2.registrar_visita()

socio3.registrar_visita()
socio3.registrar_visita()
socio3.registrar_visita()

# Consultar y mostrar resultados
socios = [socio1, socio2, socio3]

for socio in socios:
    print("-------------------------")
    print("Nombre:", socio.nombre)
    print("Número de socio:", socio.numero_socio)
    print("Visitas:", socio.visitas)

    if socio.puede_entrar():
        print("Puede entrar: Sí")
    else:
        print("Puede entrar: No")

