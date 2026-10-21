from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo,velocidad_maxima = 50):
        self.marca = marca
        self.modelo = modelo
        self._velocidad = 0
        self._velocidad_maxima = velocidad_maxima
        self.__numero_chasis = "CH-98432"

    @property
    def velocidad_maxima(self):
        return self._velocidad_maxima

    @velocidad_maxima.setter
    def velocidad_maxima(self, valor):
        if valor <= 0:
            raise ValueError("La velocidad máxima debe ser positiva.")
        self._velocidad_maxima = valor

    def acelerar(self, incremento):
        self._velocidad = min(self._velocidad + incremento, self._velocidad_maxima)
        print(f"{self.marca} {self.modelo} acelera a {self._velocidad} km/h.")

    def __str__(self):
        return f"{self.marca} {self.modelo}"

    @abstractmethod
    def inspeccion_tecnica(self):
        """Cada subclase DEBE implementar sus propios controles."""
        pass

class Moto(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima=90):
            super().__init__(marca, modelo, velocidad_maxima)

    def acelerar(self, incremento):
        incremento_moto = incremento * 1.5
        self._velocidad = min(self._velocidad + incremento_moto, self._velocidad_maxima)
        print(f"{self.marca} {self.modelo} sale disparada a {self._velocidad:.1f} km/h.")

    def inspeccion_tecnica(self):
        print(f"VTV Moto ({self.marca}): Revisión de frenos, cadena y luces reglamentarias.")


class Auto(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima = 75,cantidad_puertas=4):
        super().__init__(marca, modelo,velocidad_maxima)
        self.cantidad_puertas = cantidad_puertas

    def tocar_bocina(self):
        print(f"El {self.marca} hace: ¡Pip, pip!")

    def inspeccion_tecnica(self):
        print(f"VTV Auto ({self.marca}): Control de {self.cantidad_puertas} cinturones, matafuegos y gases.")


class Camion(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima=90, capacidad_toneladas=10):
        super().__init__(marca, modelo, velocidad_maxima)
        self.capacidad_toneladas = capacidad_toneladas

    def acelerar(self, incremento):
        incremento_pesado = incremento * 0.5
        self._velocidad = min(self._velocidad + incremento_pesado, self._velocidad_maxima)
        print(f"Camión {self.marca} cargado con {self.capacidad_toneladas}t acelera despacio a {self._velocidad:.1f} km/h.")

    def inspeccion_tecnica(self):
        print(f"VTV Camión ({self.marca}): Inspección de tacógrafo y soporte para {self.capacidad_toneladas} toneladas.")

#vehiculo_generico = Vehiculo("Generico", "X1")
#print(vehiculo_generico.describir())

flota = [
    Auto("Peugeot", "208", cantidad_puertas=5),
    Moto("Yamaha", "MT-03"),
    Camion("Scania", "R450", capacidad_toneladas=20)
]

for v in flota:
    v.inspeccion_tecnica()


for v in flota:
    print(v)