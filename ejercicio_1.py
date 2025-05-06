class Persona:
    def __init__(self, nombre, apellidos, númeroDocumentoIdentidad, añoNacimiento):
        self.nombre = nombre
        self.apellidos = apellidos
        self.númeroDocumentoIdentidad = númeroDocumentoIdentidad
        self.añoNacimiento = añoNacimiento

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Apellidos:", self.apellidos)
        print("Número de identidad:", self.númeroDocumentoIdentidad)
        print("Año de nacimiento:", self.añoNacimiento)
        print()

# Método principal (main)
if __name__ == "__main__":
    persona1 = Persona("Pedro", "Pérez", "1053121010", 1998)
    persona2 = Persona("Luis", "León", "1053223344", 2001)

    persona1.imprimir()
    persona2.imprimir()

