SHOW databases;
USE coastbase;
SHOW tables;


DESCRIBE usuario;

INSERT INTO usuario
(id,nombre_usuario,email,pass,nombre,apellido,tipo_usario,dni,direccion)
VALUES
(NULL, 'mlopez', 'mlopez@gmail.com', '1234', 'María', 'López', 'cliente', 40123654, 'Av. San Martín 123'),
(NULL, 'jperez', 'jperez@hotmail.com', '1234', 'Juan', 'Pérez', 'cliente', 38256987, 'Calle Belgrano 456'),
(NULL, 'arodriguez', 'arodriguez@yahoo.com', '1234', 'Ana', 'Rodríguez', 'cliente', 39547896, 'Mitre 789'),
(NULL, 'lfernandez', 'lfernandez@gmail.com', '1234', 'Lucía', 'Fernández', 'cliente', 41758963, 'Sarmiento 987'),
(NULL, 'cmartinez', 'cmartinez@gmail.com', '1234', 'Carlos', 'Martínez', 'cliente', 36254879, 'Italia 354'),
(NULL, 'mgonzalez', 'mgonzalez@hotmail.com', '1234', 'Martín', 'González', 'cliente', 37125984, 'Rivadavia 812'),
(NULL, 'nramirez', 'nramirez@gmail.com', '1234', 'Natalia', 'Ramírez', 'cliente', 40256321, 'Colón 1423'),
(NULL, 'rgarcia', 'rgarcia@gmail.com', '1234', 'Roberto', 'García', 'cliente', 39485623, 'Saavedra 300'),
(NULL, 'jmorales', 'jmorales@gmail.com', '1234', 'Julia', 'Morales', 'cliente', 38879654, '9 de Julio 250'),
(NULL, 'eperez', 'eperez@gmail.com', '1234', 'Esteban', 'Pérez', 'cliente', 40587645, 'San Juan 1800'),
(NULL, 'vbenitez', 'vbenitez@gmail.com', '1234', 'Valeria', 'Benítez', 'cliente', 39214578, 'Lavalle 77'),
(NULL, 'fsosa', 'fsosa@yahoo.com', '1234', 'Fernando', 'Sosa', 'cliente', 38521497, 'Bouchard 134'),
(NULL, 'drodriguez', 'drodriguez@gmail.com', '1234', 'Diego', 'Rodríguez', 'cliente', 40124567, 'Alsina 985'),
(NULL, 'cpaz', 'cpaz@gmail.com', '1234', 'Claudia', 'Paz', 'cliente', 37985642, 'Roca 1111');

SELECT id, nombre FROM usuario;


DESCRIBE producto;
DELETE FROM producto;
SELECT*FROM producto;
ALTER TABLE producto AUTO_INCREMENT = 1;

INSERT INTO producto
(id,nombre,precio,detalles,categoria,color,img,stock,estado)
VALUES
(NULL, 'Vestidos Shore', 27503.26, 'Producto veraniego de categoría Vestidos, ideal para los días cálidos.', 'Vestidos', 'Rojo', 'img_producto_1.jpg', 'Stock', 'visible'),
(NULL, 'Tops Coast', 16533.11, 'Producto veraniego de categoría Tops y Bodys, ideal para los días cálidos.', 'Tops y Bodys', 'Blanco', 'img_producto_2.jpg', 'Sin stock', 'visible'),
(NULL, 'Vestidos Breeze', 35452.94, 'Producto veraniego de categoría Vestidos, ideal para los días cálidos.', 'Vestidos', 'Negro', 'img_producto_4.jpg', 'Stock', 'no visible'),
(NULL, 'Vestidos Tropical', 44271.48, 'Producto veraniego de categoría Vestidos, ideal para los días cálidos.', 'Vestidos', 'Azul', 'img_producto_5.jpg', 'Stock', 'visible');


UPDATE producto SET stock="Sin Stock" WHERE id=1;



DESCRIBE compras;
SELECT * FROM compras;
DELETE FROM compras;

