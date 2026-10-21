class Vehiculo:
    def __init__(self,marca,modelo, velocidad_maxima = 50):
        self.marca = marca
        self.modelo = modelo
        self._velocidad = 0
        self.__numero_chasis = "ABC123"
        self._velocidad_maxima = velocidad_maxima

    @property
    def velocidad_maxima(self):
        return self._velocidad_maxima

    @velocidad_maxima.setter
    def velocidad_maxima(self,valor):
        if valor <= 0:
            print("La velocidad maxima debe ser mayor a 0.")
            return
        self._velocidad_maxima = valor

    def acelerar(self, incremento):
            self._velocidad = min(self._velocidad + incremento, self._velocidad_maxima)
            print(f"{self.marca} {self.modelo} acelera a {self._velocidad} km/h.")

auto = Vehiculo("Toyota","Corolla") #instancia

"""
print(auto.marca)
print(auto.modelo)
print(auto._velocidad) #si bien se puede, rompe la convencion NO HACERLO
auto._Vehiculo__numero_chasis = "JBL203"
print(auto._Vehiculo__numero_chasis)
#print(dir(auto))

print(auto.velocidad_maxima)

auto.velocidad_maxima = 400

print(auto.velocidad_maxima)
"""

class Moto(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima=90):
                super().__init__(marca, modelo, velocidad_maxima)
    
    def acelerar(self, incremento):
        # Una moto acelera el doble de rápido por su menor peso
        incremento_moto = incremento * 1.5
        self._velocidad = min(self._velocidad + incremento_moto, self._velocidad_maxima)
        print(f"{self.marca} {self.modelo} sale disparada a {self._velocidad:.1f} km/h.")

moto = Moto("Yamaha", "MT-03", velocidad_maxima=100)
"""
print(moto.velocidad_maxima)
moto.velocidad_maxima = 150
print(moto.velocidad_maxima)"""

class Auto(Vehiculo): #esto es el mapa
    def __init__(self,marca,modelo, velocidad_maxima = 75, cantidad_puertas = 4):
        super().__init__(marca,modelo,velocidad_maxima)
        self.cantidad_puertas = cantidad_puertas

    def tocar_bocina(self):
        print(f"{self.marca}: Hace pi pi")

#mi_auto = Auto("Peugeot","208" ,cantidad_puertas=5)

"""
print(mi_auto.velocidad_maxima)
mi_auto.tocar_bocina()
print(f"El {mi_auto.marca} {mi_auto.modelo} tiene {mi_auto.cantidad_puertas}")"""


class Camion(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima=90, capacidad_toneladas=10):
        super().__init__(marca, modelo, velocidad_maxima)
        self.capacidad_toneladas = capacidad_toneladas

    def acelerar(self, incremento):
        # Acelera con menor respuesta por la carga
        incremento_pesado = incremento * 0.5
        self._velocidad = min(self._velocidad + incremento_pesado, self._velocidad_maxima)
        print(f"Camión {self.marca} cargado con {self.capacidad_toneladas}t acelera despacio a {self._velocidad:.1f} km/h.")


mi_auto = Auto("Peugeot", "208", velocidad_maxima=120, cantidad_puertas=5)
mi_moto = Moto("Yamaha", "MT-03", velocidad_maxima=160)
mi_camion = Camion("Scania", "R450", velocidad_maxima=90, capacidad_toneladas=25)

"""
flota = [mi_auto, mi_moto, mi_camion]

for vehiculo in flota:
    vehiculo.acelerar(30)"""