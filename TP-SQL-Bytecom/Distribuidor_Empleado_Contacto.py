# Distribuidor_Empleado_Contacto.py
"""
create table if not exists distribuidor_empleado_contacto(
    email1 varchar (100) not null primary key,
	telefono1 int (15) not null,
    email2 varchar (100) not null,
    telefono2 int (15) not null,
    empleado_id int (15) not null,
    foreign key (empleado_id) references distribuidor_empleado(empleado_id));
"""
# Defino una clase para mi tabla sql distribuidor_empleado_contacto
class Distribuidor_Empleado_Contacto:
    def __init__(self, email1, telefono1, email2, telefono2, empleado_id):
        self.__email1 = email1
        self.__telefono1 = telefono1
        self.__email2 = email2
        self.__telefono2 = telefono2
        self.__empleado_id = empleado_id

# defino getters para mi clase distribuidor_empleado_contacto
    @property
    def email1(self):
        return self.__email1

    @property
    def telefono1(self):
        return self.__telefono1

    @property
    def email2(self):
        return self.__email2

    @property
    def telefono2(self):
        return self.__telefono2

    @property
    def empleado_id(self):
        return self.__empleado_id

# defino setters para mi clase distribuidor_empleado_contacto
    
    @email1.setter
    def email1(self, email1):
        self.__email1 = email1

    @telefono1.setter
    def telefono1(self, telefono1):
        self.__telefono1 = telefono1

    @email2.setter
    def email2(self, email2):
        self.__email2 = email2

    @telefono2.setter
    def telefono2(self, telefono2):
        self.__telefono2 = telefono2

    @empleado_id.setter
    def empleado_id(self, empleado_id):
        self.__empleado_id = empleado_id

# defino deleters para mi clase distribuidor_empleado_contacto
    
    @email1.deleter
    def email1(self):
        del self.__email1

    @telefono1.deleter
    def telefono1(self):
        del self.__telefono1

    @email2.deleter
    def email2(self):
        del self.__email2

    @telefono2.deleter
    def telefono2(self):
        del self.__telefono2

    @empleado_id.deleter
    def empleado_id(self):
        del self.__empleado_id

# defino un metodo str para mi clase distribuidor_empleado_contacto
    
    def __str__(self):
        return f"Distribuidor_Empleado_Contacto(email1={self.__email1}, telefono1={self.__telefono1}, email2={self.__email2}, telefono2={self.__telefono2}, empleado_id={self.__empleado_id})"  

# defino un metodo repr para mi clase distribuidor_empleado_contacto
    
    def __repr__(self):
        return f"Distribuidor_Empleado_Contacto(email1={self.__email1}, telefono1={self.__telefono1}, email2={self.__email2}, telefono2={self.__telefono2}, empleado_id={self.__empleado_id})"

# defino un metodo eq para mi clase distribuidor_empleado_contacto

    def __eq__(self, other):
        if isinstance(other, Distribuidor_Empleado_Contacto):
            return self.__email1 == other.__email1 and self.__telefono1 == other.__telefono1 and self.__email2 == other.__email2 and self.__telefono2 == other.__telefono2 and self.__empleado_id == other.__empleado_id
        return False

# defino un metodo hash para mi clase distribuidor_empleado_contacto
    
    def __hash__(self):
        return hash((self.__email1, self.__telefono1, self.__email2, self.__telefono2, self.__empleado_id))

# utilicemos reglas de polimorfismo para crear una lista de objetos distribuidor_empleado_contacto y mostrar su informacion
if __name__ == "__main__":
    contacto1 = Distribuidor_Empleado_Contacto("john.doe@example.com", "123-456-7890", "jane.doe@example.com", "098-765-4321", 1)
    contacto2 = Distribuidor_Empleado_Contacto("bob.smith@example.com", "555-555-5555", "alice.smith@example.com", "555-123-4567", 2)

    contactos = [contacto1, contacto2]

    for contacto in contactos:
        print(contacto) # Esto llamará al método __str__ de cada objeto y mostrará su información en la consola

# utilicemos clase abstrata para crear una clase base para distribuidor_empleado_contacto y luego heredar de ella
from abc import ABC, abstractmethod

class Distribuidor_Empleado_Contacto_Base(ABC):
    def __init__(self, email1, telefono1, email2, telefono2, empleado_id):
        self.__email1 = email1
        self.__telefono1 = telefono1
        self.__email2 = email2
        self.__telefono2 = telefono2
        self.__empleado_id = empleado_id

    @property
    def email1(self):
        return self.__email1

    @property
    def telefono1(self):
        return self.__telefono1

    @property
    def email2(self):
        return self.__email2

    @property
    def telefono2(self):
        return self.__telefono2

    @property
    def empleado_id(self):
        return self.__empleado_id

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass