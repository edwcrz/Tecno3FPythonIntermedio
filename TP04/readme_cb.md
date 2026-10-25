clase cuentabancaria: abstracta

atributos:
titular: publico
cbu: privado
saldo: privado

metodos:
getter cbu
getter saldo

setter cbu no lleva para que no tenga acceso una vez que es cargado
setter saldo lleva, es mandatorio para poder operar con metodos: depositar y extraer con el saldo

extraer: se realiza genera un metodo abtrasct que obliga a implementarse en todos los metodos hijos

__str__ sirve para mostrar cuando se llama a la clase para que no muestre una posicion de memoria
