# Cuenta Cheque
"""
Cuenta Cheque:
Recibe un Costo_Emision fijo por Cheque/Extraccion (por defecto $50).
Sobreescribe Extraer(Monto): Descuenta el monto solicitado más el costo administrativo por emisión dle cheque($50).
"""
# herencia de Cuenta Bancaria
from cuentabancaria import CuentaBancaria as cb
      
class CuentaCheque(cb):
    def __init__(self, titular, cbu, saldo, costo_emision = 50):
        super().__init__(titular, cbu, saldo)
        self._costo_emision = costo_emision
    
    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("La extraccion debe ser mayor o igual que cero")
        if monto > self._saldo+self._costo_emision:
            raise ValueError("El monto que desdea extraer mas el costo administrativo por emision del cheque de ${self._cosco_emision} es superior al saldo")
        self._saldo -= (monto + self._costo_emision)