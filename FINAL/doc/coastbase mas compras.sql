-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 09, 2026 at 03:56 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `coastbase`
--

-- --------------------------------------------------------

--
-- Table structure for table `compras`
--

CREATE TABLE `compras` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `estado` enum('En preparación','Pendiente','Listo para entregar','Entregado','En carrito','Cancelado') NOT NULL,
  `fechahora` datetime NOT NULL,
  `total` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `compras`
--

INSERT INTO `compras` (`id`, `id_usuario`, `estado`, `fechahora`, `total`) VALUES
(1, 1, 'Pendiente', '2025-11-01 12:00:00', 27503.3),
(2, 2, 'Listo para entregar', '2025-11-16 12:00:00', 27541),
(3, 3, 'Entregado', '2025-12-02 12:00:00', 30912),
(4, 4, 'Cancelado', '2025-12-17 12:00:00', 12374.9),
(5, 5, 'En preparación', '2025-11-05 12:00:00', 44271.5),
(6, 6, 'Listo para entregar', '2025-11-22 12:00:00', 37942.6),
(7, 7, 'Entregado', '2025-12-06 12:00:00', 21870.9),
(8, 8, 'Entregado', '2025-12-25 12:00:00', 23418.4),
(9, 9, 'Pendiente', '2025-11-10 12:00:00', 9984.33),
(10, 10, 'Listo para entregar', '2025-11-28 12:00:00', 12756.3),
(11, 1, 'Entregado', '2025-12-20 14:30:00', 49990),
(12, 2, 'Pendiente', '2025-12-22 11:00:00', 32000),
(13, 3, 'En preparación', '2026-01-05 10:20:00', 24000),
(14, 4, 'Entregado', '2026-01-07 17:45:00', 75000),
(15, 5, 'Listo para entregar', '2026-01-10 09:15:00', 35000),
(16, 6, 'Pendiente', '2026-01-12 18:30:00', 27503.3),
(17, 7, 'En preparación', '2026-01-15 13:10:00', 64000),
(18, 8, 'Entregado', '2026-01-18 16:00:00', 49990),
(19, 9, 'Pendiente', '2026-01-20 12:40:00', 24000),
(20, 10, 'Entregado', '2026-01-22 19:10:00', 32000),
(21, 11, 'Pendiente', '2026-01-25 15:00:00', 35000),
(22, 12, 'En preparación', '2026-01-26 11:30:00', 49990),
(23, 13, 'Listo para entregar', '2026-01-27 10:00:00', 27503.3),
(24, 14, 'Entregado', '2026-01-28 17:00:00', 24000),
(25, 1, 'Pendiente', '2026-02-01 14:20:00', 64000);

-- --------------------------------------------------------

--
-- Table structure for table `datos_pago`
--

CREATE TABLE `datos_pago` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `comprobante` varchar(255) NOT NULL,
  `id_compra` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `datos_pago`
--

INSERT INTO `datos_pago` (`id`, `id_usuario`, `comprobante`, `id_compra`) VALUES
(1, 1, 'CP1000', 1),
(2, 2, 'CP1001', 2),
(3, 3, 'CP1002', 3),
(4, 4, 'CP1003', 4),
(5, 5, 'CP1004', 5),
(6, 6, 'CP1005', 6),
(7, 7, 'CP1006', 7),
(8, 8, 'CP1007', 8),
(9, 9, 'CP1008', 9),
(10, 10, 'CP1009', 10),
(11, 1, 'CP1010', 11),
(12, 2, 'CP1011', 12),
(13, 3, 'CP1012', 13),
(14, 4, 'CP1013', 14),
(15, 5, 'CP1014', 15),
(16, 6, 'CP1015', 16),
(17, 7, 'CP1016', 17),
(18, 8, 'CP1017', 18),
(19, 9, 'CP1018', 19),
(20, 10, 'CP1019', 20),
(21, 11, 'CP1020', 21),
(22, 12, 'CP1021', 22),
(23, 13, 'CP1022', 23),
(24, 14, 'CP1023', 24),
(25, 1, 'CP1024', 25);

-- --------------------------------------------------------

