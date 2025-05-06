from enum import Enum

# Enumeración para el tipo de planeta
class TipoPlaneta(Enum):
    GASEOSO = 1
    TERRESTRE = 2
    ENANO = 3

class Planeta:
    def __init__(self, nombre=None, cantidad_satelites=0, masa=0.0, volumen=0.0, diametro=0, distancia_sol=0, tipo=TipoPlaneta.TERRESTRE, es_observable=False):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol  # en kilómetros
        self.tipo = tipo
        self.es_observable = es_observable

    def imprimir(self):
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidad_satelites}")
        print(f"Masa del planeta = {self.masa}")
        print(f"Volumen del planeta = {self.volumen}")
        print(f"Diámetro del planeta = {self.diametro}")
        print(f"Distancia al sol = {self.distancia_sol}")
        print(f"Tipo de planeta = {self.tipo.name}")
        print(f"Es observable = {self.es_observable}")

    def calcular_densidad(self):
        if self.volumen == 0:
            return 0
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        UA = 149597870  # Km
        limite = 3.4 * UA
        return self.distancia_sol > limite

# Método main
if __name__ == "__main__":
    p1 = Planeta("Tierra", 1, 5.9736e24, 1.08321e12, 12742, 150000000, TipoPlaneta.TERRESTRE, True)
    p1.imprimir()
    print("Densidad del planeta =", p1.calcular_densidad())
    print("Es planeta exterior =", p1.es_planeta_exterior())
    print()

    p2 = Planeta("Júpiter", 79, 1.899e27, 1.4313e15, 139820, 750000000, TipoPlaneta.GASEOSO, True)
    p2.imprimir()
    print("Densidad del planeta =", p2.calcular_densidad())
    print("Es planeta exterior =", p2.es_planeta_exterior())
