# Bill_of_Material.py
"""
creo una clase para mi tabla sql bill_of_material

create table if not exists bill_of_material(
	bom_id int (15) not null primary key auto_increment,
	sku varchar (100) not null,
    vendor_id int (15) not null,
    categoria varchar (100) not null,
    subcategoria varchar (100) not null,
    cantidad_por_nodo int (10) not null,
    candidad_nodo int (10) not null,
    cantidad int (10) not null,
    equipo_tipo int (10) not null,
    serviceable boolean not null,
    spare boolean not null,
    foreign key (sku) references precio_lista(sku));
"""

# clase para mi tabla sql bill_of_material
class Bill_of_Material:
    def __init__(self, bom_id, sku, vendor_id, categoria, subcategoria, cantidad_por_nodo, candidad_nodo, cantidad, equipo_tipo, serviceable, spare):
        self.__bom_id = bom_id
        self.__sku = sku
        self.__vendor_id = vendor_id
        self.__categoria = categoria
        self.__subcategoria = subcategoria
        self.__cantidad_por_nodo = cantidad_por_nodo
        self.__candidad_nodo = candidad_nodo
        self.__cantidad = cantidad
        self.__equipo_tipo = equipo_tipo
        self.__serviceable = serviceable
        self.__spare = spare

# creo getters, setters y deleters para mi clase bill_of_material
# defino getters para mi clase bill_of_material
@property
def bom_id(self):
    return self.__bom_id
@property
def sku(self):
    return self.__sku
@property
def vendor_id(self):
    return self.__vendor_id
@property
def categoria(self):
    return self.__categoria
@property
def subcategoria(self):
    return self.__subcategoria
@property
def cantidad_por_nodo(self):
    return self.__cantidad_por_nodo
@property
def candidad_nodo(self):
    return self.__candidad_nodo
@property
def cantidad(self):
    return self.__cantidad
@property
def equipo_tipo(self):
    return self.__equipo_tipo
@property
def serviceable(self):
    return self.__serviceable
@property
def spare(self):
    return self.__spare

# defino setters para mi clase bill_of_material
@bom_id.setter
def bom_id(self, bom_id):
    self.__bom_id = bom_id

@sku.setter
def sku(self, sku):
    self.__sku = sku

@vendor_id.setter
def vendor_id(self, vendor_id):
    self.__vendor_id = vendor_id

@categoria.setter
def categoria(self, categoria):
    self.__categoria = categoria

@subcategoria.setter
def subcategoria(self, subcategoria):
    self.__subcategoria = subcategoria

@cantidad_por_nodo.setter
def cantidad_por_nodo(self, cantidad_por_nodo):
    self.__cantidad_por_nodo = cantidad_por_nodo

@candidad_nodo.setter
def candidad_nodo(self, candidad_nodo):
    self.__candidad_nodo = candidad_nodo

@cantidad.setter
def cantidad(self, cantidad):
    self.__cantidad = cantidad

@equipo_tipo.setter
def equipo_tipo(self, equipo_tipo):
    self.__equipo_tipo = equipo_tipo

@serviceable.setter
def serviceable(self, serviceable):
    self.__serviceable = serviceable

@spare.setter
def spare(self, spare):
    self.__spare = spare

# genero delete para mi clase bill_of_material
@bom_id.deleter
def bom_id(self):
    del self.__bom_id
def sku(self):
    del self.__sku
def vendor_id(self):
    del self.__vendor_id
def categoria(self):
    del self.__categoria
def subcategoria(self):
    del self.__subcategoria
def cantidad_por_nodo(self):
    del self.__cantidad_por_nodo
def candidad_nodo(self):
    del self.__candidad_nodo
def cantidad(self):
    del self.__cantidad
def equipo_tipo(self):
    del self.__equipo_tipo
def serviceable(self):
    del self.__serviceable
def spare(self):
    del self.__spare

def __str__(self):
    return f"BillOfMaterial(id={self.__bom_id}, sku={self.__sku})"
def __repr__(self):
    return f"BillOfMaterial(id={self.__bom_id}, sku={self.__sku})"

