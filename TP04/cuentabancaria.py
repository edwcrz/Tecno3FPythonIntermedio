# Cuenta Bancaria
"""
Clase Abstracta: CuentaBancaria

Atributos:
Titular (Publico)
_CBU (Protegido, 
        de solo lectura mediante @property
_Saldo (Protegido, 
        con @property para leer y 
        @saldo.setter que lance ValueError si se intenta asignar un valor menora a cero)

Metodos:
Depositar(Monto): Suma dinero validando que el monto sea mayor a 0

__STR__(): Retorna el formato "[TipoDeCuenta] Titular: ...| Cbu: ...|Saldo: $...".

@AbstractMethod def extrae(Self, Monto): 
Método obligatorio sin cuerpo (PASS)
Cada cuenta implementará su propia regla de extracción
"""

"""
from abc import ABC, abstractmethod

class CuentaBancaria(ABC)
    def __init__(self, titular, _cbu, _saldo)
        pass
"""

from abc import ABC, abstractmethod

class CuentaBancaria (ABC):
    def __init__(self, titular, cbu, saldo):
        self.titular = titular  # publico
        self._cbu = cbu # privado
        self._saldo = saldo # privado

    @property
    def cbu(self):
        return self._cbu

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            raise ValueError("El saldo no puede ser menor que 0")
        else:
            self._saldo = saldo

    # print (CuentaBancaria)
    # print (type(CuentaBancaria))
    # print (vars(CuentaBancaria))

    def __str__(self):
        return (
            f"[{type(self).__name__}] "
            f"Titular: {self.titular} | "
            f"CBU: {self._cbu} | "
            f"Saldo: ${self._saldo:.2f}"
        )

    @abstractmethod
    def extraer (self, monto):
        pass

    def depositar(self, monto):
        if monto <= 0:
            print("el mondo a depositar debe ser > 0")
        else:
            self._saldo += monto

    def __str__(self):
        return f"{self.titular} {self._cbu} {self._saldo}"