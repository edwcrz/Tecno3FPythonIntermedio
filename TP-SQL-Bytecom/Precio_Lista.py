# Precio_Lista.py
"""
creo una clase para mi tabla sql precio_lista

create table if not exists precio_lista(
	sku varchar (100) not null primary key,
    descripcion varchar (100) not null,
    unit_price int (10) not null,
    peso int (10) not null,
    volumen int (10) not null,
    categoria varchar (100) not null,
    subcategoria varchar (100) not null,
    serie varchar (100) not null,
    linea varchar (100) not null,
    vendor_id int (15),
    foreign key (vendor_id) references vendor(vendor_id));
"""

class Precio_Lista:
    def __init__(self, sku, descripcion, unit_price, peso, volumen, categoria, subcategoria, serie, linea, vendor_id):
        self.__sku = sku
        self.__descripcion = descripcion
        self.__unit_price = unit_price
        self.__peso = peso
        self.__volumen = volumen
        self.__categoria = categoria
        self.__subcategoria = subcategoria
        self.__serie = serie
        self.__linea = linea
        self.__vendor_id = vendor_id

    @property
    def sku(self):
        return self.__sku

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def unit_price(self):
        return self.__unit_price

    @property
    def peso(self):
        return self.__peso

    @property
    def volumen(self):
        return self.__volumen

    @property
    def categoria(self):
        return self.__categoria

    @property
    def subcategoria(self):
        return self.__subcategoria

    @property
    def serie(self):
        return self.__serie

    @property
    def linea(self):
        return self.__linea

    @property
    def vendor_id(self):
        return self.__vendor_id

## defino los setters para cada atributo de la clase Precio_Lista
    @sku.setter
    def sku(self, nuevo_sku):
        if not nuevo_sku:
            raise ValueError("El SKU no puede estar vacío.")
        self.__sku = nuevo_sku

    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        if not nueva_descripcion:
            raise ValueError("La descripción no puede estar vacía.")
        self.__descripcion = nueva_descripcion

    @unit_price.setter
    def unit_price(self, nuevo_unit_price):
        if not isinstance(nuevo_unit_price, (int, float)):
            raise TypeError("El precio unitario debe ser un número.")
        if nuevo_unit_price < 0:
            raise ValueError("El precio unitario no puede ser negativo.")
        self.__unit_price = nuevo_unit_price

    @peso.setter
    def peso(self, nuevo_peso):
        if not isinstance(nuevo_peso, (int, float)):
            raise TypeError("El peso debe ser un número.")
        if nuevo_peso < 0:
            raise ValueError("El peso no puede ser negativo.")
        self.__peso = nuevo_peso

    @volumen.setter
    def volumen(self, nuevo_volumen):
        if not isinstance(nuevo_volumen, (int, float)):
            raise TypeError("El volumen debe ser un número.")
        if nuevo_volumen < 0:
            raise ValueError("El volumen no puede ser negativo.")
        self.__volumen = nuevo_volumen

    @categoria.setter
    def categoria(self, nueva_categoria):
        if not nueva_categoria:
            raise ValueError("La categoría no puede estar vacía.")
        self.__categoria = nueva_categoria

    @subcategoria.setter
    def subcategoria(self, nueva_subcategoria):
        if not nueva_subcategoria:
            raise ValueError("La subcategoría no puede estar vacía.")
        self.__subcategoria = nueva_subcategoria

    @serie.setter
    def serie(self, nueva_serie):
        if not nueva_serie:
            raise ValueError("La serie no puede estar vacía.")
        self.__serie = nueva_serie

    @linea.setter
    def linea(self, nueva_linea):
        if not nueva_linea:
            raise ValueError("La línea no puede estar vacía.")
        self.__linea = nueva_linea

    @vendor_id.setter
    def vendor_id(self, nuevo_vendor_id):
        if not isinstance(nuevo_vendor_id, int):
            raise TypeError("El ID del proveedor debe ser un entero.")
        self.__vendor_id = nuevo_vendor_id

# defino un método para mostrar la información del producto
    def mostrar_info(self):
        info = (
            f"SKU: {self.__sku}\n"
            f"Descripción: {self.__descripcion}\n"
            f"Precio Unitario: {self.__unit_price}\n"
            f"Peso: {self.__peso}\n"
            f"Volumen: {self.__volumen}\n"
            f"Categoría: {self.__categoria}\n"
            f"Subcategoría: {self.__subcategoria}\n"
            f"Serie: {self.__serie}\n"
            f"Línea: {self.__linea}\n"
            f"ID del Proveedor: {self.__vendor_id}"
        )
        return info

# defino los deleters para cada atributo de la clase Precio_Lista
    @sku.deleter
    def sku(self):
        del self.__sku
    @descripcion.deleter
    def descripcion(self):
        del self.__descripcion
    @unit_price.deleter
    def unit_price(self):
        del self.__unit_price
    @peso.deleter
    def peso(self):
        del self.__peso 
    @volumen.deleter
    def volumen(self):
        del self.__volumen
    @categoria.deleter
    def categoria(self):
        del self.__categoria
    @subcategoria.deleter
    def subcategoria(self):
        del self.__subcategoria
    @serie.deleter
    def serie(self):
        del self.__serie
    @linea.deleter
    def linea(self):
        del self.__linea    
    