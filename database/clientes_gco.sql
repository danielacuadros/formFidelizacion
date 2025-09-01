-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-09-2025 a las 05:52:16
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `clientes_gco`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ciudades`
--

CREATE TABLE `ciudades` (
  `id_ciudad` int(11) NOT NULL,
  `nombre_ciudad` varchar(100) NOT NULL,
  `departamento` varchar(100) DEFAULT NULL,
  `pais` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ciudades`
--

INSERT INTO `ciudades` (`id_ciudad`, `nombre_ciudad`, `departamento`, `pais`) VALUES
(1, 'Bogotá', 'Bogotá D.C.', 'Colombia'),
(2, 'Medellín', 'Antioquia', 'Colombia'),
(3, 'Cali', 'Valle del Cauca', 'Colombia'),
(4, 'Barranquilla', 'Atlántico', 'Colombia'),
(5, 'Cartagena', 'Bolívar', 'Colombia'),
(6, 'Bucaramanga', 'Santander', 'Colombia'),
(7, 'Pereira', 'Risaralda', 'Colombia'),
(8, 'Pasto', 'Nariño', 'Colombia'),
(9, 'Lima', 'Lima', 'Perú'),
(10, 'Quito', 'Pichincha', 'Ecuador'),
(11, 'Guayaquil', 'Guayas', 'Ecuador'),
(12, 'Ciudad de Guatemala', 'Guatemala', 'Guatemala');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `id` bigint(20) NOT NULL,
  `tipo_identificacion` varchar(10) NOT NULL,
  `numero_identificacion` varchar(20) NOT NULL,
  `nombres` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `direccion` varchar(255) NOT NULL,
  `id_ciudad` int(11) NOT NULL,
  `id_marca` int(11) NOT NULL,
  `ciudad` varchar(100) DEFAULT NULL,
  `departamento` varchar(100) DEFAULT NULL,
  `marca` varchar(100) DEFAULT NULL,
  `pais` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`id`, `tipo_identificacion`, `numero_identificacion`, `nombres`, `apellidos`, `fecha_nacimiento`, `direccion`, `id_ciudad`, `id_marca`, `ciudad`, `departamento`, `marca`, `pais`) VALUES
