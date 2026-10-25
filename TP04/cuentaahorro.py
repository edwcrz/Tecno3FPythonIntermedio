# Cuenta Ahorro
# Herencia y Polimorfismo
"""
Cuenta Ahorro:
implementa Extraer(monto): permite retirar únicamente si monto <= Saldo.
agrega el método propio Aplicar_Interes(): suma al saldo un interés del 0,1% (Tasa = 0,001)
"""
# herencia de Cuenta Bancaria
from cuentabancaria import CuentaBancaria as cb
      
class CuentaAhorro(cb):

    def __init__(self, titular, cbu, saldo, tasa = 0.001, comision = 0, numero_ca = 12341234):
        super().__init__(titular, cbu, saldo)   
        # la clase hija CuentaAhorro va extender o heredar de cuenta Bancaria.
        # exiende con 2 atributos unicos: interes y numero_ca
        self._tasa = tasa
        self._comision = comision
        self.__numero_ca = numero_ca

    @property
    def tasa(self):
        return self._tasa

    @tasa.setter 
    def tasa(self, tasa):
        if tasa < 0:
            raise ValueError("la tasa de interes ingresado debe ser mayor o igual a 0")
        else:
            self._tasa = tasa

    @property
    def comision(self):
        return self._comision

    @comision.setter
    def comision(self, comision):
        if comision < 0:
            raise ValueError("la comision ingresada debe ser mayor o igual a 0")
        else:
            self._comision = comision

    @property
    def numero_ca(self):
        return self.__numero_ca

    @numero_ca.setter
    def numero_ca(self, numero_cuenta_ca):
        if numero_cuenta_ca < 0:
            raise ValueError("el numero de cuenta ca debe ser mayor o igual a 0")
        else:
            self._CuentaAhorro__numero_ca = numero_cuenta_ca

    def aplicar_interes(self):
        interes = self._saldo * self._tasa
        self._saldo += interes
        print (f" el saldo con intereses es {self._saldo}")

    def aplicar_comision(self):
        self._saldo -= self._comision
        print (f" el saldo al aplicar la comision de la operacion es: ${self._comision}")

    def extraer(self, monto):
        super().extraer(monto)
        if monto <= 0:
            raise ValueError(f"La extraccion debe ser mayor o igual que cero")
        if monto > self._saldo + self._comision:
            raise ValueError(f"Saldo insuficiente para retirar {monto}")
        print (f"se extrajo {monto}")
        self.aplicar_comision()
        self._saldo -= monto

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError(f"el monto a depositar debe ser > 0")
        self.aplicar_comision()
        self.saldo += monto

    def __str__(self):
        return f"{super().__str__()} | Interes: ${self._tasa:.2f} | Comision: ${self._comision:.2f} | Numero_ca: {self._CuentaAhorro__numero_ca:.2f}"
