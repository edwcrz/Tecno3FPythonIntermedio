"""
Programacion Orientada a Objetos
Clase es una plantilla para crear objetos. Un objeto es una instancia de una clase.
clase: es un conjunto de atributos y métodos que definen el comportamiento de un objeto.
objeto: es una instancia de una clase. Un objeto tiene un estado y un comportamiento.   
metodo: es una función que pertenece a una clase. Un método define el comportamiento de un objeto.
atributo: es una variable que pertenece a una clase. Un atributo define el estado de un

reutilizaciòn: es la capacidad de un objeto de heredar atributos y métodos de otra clase. 
La reutilización permite crear nuevas clases a partir de clases existentes, lo que facilita la creación de programas más complejos y eficientes.
mantenimiento de código: es la capacidad de un programa de ser modificado y mejorado sin afectar su funcionamiento. 
El mantenimiento de código permite corregir errores, agregar nuevas funcionalidades y mejorar el rendimiento del programa.
modularidad: es la capacidad de un programa de ser dividido en módulos independientes que pueden ser desarrollados y probados por separado. 
La modularidad permite crear programas más complejos y eficientes, ya que cada módulo puede ser desarrollado y probado de manera independiente.
escalabilidad: es la capacidad de un programa de ser ampliado y mejorado sin afectar su funcionamiento. 
La escalabilidad permite agregar nuevas funcionalidades y mejorar el rendimiento del programa sin afectar su funcionamiento.
extensibilidad: es la capacidad de un programa de ser modificado y mejorado sin afectar su funcionamiento. 
La extensibilidad permite agregar nuevas funcionalidades y mejorar el rendimiento del programa sin afectar su funcionamiento.

encapsulamiento: es la capacidad de un objeto de ocultar su estado interno y exponer solo una interfaz pública para interactuar con él. 
El encapsulamiento permite proteger el estado interno de un objeto y evitar que sea modificado directamente por otros objetos, 
lo que mejora la seguridad y la integridad del programa.
protección de datos: es la capacidad de un objeto de proteger su estado interno y evitar que sea modificado directamente por otros objetos. 
La protección de datos permite mejorar la seguridad y la integridad del programa, ya que evita que los datos sean modificados de manera incorrecta o malintencionada.
interface controlada: es la capacidad de un objeto de exponer solo una interfaz pública para interactuar con él. 
La interface controlada permite proteger el estado interno de un objeto y evitar que sea modificado directamente por otros objetos, lo que mejora la seguridad y la integridad del programa.
mantenibilidad: es la capacidad de un programa de ser modificado y mejorado sin afectar su funcionamiento. 
La mantenibilidad permite corregir errores, agregar nuevas funcionalidades y mejorar el rendimiento del programa sin afectar su funcionamiento.
setter : es un método que permite modificar el valor de un atributo de un objeto. 
Un setter permite controlar el acceso a los atributos de un objeto y evitar que sean modificados de manera incorrecta o malintencionada.
getter: es un método que permite obtener el valor de un atributo de un objeto. 
Un getter permite controlar el acceso a los atributos de un objeto y evitar que sean modificados de manera incorrecta o malintencionada.
init: es un método especial que se ejecuta automáticamente cuando se crea un objeto de una clase. 
El método init permite inicializar los atributos de un objeto y establecer su estado inicial.

herencia: es la capacidad de una clase de heredar atributos y métodos de otra clase. 
La herencia permite crear nuevas clases a partir de clases existentes, lo que facilita la creación de programas más complejos y eficientes.
principio es un: conjunto de reglas o normas que guían el diseño y desarrollo de un programa. 
Los principios permiten crear programas más complejos y eficientes, ya que establecen las bases para la creación de clases y objetos.
reutilización de código: es la capacidad de un programa de ser modificado y mejorado sin afectar su funcionamiento. 
La reutilización de código permite corregir errores, agregar nuevas funcionalidades y mejorar el rendimiento del programa sin afectar su funcionamiento.
especializacion: es la capacidad de una clase de heredar atributos y métodos de otra clase y agregar nuevas funcionalidades. 
La especialización permite crear nuevas clases a partir de clases existentes, lo que facilita la creación de programas más complejos y eficientes.

polimorfismo: es la capacidad de un objeto de comportarse de diferentes maneras según el contexto en el que se utilice. 
El polimorfismo permite crear programas más complejos y eficientes, ya que permite que un objeto pueda ser utilizado de diferentes maneras según el contexto en el que se utilice.
intercambiabilidad es la capacidad de un objeto de ser utilizado en lugar de otro objeto de la misma clase. 
La intercambiabilidad permite crear programas más complejos y eficientes, ya que permite que un objeto pueda ser utilizado en lugar de otro objeto de la misma clase.
eliminación de condiciones innecesarias: es la capacidad de un programa de ser modificado y mejorado sin afectar su funcionamiento. 
La eliminación de condiciones innecesarias permite corregir errores, agregar nuevas funcionalidades y mejorar el rendimiento del programa sin afectar su funcionamiento.
duck typing: es la capacidad de un objeto de comportarse de diferentes maneras según el contexto en el que se utilice. 
El duck typing permite crear programas más complejos y eficientes, ya que permite que un objeto pueda ser utilizado de diferentes maneras según el contexto en el que se utilice.

abstracción: es la capacidad de un objeto de ocultar su estado interno y exponer solo una interfaz pública para interactuar con él.
foco en el dominio del problema: es la capacidad de un programa de ser modificado y mejorado sin afectar su funcionamiento.
reducción de la complejidad: es la capacidad de un programa de ser modificado y mejorado sin afectar su funcionamiento.
mantenibilidad: es la capacidad de un programa de ser modificado y mejorado sin afectar su funcionamiento.
"""

