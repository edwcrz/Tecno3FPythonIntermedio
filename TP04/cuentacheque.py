# Cuenta Cheque
"""
Cuenta Cheque:
Recibe un Costo_Emision fijo por Cheque/Extraccion (por defecto $50).
Sobreescribe Extraer(Monto): Descuenta el monto solicitado más el costo administrativo por emisión del cheque($50).
"""
# herencia de Cuenta Bancaria
from cuentabancaria import CuentaBancaria as cb
      
class CuentaCheque(cb):
    def __init__(self, titular, cbu, saldo, costo_emision = 50, numero_ch= 9999999):
        super().__init__(titular, cbu, saldo)
        self._costo_emision = costo_emision
        self.__numero_ch = numero_ch

    @property
    def costo_emision(self):
        return self._costo_emision

    @costo_emision.setter
    def costo_emision(self, costo_emision):
        self._costo_emision = costo_emision
        return

    @property
    def numero_ch(self):
        return self.__numero_ch

    @numero_ch.setter
    def numero_cc(self, numero_cuenta_ch):
        if numero_cuenta_ch < 0:
            raise ValueError("el numero de cuenta ch debe ser mayor o igual a 0")
        else:
            self._CuentaCheque__numero_ch = numero_cuenta_ch
          
    def aplicar_costo_emision(self):
        self._saldo -= self._costo_emision

    def extraer(self, monto):
        super().extraer(monto)
        if monto > self._saldo - self._costo_emision:
            raise ValueError(f"el actaul costo administrativo de emision ${self._costo_emision} no permite operar con el monto ${monto} por ser superior al saldo {self.saldo}")
        self.aplicar_costo_emision ()
        self._saldo -= monto

    def __str__(self):
        return f"{super().__str__()} | Costo_emision: ${self._costo_emision:.2f} | Numero_ca: {self._CuentaCheque__numero_ch:.2f}"