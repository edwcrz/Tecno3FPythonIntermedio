# Contacto_Cliente.py
"""
create table if not exists contacto_cliente(
	email01 varchar (100) not null primary key,
	telefono01 int (15) not null,
    email02 varchar (100) not null,
    telefono02 int (15) not null,
    slack_id varchar (100) not null,
	discord_id varchar (100) not null,
    empleado_id int (15) not null,
    foreign key (empleado_id) references empleado_cliente(empleado_id));
"""

# clase para mi tabla sql contacto_cliente
class Contacto_Cliente:
    def __init__(self, email01, telefono01, email02, telefono02, slack_id, discord_id, empleado_id):
        self.__email01 = email01
        self.__telefono01 = telefono01
        self.__email02 = email02
        self.__telefono02 = telefono02
        self.__slack_id = slack_id
        self.__discord_id = discord_id
        self.__empleado_id = empleado_id

# creo getters, setters y deleters para mi clase contacto_cliente
# defino getters para mi clase contacto_cliente

    @property
    def email01(self):
        return self.__email01

    @property
    def telefono01(self):
        return self.__telefono01

    @property
    def email02(self):
        return self.__email02

    @property
    def telefono02(self):
        return self.__telefono02

    @property
    def slack_id(self):
        return self.__slack_id

    @property
    def discord_id(self):
        return self.__discord_id

    @property
    def empleado_id(self):
        return self.__empleado_id

# defino setters para mi clase contacto_cliente

    @email01.setter
    def email01(self, email01):
        self.__email01 = email01

    @telefono01.setter
    def telefono01(self, telefono01):
        self.__telefono01 = telefono01

    @email02.setter
    def email02(self, email02):
        self.__email02 = email02

    @telefono02.setter
    def telefono02(self, telefono02):
        self.__telefono02 = telefono02

    @slack_id.setter
    def slack_id(self, slack_id):
        self.__slack_id = slack_id

    @discord_id.setter
    def discord_id(self, discord_id):
        self.__discord_id = discord_id

    @empleado_id.setter
    def empleado_id(self, empleado_id):
        self.__empleado_id = empleado_id

# defino deleters para mi clase contacto_cliente

    @email01.deleter
    def email01(self):
        del self.__email01

    @telefono01.deleter
    def telefono01(self):
        del self.__telefono01

    @email02.deleter
    def email02(self):
        del self.__email02

    @telefono02.deleter
    def telefono02(self):
        del self.__telefono02

    @slack_id.deleter
    def slack_id(self):
        del self.__slack_id

    @discord_id.deleter
    def discord_id(self):
        del self.__discord_id

    @empleado_id.deleter
    def empleado_id(self):
        del self.__empleado_id

# defino un metodo para mostrar los datos de mi clase contacto_cliente
    def mostrar_info(self):
        info = (
            f"Email 01: {self.__email01}\n"
            f"Teléfono 01: {self.__telefono01}\n"
            f"Email 02: {self.__email02}\n"
            f"Teléfono 02: {self.__telefono02}\n"
            f"Slack ID: {self.__slack_id}\n"
            f"Discord ID: {self.__discord_id}\n"
            f"Empleado ID: {self.__empleado_id}"
        )
        return info