ALTER TABLE compras AUTO_INCREMENT=1;
INSERT INTO compras
(id,id_usuario,estado,fechahora,total)
VALUES
(NULL, 1, 'Pendiente', '2025-11-01 12:00:00', 27503.26),
(NULL, 2, 'Listo para entregar', '2025-11-16 12:00:00', 27541.01),
(NULL, 3, 'Entregado', '2025-12-02 12:00:00', 30912.02),
(NULL, 4, 'Cancelado', '2025-12-17 12:00:00', 12374.90),
(NULL, 5, 'En preparación', '2025-11-05 12:00:00', 44271.48),
(NULL, 6, 'Listo para entregar', '2025-11-22 12:00:00', 37942.65),
(NULL, 7, 'Entregado', '2025-12-06 12:00:00', 21870.91),
(NULL, 8, 'Cancelado', '2025-12-25 12:00:00', 23418.42),
(NULL, 9, 'Pendiente', '2025-11-10 12:00:00', 9984.33),
(NULL, 10, 'Listo para entregar', '2025-11-28 12:00:00', 12756.32);

SELECT* FROM compras;



DESCRIBE datos_pago;
DELETE FROM datos_pago;
select * FROM datos_pago;
ALTER TABLE datos_pago AUTO_INCREMENT=1;
INSERT INTO datos_pago
(id,id_usuario,comprobante,id_compra)
VALUES
(NULL, 1, 'CP1000', 1),
(NULL, 2, 'CP1001', 2),
(NULL, 3, 'CP1002', 3),
(NULL, 4, 'CP1003', 4),
(NULL, 5, 'CP1004', 5),
(NULL, 6, 'CP1005', 6),
(NULL, 7, 'CP1006', 7),
(NULL, 8, 'CP1007', 8),
(NULL, 9, 'CP1008', 9),
(NULL, 10, 'CP1009', 10);




DESCRIBE detalles_compras;
DELETE FROM detalles_compras;

ALTER TABLE detalles_compras AUTO_INCREMENT = 1;

INSERT INTO detalles_compras
(id,id_producto,id_compra,cantidad,precio_unidad)
VALUES
(NULL, 1, 1, 1, 27503.26),
(NULL, 2, 2, 1, 16533.11),
(NULL, 3, 3, 1, 19081.44),
(NULL, 4, 4, 1, 35452.94);

select * from detalles_compras;


SELECT compras.id AS id_compra,
usuario.nombre AS comprador,
compras.id_usuario,
compras.total
FROM compras
INNER JOIN usuario ON compras.id_usuario=usuario.id;


SELECT 
    usuario.id AS id_usuario,
    usuario.nombre,
    usuario.email,
    compras.id AS id_compra,
    datos_pago.id AS id_dato_pago,
    datos_pago.id_usuario,
    datos_pago.id_compra,
    datos_pago.comprobante
FROM datos_pago 
INNER JOIN compras  ON datos_pago.id_compra = compras.id
INNER JOIN usuario  ON datos_pago.id_usuario = usuario.id
LIMIT 5;

SELECT usuario.direccion, compras.id, usuario.nombre
FROM usuario INNER JOIN compras
ON compras.id_usuario = usuario.id;

SELECT usuario.nombre, compras.estado, datos_pago.comprobante
FROM datos_pago
INNER JOIN usuario ON datos_pago.id_usuario=usuario.id 
INNER JOIN compras ON datos_pago.id_compra=compras.id;





select * from usuario ;
select usuario.nombre where like %Carlos%;


SELECT * from usuario WHERE nombre = "Carlos";

SELECT producto.nombre as producto, detalles_compras.cantidad as cantidad, compras.id as identif, usuario.nombre as nombre
FROM producto
INNER JOIN detalles_compras ON producto.id = detalles_compras.id_producto
INNER JOIN compras ON detalles_compras.id_compra=compras.id 
INNER JOIN usuario ON compras.id_usuario=usuario.id;
