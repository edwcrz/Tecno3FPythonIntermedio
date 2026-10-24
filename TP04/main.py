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

# instancio cuenta ca
cuentaca = ca(
            "Eduardo Cruz",             # titular
            "1234567890123456789012",   # cbu
            100000,                     # saldo
            0.01,                       # tasa
            0.00,                       # comision
            123456789012)               # numero_ca

"""
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

"""
"""

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
"""
print ("opero sobre la cuentaca")
print (f"detalles de la cuentaca {cuentaca}")

print ("operacion depositar")

flag = False

while flag == False:
    try:    
        monto_ingresado = float(input("ingrese un monto a depositar decimal mayor a 0 :\n"))
    except ValueError as ve:
        print (f"Value Error. Error de {ve}. el monto a depositar debe ser un numero decimal mayor o igual a 0")
    except Exception as e:
        print (f"Exception. Error de {e}. error desconocido")
    print (f"el monto ingresado fue : ${monto_ingresado}")
    flag = True

flag = False
while flag == False:
    try:
        comision_ingresada = float(input("ingrese una comision de operacion mayor o igual a 0 :\n"))
    except ValueError as ve:
        print (f"Value Error. Error de {ve}. la comision por depositar debe ser un numero decimal mayor o igual a 0")
    except Exception as e:
        print (f"Error de {e}. error desconocido")
    print (f"la comision ingresada fue: ${comision_ingresada}")
    flag = True

cuentaca._comision = comision_ingresada

cuentaca.depositar(monto_ingresado)
print(f" el saldo de la cuentaca es ${cuentaca.saldo}")
print(f" detalles de la cuentaca {cuentaca}")

print ("opero sobre la cuentaca")
print ("operacion extraer")

flag = False
while flag == False:
    try:
        monto_ingresado = float(input("ingrese un monto a extraer mayor a 0 :\n"))
    except ValueError as ve:
        print (f"ErrorValue. Error de {ve}. el monto a extraer debe ser un numero decimal mayor o igual a 0")
    except Exception as e:
        print (f"Error de {e}. error desconocido")
    print (f"el monto a extraer ingresado fue: ${monto_ingresado}")
    flag = True

cuentaca.extraer(monto_ingresado)
print(f" el saldo de la cuentaca es ${cuentaca.saldo}")
print(f" detalles de la cuentaca {cuentaca}")

cuentacc = cc(
            cuentaca.titular,   
            cuentaca._cbu,
            cuentaca._saldo,
            500.00)             #limite descubierto


print ("opero sobre la cuentacc")
print (f"detalles de la cuentaca {cuentacc}")

print ("operacion extraer")


flag = False
while flag == False:
    try:
        monto_ingresado = float(input("ingrese un monto a extraer mayor a 0 :\n"))
    except ValueError as ve:
        print (f"ErrorValue. Error de {ve}. el monto a extraer debe ser un numero decimal mayor o igual a 0")
    except Exception as e:
        print (f"Error de {e}. error desconocido")
    print (f"el monto a extraer ingresado fue: ${monto_ingresado}")
    flag = True

flag = False
while flag == False:
    try:
        limite_descubierto_ingresado = float(input("ingrese un limite descubierto mayor o igual a 0 :\n"))
    except ValueError as ve:
        print (f"ErrorValue. Error de {ve}. el limite descubierto para la operacion Extraer debe ser un numero decimal mayor o igual a 0")
    except Exception as e:
        print (f"Error de {e}. error desconocido")
    print (f"el monto a extraer ingresado fue: ${limite_descubierto_ingresado}")
    flag = True

cuentacc._limite_descubierto = limite_descubierto_ingresado

cuentacc.extraer(monto_ingresado)
print(f"el saldo de la cuentacc es {cuentacc.saldo}")
print(f"los detalles de la cuentacc son {cuentacc}")

cuentach = ch(
            cuentacc.titular,
            cuentacc._cbu,
            cuentacc._saldo,
            50.00)              # costo de emsion del cheque

print(f"el saldo de la cuentach es {cuentach.saldo}")
print(f"los detalles de la cuentach son {cuentach}")

flag = False
while flag == False:
    try:
        monto_ingresado = float(input("ingrese un monto a extraer mayor a 0 :\n"))
    except ValueError as ve:
        print (f"ErrorValue. Error de {ve}. el monto debe ser un numero decimal mayor o igual a 0")
    except Exception as e:
        print (f"Error de {e}. error desconocido")
    print (f"el monto a extraer ingresado fue: ${monto_ingresado}")
    flag = True

flag = False
while flag == False:
    try:
        costo_emision_ingresado = float(input("ingrese un costo de emision mayor o igual a 0:\n"))
    except ValueError as ve:
        print (f"ErrorValue. Error de {ve}. el costo de emision ingresado debe ser un numero decimal mayor o igual a 0")
    except Exception as e:
        print (f"Error de {e}. error desconocido")
    print (f"el costo de emision ingresado fue: ${costo_emision_ingresado}")
    flag = True

cuentach._costo_emision = costo_emision_ingresado

cuentach.extraer(monto_ingresado)
print(f"el saldo de la cuentach es {cuentach.saldo}")
print(f"la cuentach es {cuentach}")

