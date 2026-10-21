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
