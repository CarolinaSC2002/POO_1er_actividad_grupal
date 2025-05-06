class Persona:
    def __init__(self, nombre, apellido, documento, anio_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.anio_nacimiento = anio_nacimiento

    def imprimir_datos(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Documento de identidad:", self.documento)
        print("Año de nacimiento:", self.anio_nacimiento)
        print()

# Método principal (main)
if __name__ == "__main__":
    persona1 = Persona("Ana", "Torres", "12345678", 1990)
    persona2 = Persona("Luis", "Martínez", "87654321", 1985)

    persona1.imprimir_datos()
    persona2.imprimir_datos()
