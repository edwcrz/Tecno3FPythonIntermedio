class Coche:
    def __init__(self, marca, modelo , color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False

    def encender(self):
        if self.encendido:
            print(f"El Coche {self.marca} {self.modelo} ya esta encendido.")
        else:
            self.encendido = True
            print(f"El Coche {self.marca} {self.modelo} arrancando la maquina...")

    def apagar(self):
        self.encendido = False
        print(f"El Coche {self.marca} {self.modelo} esta apagado.")
    

coche = Coche("Fiat","Duna","Crema")
coche2 = Coche("Renault","12","Azul Metalico")

print(coche.marca)
#print(coche2.marca)
print(coche.color)
#coche.color = "Verde"

#print(coche.color)

print(coche.encendido)

coche.encender()
print(coche.encendido)
coche.encender()
coche.apagar()
print(coche.encendido)