# Sistema Bancario POO
"""
1- Clase Abstacta: CuentaBancaria (ABC)
    Atributos protegidos: _titular, _cbu, _saldo
    Decoradores: @property, @saldo.setter con validaciones
    Metodo Concreto: depositar(self, monto) y __str__(self)
    Metodo Abstracto: (@abstractmethod): extraer(monto)

2- Subclases que heredan y aplican Polimorfismo:
    CuentaAhorro:       extraer(monto) solo si hay saldo suficiente y no permite sobregiro.
                        Agrega aplicar_interes() con tasa fija (ej: 0,1% --> 0,001)
    Cuenta corriente:   agrega limite_descubierto. Permiete extraer hasta agotar el saldo + descubierto
    CuentaCheque:       cobra una comision administrativa fija por cada extraccion exitosa
"""
"""
en el TP04 debemos tener el objetivo de practicar
Programación orientada a objetos
Clases: se define
Objetos: se define
Encapsulamiento: acceder a los atributos privados (_datos) a través de métodos públicos (funciones) únicamente
    publico         self.atributopublico
    privado         self._atributoprivado
    name mangling   self.__atributonamemangling # evitar una colision cuando estamos heredando
property modifica la funcion para que se convierta en un atributo
el callable
Cualquier objeto de una clase personalizada que incluya el método especial __call__.
Puedes verificar si un objeto se puede llamar o no utilizando la función nativa callable():


"""
# importo las clases
from cuentaahorro import CuentaAhorro as ca
from cuentacorriente import CuentaCorriente as cc
from cuentacheque import CuentaCheque as ch

cuentaca = ca(
            "Eduardo Cruz",
            "1234567890123456789012",
            100000,
            0.001,
            9453211234122
)

# Encapsulamiento 
 
print("Objeto completo:")
print(cuentaca)

print("\nTipo de objeto:")
print(type(cuentaca))

print("\nVariables de objeto:")
print(vars(cuentaca))

print("\nAtributos y Objetos de la clase CuentaAhorro:")
print(dir(cuentaca))

print("\nTitular es publico, se lo llama sin getter:")
print(cuentaca.titular)   # titular es publico y no permite armar un getter

# indebido
print("\nImprimo CBU metodo indebido:")
print(cuentaca._cbu)

# correcto
print("\nImprimo CBU metodo correcto:")
print(cuentaca.cbu) ## ese cbu es el metodo con property.

print("\nImprimo Saldo metodo indebido sin getter:")
print(cuentaca._saldo)

print("\nImprimo Saldo metodo correcto con getter:")
print(cuentaca.saldo) ## cada property lleva su @property (yo pensaba que iba uno al principio)

print("\nImprimo Interes metodo indebido sin getter:")
print(cuentaca._interes)

print("\nImprimo Interes metodo correcto con getter:")
print(cuentaca.interes)

print("\nImprimo numero_ca metodo indebido sin getter:")
print(cuentaca._CuentaAhorro__numero_ca)

print("\nImprimo numero_ca metodo correcto con getter:")
print(cuentaca.numero_ca)

interes_ingresado = float(input("ingrese un interes para la cuenta ahorro mayor o igual a 0 :\n"))
# print(type(interes_ingresado))
cuentaca.interes = interes_ingresado
# cuentaca.interes = 0.1
print(cuentaca.interes)

numero_cuenta_ca_ingresado = int(input("ingrese el numero de cuenta ahorro de 12 digitos decimal mayor a 0 :\n"))
# print(type(numero_cuenta_ca_ingresado))
cuentaca.numero_ca = numero_cuenta_ca_ingresado
# cuentaca.numero_ca = 555444999222
print(cuentaca.numero_ca)

print(type(callable(cuentaca.numero_ca)))
if callable(cuentaca.numero_ca):
    print(f"el objeto {cuentaca.numero_ca} eS callable")
else:
    print(f"el objeto {cuentaca.numero_ca} es NO callable")


monto_ingresado = float(input("ingrese un monto a depositar decimal mayor a 0 :\n"))
cuentaca.depositar(monto_ingresado, comision=10)
print(cuentaca.saldo)

"""
print(cuentaca)


print("\nAtributos y Objetos de mi clase")
print(dir(ca))

print("\nNumeroca:")
print(cuenta._CuentaAhorro__numeroca)


print (cuenta.titular)


print("\nDespués de extraer:")
cuenta.extraer(15000)
print(cuenta._saldo)

print("\nDespués de aplicar interés:")
cuenta.aplicar_interes()
print(cuenta)


cuenta.depositar(20000)
print("Después del depósito:")
print(cuenta)


cuenta.extraer(15000)
print("Después de la extracción:")
print(cuenta)

cuenta.aplicar_interes()
print("Después de aplicar el interés:")
print(cuenta)

# --- CASOS DE PRUEBA ---
ahorro = ca("Carlos Rossi", "285001", saldo_inicial=1000)
corriente = cc("María López", "285002", saldo_inicial=500, limite_descubierto=1000)
cheque = ch("Empresa SRL", "285003", saldo_inicial=2000, costo_emision=100)

cuentas = [ahorro, corriente, cheque]

print (cuentas[ahorro])


print("--- ESTADO INICIAL ---")
for c in cuentas:
    print(c)

print("\n--- PRUEBA POLIMÓRFICA DE EXTRACCIONES ($800) ---")
for c in cuentas:
    c.extraer(800)
"""
"""
print("\n--- PRUEBA DE INTERÉS EN CUENTA AHORRO ---")
ahorro.aplicar_interes()
"""

"""
print("\n--- PRUEBA DE LECTURA Y PROTECCIÓN (@property) ---")
print(f"Saldo consultado: ${ahorro.saldo}")
#ahorro.saldo = -500  # Descomentar para verificar que arroja ValueError
#ahorro.cbu = "999"   # Descomentar para verificar que arroja AttributeError (solo lectura)
"""
