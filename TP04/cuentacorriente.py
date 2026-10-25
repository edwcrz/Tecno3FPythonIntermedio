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
    def __init__(self, titular, cbu, saldo, limite_descubierto : float = 500, comision : float =0, numero_cc : int = 444555666):
        super().__init__(titular, cbu, saldo)
        self._limite_descubierto = limite_descubierto
        self._comision = comision
        self.__numero_cc = numero_cc

    @property
    def limite_descubierto(self):
        return self._limite_descubierto

    @limite_descubierto.setter
    def limite_descubierto(self, limite_descubierto):
        if limite_descubierto < 0:
            raise ValueError("el limite descubierto ingresado debe ser mayor o igual a 0")
        else:
            self._limite_descubierto = limite_descubierto

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
    def numero_cc(self):
        return self.__numero_cc

    @numero_cc.setter
    def numero_cc(self, numero_cuenta_cc):
        if numero_cuenta_cc < 0:
            raise ValueError("el numero de cuenta cc debe ser mayor o igual a 0")
        else:
            self._CuentaCorriente__numero_cc = numero_cuenta_cc

    def modificar_limite_descubierto(self, limite_descubierto):
        self._limite_descubierto = limite_descubierto
        print (f" el nuevo limite descubierto es: {self._limite_descubierto}")

    def aplicar_comision(self):
        self._saldo -= self._comision

    def extraer(self, monto):
        super().extraer(monto)
        if monto <=0:
            print (f"ValueError el monto ${monto} que se ingreso es menor o igual a 0")
        if monto > self._saldo + self._limite_descubierto + self._comision:
            print (f"el monto {monto} que ingreso es mayor al saldo ${self._saldo} incluyendo un limite descubierto ${self._limite_descubierto} y la comision por la operacion ${self._comision}")
        else:
            self.aplicar_comision(self._comision)
            self._saldo -= monto

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("el mondo a depositar debe ser > 0")
        self.aplicar_comision(self._comision)
        self.saldo += monto

    def __str__(self):
        return f"{super().__str__()} | Limite Descubierto: ${self._limite_descubierto:.2f} | Comision: ${self._comision:.2f} | Numero_cc: {self._CuentaCorriente__numero_cc:.2f}" 
