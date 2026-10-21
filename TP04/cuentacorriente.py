# Cuenta Corriente

"""
Cuenta Correinte:
Recibe por parámetro un Límite_Descubierto (por defecto $500).
Sobreescribe Extraer(Monto): Permite retirar dinero incluso si el saldo no alcanza, 
siempre que no supere saldo + Limite_Descubierto.
"""
# herencia de Cuenta Bancaria
from cuentabancaria import CuentaBancaria as cb
      
class CuentaCorriente(cb):
    def __init__(self, titular, cbu, saldo, limite_descubierto = 500):
        super().__init__(titular, cbu, saldo)
        self._limite_descubierto = limite_descubierto
    
    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("La extraccion debe ser mayor o igual que cero")
        if monto > self._saldo+self._limite_descubierto:
            raise ValueError(f"El monto que pretende extraer supera el lìmite de ${self._limite_descubierto} de descubierto")
        self._saldo -= monto            

    def modificar_limite_descubierto(self, limite_descubierto):
        self._limite_descubierto = limite_descubierto
        print (f" el nuevo limite descubierto es: {self._limite_descubierto}")