--
-- Table structure for table `detalles_compras`
--

CREATE TABLE `detalles_compras` (
  `id` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL,
  `id_compra` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `precio_unidad` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `detalles_compras`
--

INSERT INTO `detalles_compras` (`id`, `id_producto`, `id_compra`, `cantidad`, `precio_unidad`) VALUES
(1, 1, 1, 1, 27503.3),
(2, 2, 2, 1, 16533.1),
(3, 3, 3, 1, 19081.4),
(4, 4, 4, 1, 35452.9),
(5, 4, 5, 1, 44271.5),
(6, 1, 6, 2, 27503.3),
(7, 2, 7, 1, 16533.1),
(8, 3, 8, 1, 35452.9),
(9, 1, 9, 3, 27503.3),
(10, 2, 10, 1, 16533.1),
(11, 7, 11, 1, 49990),
(12, 6, 12, 1, 32000),
(13, 4, 13, 1, 24000),
(14, 2, 14, 2, 35000),
(15, 2, 15, 1, 35000),
(16, 3, 16, 1, 27503.3),
(17, 6, 17, 2, 32000),
(18, 7, 18, 1, 49990),
(19, 4, 19, 1, 24000),
(20, 6, 20, 1, 32000),
(21, 2, 21, 1, 35000),
(22, 7, 22, 1, 49990),
(23, 3, 23, 1, 27503.3),
(24, 4, 24, 1, 24000),
(25, 6, 25, 2, 32000);

-- --------------------------------------------------------

--
-- Table structure for table `producto`
--

CREATE TABLE `producto` (
  `id` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `precio` float NOT NULL,
  `detalles` text NOT NULL,
  `categoria` enum('Tops y Bodys','Polleras y Shorts','Vestidos','Accesorios') NOT NULL,
  `color` enum('Negro','Blanco','Rojo','Azul') NOT NULL,
  `img` varchar(255) NOT NULL,
  `stock` enum('Stock','Sin stock') NOT NULL,
  `estado` enum('visible','no visible') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `producto`
--

INSERT INTO `producto` (`id`, `nombre`, `precio`, `detalles`, `categoria`, `color`, `img`, `stock`, `estado`) VALUES
(1, 'Top Shore', 25000, 'Top veraniego liviano, ideal para días cálidos', 'Tops y Bodys', 'Blanco', 'img_producto_1.jpg', 'Sin stock', 'visible'),
(2, 'Body Bay', 35000, 'Body cómodo y elegante para uso diario', '', '', 'afdd0d15-4880-4b58-966f-76c45f9bdd80.jpg', 'Stock', 'visible'),
(3, 'Top Dove', 27503.3, 'Producto veraniego de categoría Tops y Bodys, ideal para los días cálidos.', 'Tops y Bodys', 'Blanco', 'img_producto_4.jpg', 'Stock', 'visible'),
(4, 'Top Pearl', 24000, 'Top moderno con diseño delicado', 'Tops y Bodys', 'Blanco', 'img_producto_5.jpg', 'Stock', 'visible'),
(6, 'Top Shelly', 32000, 'Top premium ideal para ocasiones especiales', 'Tops y Bodys', 'Blanco', '4cfc713e-4b85-4d9c-9668-e31f3d641ac6.webp', 'Stock', 'visible'),
(7, 'Short Morgan', 49990, 'Producto veraniego de categoria Polleras y Shorts, ideal para los dias calidos', 'Polleras y Shorts', 'Negro', 'c3b60a22-79df-48c4-9e00-dc707435ca88.webp', 'Stock', 'visible');

-- --------------------------------------------------------

--
-- Table structure for table `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nombre_usuario` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `pass` varchar(6) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `apellido` varchar(20) NOT NULL,
  `tipo_usario` enum('admin','cliente') NOT NULL,
  `dni` int(11) NOT NULL,
  `direccion` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuario`
--

INSERT INTO `usuario` (`id`, `nombre_usuario`, `email`, `pass`, `nombre`, `apellido`, `tipo_usario`, `dni`, `direccion`) VALUES
(1, 'mlopez', 'mlopez@gmail.com', '123456', 'María', 'López', 'cliente', 40123654, 'Av. San Martín 123'),
(2, 'jperez', 'jperez@hotmail.com', '123456', 'Juan', 'Pérez', 'cliente', 38256987, 'Calle Belgrano 456'),
(3, 'arodriguez', 'arodriguez@yahoo.com', '123456', 'Ana', 'Rodríguez', 'cliente', 39547896, 'Mitre 789'),
(4, 'lfernandez', 'lfernandez@gmail.com', '123456', 'Lucía', 'Fernández', 'cliente', 41758963, 'Sarmiento 987'),
(5, 'cmartinez', 'cmartinez@gmail.com', '123456', 'Carlos', 'Martínez', 'cliente', 36254879, 'Italia 354'),
(6, 'mgonzalez', 'mgonzalez@hotmail.com', '123456', 'Martín', 'González', 'cliente', 37125984, 'Rivadavia 812'),
(7, 'nramirez', 'nramirez@gmail.com', '123456', 'Natalia', 'Ramírez', 'cliente', 40256321, 'Colón 1423'),
(8, 'rgarcia', 'rgarcia@gmail.com', '123456', 'Roberto', 'García', 'cliente', 39485623, 'Saavedra 300'),
(9, 'jmorales', 'jmorales@gmail.com', '123456', 'Julia', 'Morales', 'cliente', 38879654, '9 de Julio 250'),
(10, 'eperez', 'eperez@gmail.com', '123456', 'Esteban', 'Pérez', 'cliente', 40587645, 'San Juan 1800'),
(11, 'vbenitez', 'vbenitez@gmail.com', '123456', 'Valeria', 'Benítez', 'cliente', 39214578, 'Lavalle 77'),
(12, 'fsosa', 'fsosa@yahoo.com', '123456', 'Fernando', 'Sosa', 'cliente', 38521497, 'Bouchard 134'),
(13, 'drodriguez', 'drodriguez@gmail.com', '123456', 'Diego', 'Rodríguez', 'cliente', 40124567, 'Alsina 985'),
(14, 'cpaz', 'cpaz@gmail.com', '123456', 'Claudia', 'Paz', 'cliente', 37985642, 'Roca 1111'),
(15, 'admin', 'admin@coast.com', '123456', 'Admin', 'Sistema', 'admin', 11111111, 'Sistema');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `compras`
--
ALTER TABLE `compras`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_compras_id_usuario` (`id_usuario`);

--
-- Indexes for table `datos_pago`
--
ALTER TABLE `datos_pago`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_id_usuario` (`id_usuario`),
  ADD KEY `fk_datos_pago_id_compra` (`id_compra`);

--
-- Indexes for table `detalles_compras`
--
ALTER TABLE `detalles_compras`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_id_producto` (`id_producto`),
  ADD KEY `fk_id_compra` (`id_compra`);

--
-- Indexes for table `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `un_nombre_producto` (`nombre`);

--
-- Indexes for table `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `un_email_usuario` (`email`),
  ADD UNIQUE KEY `un_dni_usuario` (`dni`),
  ADD UNIQUE KEY `un_nombre_usuario_usuario` (`nombre_usuario`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `compras`
--
ALTER TABLE `compras`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `datos_pago`
--
ALTER TABLE `datos_pago`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `detalles_compras`
--
ALTER TABLE `detalles_compras`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `producto`
--
ALTER TABLE `producto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `compras`
--
ALTER TABLE `compras`
  ADD CONSTRAINT `fk_compras_id_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`);

--
-- Constraints for table `datos_pago`
--
ALTER TABLE `datos_pago`
  ADD CONSTRAINT `fk_datos_pago_id_compra` FOREIGN KEY (`id_compra`) REFERENCES `compras` (`id`),
  ADD CONSTRAINT `fk_id_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`);

--
-- Constraints for table `detalles_compras`
--
ALTER TABLE `detalles_compras`
  ADD CONSTRAINT `fk_id_compra` FOREIGN KEY (`id_compra`) REFERENCES `compras` (`id`),
  ADD CONSTRAINT `fk_id_producto` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