class Costo:
    def __init__(self, sku, descripcion, cost):
        self.__sku = sku
        self.__descripcion = descripcion    
        self.__cost = cost  # Atributo privado

    @property
    def cost(self):
        return self.__cost  # Getter para obtener el valor del costo

    @property
    def descripcion(self):
        return self.__descripcion  # Getter para obtener el valor de la descripción

    @property
    def sku(self):
        return self.__sku  # Getter para obtener el valor del SKU   

    @cost.setter
    def cost(self, nuevo_cost):
        if nuevo_cost < 0:
            raise ValueError("El costo no puede ser negativo.")
        self.__cost = nuevo_cost  # Setter para modificar el valor del costo

    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        if not nueva_descripcion:
            raise ValueError("La descripción no puede estar vacía.")
        self.__descripcion = nueva_descripcion  # Setter para modificar el valor de la descripción

    @sku.setter
    def sku(self, nuevo_sku):
        if not nuevo_sku:
            raise ValueError("El SKU no puede estar vacío.")
        self.__sku = nuevo_sku  # Setter para modificar el valor del SKU    
    
"""
que es el @property: es un decorador que permite definir un método como una propiedad de una clase.
que es el @setter: es un decorador que permite definir un método como un setter de una propiedad de una clase.
"""

router1 = Costo("acx7010", "Router acx 7010 24 puertos 10GE Base-T", 140.0)
router2 = Costo("acx7020", "Router acx 7020 24 puertos 10GE SFP", 150.0)
router3 = Costo("acx7030", "Router acx 7030 24 puertos 1GE/10GE", 160.0)

print(f"SKU: {router1.sku}, Descripción: {router1.descripcion}, Costo: {router1.cost}")
print(f"SKU: {router2.sku}, Descripción: {router2.descripcion}, Costo: {router2.cost}")
print(f"SKU: {router3.sku}, Descripción: {router3.descripcion}, Costo: {router3.cost}")

"""
que hace: _Costo__sku: es el nombre del atributo privado sku de la clase Costo.
que hace: _Costo__descripcion: es el nombre del atributo privado descripcion de la clase Costo.
que hace: _Costo__cost: es el nombre del atributo privado cost de la clase Costo.

"""