create database examen
use examen

create table autores(
	id int primary key not null,
	nombres varchar(100),
	apellidos varchar(100),
	fecha_de_nacimiento date,
	editorial varchar(100)
)


create table libros(
	id int primary key not null,
	titulo varchar(100),
	descripcion varchar(100),
	tema varchar(100),
	Numero_paginas int
)

create table relacion(
	id_relacion int primary key not null,
	id_autor int foreign key (id_autor) references autores (id),
	id_libro int foreign key (id_libro) references libros (id),

)

insert into autores (id,nombres,apellidos,fecha_de_nacimiento,editorial) values(1,'leonardo', 'lopez','2008-11-11','texoco')
select*from autores

insert into libros (id,titulo,descripcion,tema,Numero_paginas) values(1,'viaje al centro de la tierra', 'efefsefsefsf','ciencia ficcion',200)
select*from libros

CREATE VIEW relaciones
AS
SELECT a.nombres,
a.apellidos, 
l.titulo AS 'libro',
a.editorial, 
l.tema,
l.Numero_paginas 
FROM autores a
JOIN libros l
ON a.id = l.id

select*from relaciones