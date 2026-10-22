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

    def __init__(self, titular, cbu, saldo, interes = 0.001, numero_ca= None):
        super().__init__(titular, cbu, saldo)   
        # la clase hija CuentaAhorro va extender o heredar de cuenta Bancaria.
        # exiende con 2 atributos unicos: interes y numero_ca
        self._interes = interes
        self.__numero_ca = numero_ca

    @property
    def cbu(self):
        return self._cbu
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def interes(self):
        return self._interes

    @property
    def numero_ca(self):
        return self.__numero_ca

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            raise ValueError("El saldo no puede ser menor que 0")
        else:
            self._saldo = saldo

    @interes.setter 
    def interes(self, interes):
        if interes < 0:
            print ("el interes ingresado debe ser mayor o igual a 0")
            return
        else:
            self._interes = interes

    @numero_ca.setter
    def numero_ca(self, numero_cuenta_ca):
        if numero_cuenta_ca < 0:
            print ("el interes ingresado debe ser mayor o igual a 0")
            return
        else:
            self._CuentaAhorro__numero_ca = numero_cuenta_ca

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("La extraccion debe ser mayor o igual que cero")
        if monto > self._saldo:
            raise ValueError("Saldo insuficiente")
        self._saldo -= monto            

    def aplicar_interes(self):
        interes_ganado = self._saldo * self._interes
        self._saldo += interes_ganado
        print (f" el saldo con intereses es {self._saldo}")

    def depositar(self, monto, comision=10):
        super().depositar(monto)   
        if monto <= 0:
            print("el mondo a depositar debe ser > 0")
        else:
            self.saldo -= comision

"""
    def __str__(self, titular, _cbu, _saldo):
            super().__str__(interes)
            return f"{self.titular} {self._cbu} {self._saldo} {self._interes}"
"""