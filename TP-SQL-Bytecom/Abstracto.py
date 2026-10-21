# Absctracto.py
"""
create table if not exists empleado_datos_personales(
	dni int (8) not null primary key,
    nombre varchar (100) not null,
	segundo_nombre varchar (100) not null,
    apellido varchar (100) not null,
	direccion varchar (100) not null,
    localidad varchar (100) not null,
    ciudad varchar (100) not null,
    pais varchar (100) not null,
    nacionalidad varchar (100) not null,
    codigo_postal varchar (100) not null,
    telefono varchar (100) not null,
    email_personal varchar (100) not null,    
    fecha_nacimiento date not null);
create table if not exists empleado_liquidacion(
	cuil int (11) not null primary key,
    banco01 varchar (100) not null,
    sucursal01 varchar (100) not null,
    cuenta01 varchar (100) not null,
    banco02 varchar (100) not null,
    sucursal02 varchar (100) not null,
    cuento02 varchar (100) not null); 
create table if not exists sector(
	sector_id int (12) not null primary key,
    nombre_sector varchar (100) not null,
    lider_sector varchar (100) not null,
    entidadd_superior varchar (100) not null,
    rol varchar (100) not null);
create table if not exists empleado(
	empleado_id int (15) not null primary key auto_increment,
    dni int (8) not null,
    cuil int (11) not null,
    foreign key (dni) references empleado_datos_personales(dni),
    foreign key (cuil) references empleado_liquidacion(cuil));
create table if not exists funcion(
	funcion_id int (15) not null primary key auto_increment,
	empleado_id int (15) not null,
    sector_id int (15) not null,
    foreign key (empleado_id) references empleado(empleado_id),
	foreign key (sector_id) references sector(sector_id));
create table if not exists empleado_contacto_laboral(
    email01 varchar (100) not null primary key,
    telefono01 varchar (100) not null,
    email02 varchar (100) not null,
	telefono02 varchar (100) not null,
    discord_id varchar (100) not null,
    slack_id varchar (100) not null,
    empleado_id int (15) not null,
    foreign key (empleado_id) references empleado(empleado_id));

/*
	select * from empleado_datos_personales;
	select * from empleado_liquidacion;
	select * from sector;
	select * from empleado;
	select * from funcion;
	select * from empleado_contacto_laboral;
 */   
-- modulo vendor
create table if not exists vendor(
	vendor_id int (15) not null primary key auto_increment,
    razon_social varchar (100) not null,
    cuil int (11) not null,
    nombre_fantasia varchar (100) not null,
    pais_base_comercial varchar (100) not null,
    pais_fabricacion varchar (100) not null,
    pais_facturacion_hardware varchar (100) not null,
    pais_facturacion_servicios varchar (100) not null);
create table if not exists vendor_empleado(
	empleado_id int (15) not null primary key auto_increment,
    nombre varchar (100) not null,
    segundo_nombre varchar (100) not null,
    apellido varchar (100) not null,
    sector varchar (100) not null,
    vendor_id int (15) not null,
    foreign key (vendor_id) references vendor(vendor_id));
create table if not exists vendor_empleado_contacto(
    email1 varchar (100) not null primary key,
	telefono1 int (15) not null,
    email2  varchar (100) not null,
    telefono2  int (15) not null,
    empleado_id int (15) not null,
    foreign key (empleado_id) references vendor_empleado(empleado_id));
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

/*
	select * from vendor;
	select * from vendor_empleado;
	select * from vendor_empleado_contacto;
	select * from precio_lista;
*/

-- modulo distribuidor
create table if not exists distribuidor_mayorista(
	distribuidor_id int (15) not null primary key auto_increment,
    razon_social varchar (100) not null,
    cuil int (11) not null,
    nombre_fantasia varchar (100) not null,
    pais_base_comercial varchar (100) not null,
    pais_facturacion_hardware varchar (100) not null,
    pais_facturacion_servicios varchar (100) not null);
create table if not exists distribuidor_empleado(
	empleado_id int (15) not null primary key auto_increment,
    nombre varchar (100) not null,
    segundo_nombre varchar (100) not null,
    apellido varchar (100) not null,
    sector varchar (100) not null,
    distribuidor_id int (15) not null,
    foreign key (distribuidor_id) references distribuidor_mayorista(distribuidor_id));
create table if not exists distribuidor_empleado_contacto(
    email1 varchar (100) not null primary key,
	telefono1 int (15) not null,
    email2 varchar (100) not null,
    telefono2 int (15) not null,
    empleado_id int (15) not null,
    foreign key (empleado_id) references distribuidor_empleado(empleado_id));
/* 
	select * from distribuidor_mayorista;
	select * from distribuidor_empleado;
	select * from distribuidor_empleado_contacto;
*/

-- modulo cliente
create table if not exists cliente(
	cliente_id int (15) not null primary key auto_increment,
    nombre_cliente varchar (100) not null,
	razon_social varchar (100) not null,
	nombre_fantasia varchar (100) not null,
	mercado_vertical varchar (100) not null,
	fecha_ultima_compra_bienes date not null,
	fecha_ultima_compra_servicios date not null,
	fecha_ultima_compra_soporte date not null);
create table if not exists sector_cliente(
	sector_id int (15) not null primary key auto_increment,
    nombre_sector varchar (100) not null,
	cliente_id int (15) not null,
    foreign key (cliente_id) references cliente(cliente_id));
create table if not exists empleado_cliente(
	empleado_id int (15) not null primary key auto_increment,
    nombre varchar (100) not null,
    segundo_nombre varchar (100) not null,
    apellido varchar (100) not null,
    sector_id int (15) not null,
    foreign key (sector_id) references sector_cliente(sector_id));
create table if not exists contacto_cliente(
	email01 varchar (100) not null primary key,
	telefono01 int (15) not null,
    email02 varchar (100) not null,
    telefono02 int (15) not null,
    slack_id varchar (100) not null,
	discord_id varchar (100) not null,
    empleado_id int (15) not null,
    foreign key (empleado_id) references empleado_cliente(empleado_id));
/* 
	select * from cliente;
	select * from sector_cliente;
    select * from empleado_cliente;
	select * from contacto_cliente;
*/

-- modulo oportunidad
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
create table if not exists oportunidad_descuento(
	oportunidad_vendor_id int (15) not null primary key auto_increment,
    sku varchar (100) not null,
    cantidad int (15) not null,
    descuento int (15) not null,
    fecha_inicio_vigencia date not null,
    fecha_finalizacion_vigencia date not null);
create table if not exists servicio_costo(
	servicio_id int (15) not null primary key auto_increment,
	sku varchar (100) not null,
    descripcion varchar (100) not null,
    horas int (10) not null,
    cantidad int (10) not null,
    unit_cost decimal(5,2) not null,
    categoria varchar (100) not null,
    subcategoria varchar (100) not null,
    pais_origen varchar (100) not null,
    pais_facturacion varchar (100) not null,
    fecha_inicio date not null,
    fecha_finalizacion date not null);
create table if not exists soporte_costo(
	soporte_id int (15) not null primary key auto_increment,
    sku varchar (100) not null,
    descripcion varchar (100) not null,
    cantidad int not null,
    unit_cost decimal not null,
    categoria varchar (100) not null,
    subcategoria varchar (100) not null,
    cobertura varchar (100) not null,
    region_visita_onsite varchar (100),
    rma_sla varchar (100) not null,
    periodo varchar (100) not null,
    spare boolean not null,
    pais_origen varchar (100) not null,
    pais_facturacion varchar (100) not null,
    fecha_inicio date not null,
    fecha_finalizacion date not null);
create table if not exists requerimiento(
	requerimiento_id int (15) not null primary key auto_increment,
	hardware boolean not null,
    licencia_permanente boolean not null,
    suscripcion_temporal boolean not null,
    software boolean not null,
    servicios boolean not null,
    materiales boolean not null,
    soporte boolean not null,
    empleado_id int (15) not null,
    foreign key (empleado_id) references empleado_cliente(empleado_id));
create table if not exists registro_oportunidad(
	oportunidad_id int (15) not null primary key auto_increment,
    oportunidad_vendor_id int (15) not null,
	oportunidad_distribuidor_id int (15) not null,
    bom_id int (15) not null,
    distribuidor_id int (15) not null,
    requerimiento_id int (15) not null,
    servicio_id int (15) not null,
    soporte_id int (15) not null,
    foreign key (oportunidad_vendor_id) references oportunidad_descuento(oportunidad_vendor_id),
	foreign key (bom_id) references bill_of_material(bom_id),
    foreign key (distribuidor_id) references distribuidor_mayorista(distribuidor_id),
    foreign key (requerimiento_id) references requerimiento(requerimiento_id),
    foreign key (servicio_id) references servicio_costo(servicio_id),
    foreign key (soporte_id) references soporte_costo(soporte_id));
create table if not exists oportunidad_team(
	team_id int (15) not null primary key auto_increment,
    oportunidad_id int (15) not null,
	foreign key (oportunidad_id) references registro_oportunidad(oportunidad_id));
create table if not exists team_tupla(
	team_tupla_id int (15) not null primary key auto_increment,
    team_id int (15) not null,
    funcion_id int (15) not null,
	foreign key (team_id) references oportunidad_team(team_id),
    foreign key (funcion_id) references funcion(funcion_id));
  /*
	select * from bill_of_material;
	select * from oportunidad_descuento;
	select * from servicio_costo;
	select * from soporte_costo;
	select * from requerimiento;
	select * from registro_oportunidad;
	select * from oportunidad_team;
	select * from team_tupla;
*/
  
-- modulo proyecto
create table if not exists proyecto(
	proyecto_id int (15) not null primary key auto_increment,
	nombre_proyecto varchar (100) not null,
    orden_compra_id int (15) not null,
    oportunidad_id int (15) not null,
    foreign key (oportunidad_id) references registro_oportunidad(oportunidad_id));
create table if not exists hito(
	hito_id int (15) not null primary key auto_increment,
    nombre_hito varchar (100) not null,
    fecha_inicio date not null,
    fecha_finalizacion date not null,
    fecha_facturacion date not null,
    proyecto_id int (15) not null,
    foreign key (proyecto_id) references proyecto(proyecto_id));
"""

from abc import ABC, abstractmethod
# creo una clase abstracta para mi tabla sql abstracto
class Abstracto(ABC):
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id

# creo clases abstractas para mis tablas sql
# por ejemplo empleado para instanciar en vendor_empleado, distribuidor_empleado y empleado_cliente
# por ejemplo contacto para instanciar en vendor_empleado_contacto, distribuidor_empleado_contacto y contacto_cliente

class Empleado:
    def __init__(self, id, nombre, apellido):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido

    @property
    def id(self):
        return self.__id    
    @property
    def nombre(self):
        return self.__nombre
    @property
    def apellido(self):
        return self.__apellido

class Contacto:
    def __init__(self, email01, telefono01):
        self.__email01 = email01
        self.__telefono01 = telefono01

    @property
    def email01(self):
        return self.__email01   
    @property
    def telefono01(self):
        return self.__telefono01

# creo una clase para mi tabla sql proyecto

        
    