(1, 'CC', '1234567999', 'Daniela', 'Cuadros', '1998-04-07', 'calle 73 #49-20', 2, 1, NULL, NULL, NULL, NULL),
(2, 'CC', '12345678', 'Ana María', 'García López', '1990-03-15', 'Calle 45 #23-67', 1, 1, NULL, NULL, NULL, NULL),
(3, 'CC', '23456789', 'Carlos Eduardo', 'Rodríguez Silva', '1985-07-22', 'Carrera 78 #12-34', 2, 2, NULL, NULL, NULL, NULL),
(4, 'PPT', '34567890', 'María Fernanda', 'Martínez Peña', '1992-11-08', 'Avenida 6 #89-45', 3, 3, NULL, NULL, NULL, NULL),
(5, 'CE', '45678901', 'Juan Pablo', 'Hernández Castro', '1988-05-30', 'Calle 123 #56-78', 4, 4, NULL, NULL, NULL, NULL),
(6, 'CC', '56789012', 'Laura Camila', 'Jiménez Vargas', '1993-12-14', 'Carrera 45 #67-89', 5, 5, NULL, NULL, NULL, NULL),
(7, 'CC', '67890123', 'Andrés Felipe', 'Morales Ruiz', '1987-09-03', 'Calle 67 #34-12', 6, 6, NULL, NULL, NULL, NULL),
(8, 'PPT', '78901234', 'Sofía Isabel', 'Ramírez Torres', '1991-04-18', 'Avenida 89 #23-45', 7, 7, NULL, NULL, NULL, NULL),
(9, 'CC', '89012345', 'Diego Alejandro', 'Sánchez Medina', '1989-08-25', 'Carrera 12 #78-90', 8, 1, NULL, NULL, NULL, NULL),
(10, 'CE', '90123456', 'Valentina', 'González Ortiz', '1994-02-11', 'Calle 34 #45-67', 9, 2, NULL, NULL, NULL, NULL),
(11, 'CC', '01234567', 'Miguel Ángel', 'Pérez Gómez', '1986-06-07', 'Avenida 56 #78-12', 10, 3, NULL, NULL, NULL, NULL),
(12, 'CC', '11234567', 'Carolina', 'López Díaz', '1992-10-20', 'Carrera 23 #34-56', 11, 4, NULL, NULL, NULL, NULL),
(13, 'PPT', '21234567', 'Sebastián', 'Vargas Molina', '1990-01-13', 'Calle 78 #90-12', 12, 5, NULL, NULL, NULL, NULL),
(14, 'CC', '31234567', 'Natalia Andrea', 'Castro Restrepo', '1988-12-05', 'Avenida 34 #12-78', 1, 6, NULL, NULL, NULL, NULL),
(15, 'CE', '41234567', 'Ricardo', 'Moreno Aguilar', '1993-07-28', 'Carrera 67 #89-23', 2, 7, NULL, NULL, NULL, NULL),
(16, 'CC', '51234567', 'Isabella', 'Torres Mejía', '1991-03-16', 'Calle 89 #45-67', 3, 1, NULL, NULL, NULL, NULL),
(17, 'CC', '61234567', 'Alejandro', 'Ruiz Cardona', '1987-11-09', 'Avenida 12 #56-34', 4, 2, NULL, NULL, NULL, NULL),
(18, 'PPT', '71234567', 'Camila Andrea', 'Velásquez Arango', '1994-05-22', 'Carrera 45 #23-78', 5, 3, NULL, NULL, NULL, NULL),
(19, 'CC', '81234567', 'Javier Esteban', 'Giraldo Henao', '1989-09-14', 'Calle 56 #67-90', 6, 4, NULL, NULL, NULL, NULL),
(20, 'CE', '91234567', 'Mariana', 'Ospina Cadavid', '1992-04-03', 'Avenida 78 #34-12', 7, 5, NULL, NULL, NULL, NULL),
(21, 'CC', '02345678', 'David Santiago', 'Quintero Bedoya', '1986-08-17', 'Carrera 90 #45-23', 8, 6, NULL, NULL, NULL, NULL),
(22, 'CC', '12345679', 'Andrea Lucía', 'Arbeláez Villa', '1993-06-30', 'Calle 23 #78-45', 9, 7, NULL, NULL, NULL, NULL),
(23, 'PPT', '22345678', 'Fernando', 'Echeverri Posada', '1988-02-24', 'Avenida 45 #67-89', 10, 1, NULL, NULL, NULL, NULL),
(24, 'CC', '32345678', 'Daniela', 'Parra Zuluaga', '1991-10-12', 'Carrera 67 #12-34', 11, 2, NULL, NULL, NULL, NULL),
(25, 'CE', '42345678', 'Nicolás', 'Jaramillo Hoyos', '1990-07-06', 'Calle 12 #89-56', 12, 3, NULL, NULL, NULL, NULL),
(26, 'CC', '52345678', 'Paola Andrea', 'Salazar Correa', '1987-12-19', 'Avenida 34 #23-67', 1, 4, NULL, NULL, NULL, NULL),
(27, 'CC', '62345678', 'Mauricio', 'Betancur Mesa', '1994-03-08', 'Carrera 56 #78-12', 2, 5, NULL, NULL, NULL, NULL),
(28, 'PPT', '72345678', 'Juliana', 'Montoya Gómez', '1989-11-25', 'Calle 78 #34-90', 3, 6, NULL, NULL, NULL, NULL),
(29, 'CC', '82345678', 'Esteban', 'Ríos Palacio', '1992-05-14', 'Avenida 90 #45-23', 4, 7, NULL, NULL, NULL, NULL),
(30, 'CE', '92345678', 'Claudia Patricia', 'Uribe Franco', '1988-09-01', 'Carrera 12 #67-45', 5, 1, NULL, NULL, NULL, NULL),
(31, 'CC', '03456789', 'Álvaro José', 'Escobar Toro', '1991-01-27', 'Calle 45 #23-89', 6, 2, NULL, NULL, NULL, NULL),
(32, 'CC', '1234567992', 'Ana', 'Cuadros', '2002-02-01', 'calle 73 #49-20', 3, 2, NULL, NULL, NULL, NULL),
(35, 'CC', '123456777', 'Daniela', 'Cuadros', '2003-02-01', 'calle 73 #49-20', 9, 2, NULL, NULL, NULL, NULL),
(36, 'PPT', '15236478', 'Jin', 'Rendon', '1996-10-14', 'barrio olimpico', 3, 1, NULL, NULL, NULL, NULL),
(37, 'CE', '12345678456', 'Karina', 'Cuadros', '2002-02-02', 'calle 72', 11, 4, NULL, NULL, NULL, NULL),
(38, 'CC', '987456321', 'Eiren', 'Guarnizo', '2006-02-01', 'Calle 73 #49-20', 5, 7, NULL, NULL, NULL, NULL),
(40, 'CC', '1234567993', 'Pipe', 'Cuadros', '2005-05-05', 'calle 73 #49-20', 2, 1, NULL, NULL, NULL, NULL),
(41, 'CC', '1234567995', 'Daniela', 'Cuadros', '1999-05-03', 'calle 73 #49-20', 2, 2, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `marcas`
--

CREATE TABLE `marcas` (
  `id_marca` int(11) NOT NULL,
  `nombre_marca` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `marcas`
--

INSERT INTO `marcas` (`id_marca`, `nombre_marca`) VALUES
(1, 'NAF NAF'),
(2, 'RIFLE'),
(3, 'AMERICANINO'),
(4, 'CHEVIGNON'),
(5, 'ESPRIT'),
(6, 'AMERICAN EAGLE'),
(7, 'MANGO');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `ciudades`
--
ALTER TABLE `ciudades`
  ADD PRIMARY KEY (`id_ciudad`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `numero_identificacion` (`numero_identificacion`);

--
-- Indices de la tabla `marcas`
--
ALTER TABLE `marcas`
  ADD PRIMARY KEY (`id_marca`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `ciudades`
--
ALTER TABLE `ciudades`
  MODIFY `id_ciudad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT de la tabla `marcas`
--
ALTER TABLE `marcas`
  MODIFY `id_marca` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
