-- MySQL dump 10.13  Distrib 5.7.43, for Win64 (x86_64)
--
-- Host: localhost    Database: bdpsico
-- ------------------------------------------------------
-- Server version	5.7.43-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `codigos_administrador`
--

DROP TABLE IF EXISTS `codigos_administrador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `codigos_administrador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `codigos_administrador`
--

LOCK TABLES `codigos_administrador` WRITE;
/*!40000 ALTER TABLE `codigos_administrador` DISABLE KEYS */;
INSERT INTO `codigos_administrador` VALUES (1,'qwer');
/*!40000 ALTER TABLE `codigos_administrador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado_cuenta_usuario`
--

DROP TABLE IF EXISTS `estado_cuenta_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `estado_cuenta_usuario` (
  `EstadoCuentaID` int(11) NOT NULL AUTO_INCREMENT,
  `UsuarioID` int(11) NOT NULL,
  `EstadoCuenta` varchar(20) NOT NULL,
  PRIMARY KEY (`EstadoCuentaID`),
  KEY `UsuarioID` (`UsuarioID`),
  CONSTRAINT `estado_cuenta_usuario_ibfk_1` FOREIGN KEY (`UsuarioID`) REFERENCES `usuario` (`UsuarioID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_cuenta_usuario`
--

LOCK TABLES `estado_cuenta_usuario` WRITE;
/*!40000 ALTER TABLE `estado_cuenta_usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `estado_cuenta_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_accesos`
--

DROP TABLE IF EXISTS `registro_accesos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registro_accesos` (
  `RegistroID` int(11) NOT NULL AUTO_INCREMENT,
  `UsuarioID` int(11) NOT NULL,
  `FechaHoraEntrada` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `FechaHoraSalida` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`RegistroID`),
  KEY `UsuarioID` (`UsuarioID`),
  CONSTRAINT `registro_accesos_ibfk_1` FOREIGN KEY (`UsuarioID`) REFERENCES `usuario` (`UsuarioID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_accesos`
--

LOCK TABLES `registro_accesos` WRITE;
/*!40000 ALTER TABLE `registro_accesos` DISABLE KEYS */;
/*!40000 ALTER TABLE `registro_accesos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roles` (
  `RolID` int(11) NOT NULL AUTO_INCREMENT,
  `NombreRol` varchar(255) NOT NULL,
  PRIMARY KEY (`RolID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'admin'),(2,'user');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_01paciente`
--

DROP TABLE IF EXISTS `t_01paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_01paciente` (
  `Id_paciente` int(11) NOT NULL,
  `Nombre` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Apellido` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `DNI` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Fecha_nacimiento` date DEFAULT NULL,
  `Fecha_registro` date DEFAULT NULL,
  `Observaciones` text COLLATE utf8mb4_unicode_ci,
  `Id_padre` int(11) DEFAULT NULL,
  `Id_genero` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id_paciente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_01paciente`
--

LOCK TABLES `t_01paciente` WRITE;
/*!40000 ALTER TABLE `t_01paciente` DISABLE KEYS */;
INSERT INTO `t_01paciente` VALUES (1,'Ana','García','12345678','2010-05-15','2023-07-01','Sin alergias conocidas',1,2),(2,'Juan','López','23456789','2012-08-20','2023-07-05','Problemas de concentración en clase',2,1),(3,'María','Martínez','34567890','2011-03-10','2023-07-10','Fobia a los espacios cerrados',3,2),(4,'Pedro','Rodríguez','45678901','2013-11-25','2023-07-15','Intereses en música y arte',4,1),(5,'Luisa','Pérez','56789012','2010-07-30','2023-07-20','Dificultades en matemáticas',5,2),(6,'Carlos','Gómez','67890123','2012-01-12','2023-07-25','Historial de déficit de atención',2,1),(7,'Laura','Díaz','78901234','2013-06-05','2023-08-01','Intereses en deportes y actividad física',6,2),(8,'José','Hernández','89012345','2011-09-18','2023-08-05','Experiencias de ansiedad social',7,1),(9,'Sofía','Ramírez','90123456','2010-12-08','2023-08-10','Dificultades en lectura comprensiva',8,2),(10,'Andrés','Torres','01234567','2012-02-28','2023-08-15','Historial de terapia de lenguaje',9,1);
/*!40000 ALTER TABLE `t_01paciente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_02direccionpaciente`
--

DROP TABLE IF EXISTS `t_02direccionpaciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_02direccionpaciente` (
  `id_direccion` int(11) NOT NULL,
  `id_paciente` int(11) DEFAULT NULL,
  `direccion` text COLLATE utf8mb4_unicode_ci,
  `ciudad` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `estado` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `codigo_postal` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_direccion`),
  KEY `id_paciente` (`id_paciente`),
  CONSTRAINT `t_02direccionpaciente_ibfk_1` FOREIGN KEY (`id_paciente`) REFERENCES `t_01paciente` (`Id_paciente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_02direccionpaciente`
--

LOCK TABLES `t_02direccionpaciente` WRITE;
/*!40000 ALTER TABLE `t_02direccionpaciente` DISABLE KEYS */;
INSERT INTO `t_02direccionpaciente` VALUES (1,1,'Calle 123, Colonia Primavera','Ciudad de México','CDMX','12345'),(2,1,'Av. Central, Urbanización Los Pinos','Lima','Lima','54321'),(3,3,'Paseo del Sol, Barrio Vista Hermosa','Guadalajara','Jalisco','67890'),(4,4,'Rua das Flores, Bairro Centro','São Paulo','São Paulo','98765'),(5,5,'123 Main Street, Apartment 4B','New York','NY','54321'),(6,6,'Carrera 45, Conjunto Residencial Los Laureles','Bogotá','Bogotá','12345'),(7,7,'Avenida del Deporte, Sector Los Olivos','Santiago','Metropolitana','67890'),(8,8,'Calle 18, Barrio San Juan','San Salvador','San Salvador','98765'),(9,9,'Avenida Principal, Urbanización Los Robles','Caracas','Distrito Capital','54321'),(10,10,'Rua das Pedras, Condomínio Recanto Feliz','Rio de Janeiro','Rio de Janeiro','12345'),(11,10,'Avenida Central, Conjunto Residencial Los Pájaros','Quito','Pichincha','67890');
/*!40000 ALTER TABLE `t_02direccionpaciente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_02genero`
--

DROP TABLE IF EXISTS `t_02genero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_02genero` (
  `Id_genero` int(11) NOT NULL,
  `Nombre` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`Id_genero`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_02genero`
--

LOCK TABLES `t_02genero` WRITE;
/*!40000 ALTER TABLE `t_02genero` DISABLE KEYS */;
INSERT INTO `t_02genero` VALUES (1,'Masculino'),(2,'Femenino'),(4,'Otro');
/*!40000 ALTER TABLE `t_02genero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_03padres`
--

DROP TABLE IF EXISTS `t_03padres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_03padres` (
  `id_padre` int(11) NOT NULL,
  `nombres` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `apellido` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `telefono` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ocupacion` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id_nivel_educacion` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_padre`),
  KEY `id_nivel_educacion` (`id_nivel_educacion`),
  CONSTRAINT `t_03padres_ibfk_1` FOREIGN KEY (`id_nivel_educacion`) REFERENCES `t_05niveleseducacion` (`id_nivel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_03padres`
--

LOCK TABLES `t_03padres` WRITE;
/*!40000 ALTER TABLE `t_03padres` DISABLE KEYS */;
INSERT INTO `t_03padres` VALUES (1,'Juan','García','123-456-7890','Ingeniero',4),(2,'María','López','987-654-3210','Profesora',4),(3,'Carlos','Martínez','555-123-4567','Médico',4),(4,'Laura','Rodríguez','777-888-9999','Ama de casa',2),(5,'Ana','Pérez','222-333-4444','Arquitecta',3),(6,'José','Gómez','666-777-8888','Contador',4),(7,'Sofía','Díaz','444-555-6666','Empresaria',2),(8,'Andrés','Hernández','888-999-0000','Chef',3),(9,'Luis','Ramírez','111-222-3333','Economista',4),(10,'Elena','Torres','333-444-5555','Psicóloga',3);
/*!40000 ALTER TABLE `t_03padres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_04direccionpadre`
--

DROP TABLE IF EXISTS `t_04direccionpadre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_04direccionpadre` (
  `id_direccion` int(11) NOT NULL,
  `id_padre` int(11) DEFAULT NULL,
  `direccion` text COLLATE utf8mb4_unicode_ci,
  `ciudad` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id_estado_vivienda` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_direccion`),
  KEY `id_padre` (`id_padre`),
  KEY `id_estado_vivienda` (`id_estado_vivienda`),
  CONSTRAINT `t_04direccionpadre_ibfk_1` FOREIGN KEY (`id_padre`) REFERENCES `t_03padres` (`id_padre`),
  CONSTRAINT `t_04direccionpadre_ibfk_2` FOREIGN KEY (`id_estado_vivienda`) REFERENCES `t_12estadovivienda` (`id_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_04direccionpadre`
--

LOCK TABLES `t_04direccionpadre` WRITE;
/*!40000 ALTER TABLE `t_04direccionpadre` DISABLE KEYS */;
INSERT INTO `t_04direccionpadre` VALUES (1,1,'Calle 123, Colonia Primavera','Ciudad de México',1),(2,1,'Av. Central, Urbanización Los Pinos','Lima',2),(3,2,'Paseo del Sol, Barrio Vista Hermosa','Guadalajara',2),(4,3,'Rua das Flores, Bairro Centro','São Paulo',1),(5,4,'123 Main Street, Apartment 4B','New York',2),(6,5,'Carrera 45, Conjunto Residencial Los Laureles','Bogotá',1),(7,6,'Avenida del Deporte, Sector Los Olivos','Santiago',2),(8,7,'Calle 18, Barrio San Juan','San Salvador',1),(9,8,'Avenida Principal, Urbanización Los Robles','Caracas',2),(10,9,'Rua das Pedras, Condomínio Recanto Feliz','Rio de Janeiro',2),(11,9,'Rua das Flores, Apartamento 2C','Rio de Janeiro',2),(12,10,'Avenida Central, Edificio Azul','Lima',1),(13,10,'Calle 15, Urbanización Bella Vista','Lima',1);
/*!40000 ALTER TABLE `t_04direccionpadre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_05niveleseducacion`
--

DROP TABLE IF EXISTS `t_05niveleseducacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_05niveleseducacion` (
  `id_nivel` int(11) NOT NULL,
  `nivel` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id_nivel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_05niveleseducacion`
--

LOCK TABLES `t_05niveleseducacion` WRITE;
/*!40000 ALTER TABLE `t_05niveleseducacion` DISABLE KEYS */;
INSERT INTO `t_05niveleseducacion` VALUES (1,'Educación Inicial'),(2,'Educación Primaria'),(3,'Educación Secundaria'),(4,'Educación Superior');
/*!40000 ALTER TABLE `t_05niveleseducacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_06datosembarazo`
--

DROP TABLE IF EXISTS `t_06datosembarazo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_06datosembarazo` (
  `id_embarazo` int(11) NOT NULL,
  `id_paciente` int(11) DEFAULT NULL,
  `id_tipo_parto` int(11) DEFAULT NULL,
  `inicio_del_embarazo` date DEFAULT NULL,
  `fecha_fin_del_embarazo` date DEFAULT NULL,
  `semana_gestacion` int(11) DEFAULT NULL,
  `peso_al_nacer` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`id_embarazo`),
  KEY `id_paciente` (`id_paciente`),
  KEY `id_tipo_parto` (`id_tipo_parto`),
  CONSTRAINT `t_06datosembarazo_ibfk_1` FOREIGN KEY (`id_paciente`) REFERENCES `t_01paciente` (`Id_paciente`),
  CONSTRAINT `t_06datosembarazo_ibfk_2` FOREIGN KEY (`id_tipo_parto`) REFERENCES `t_08tipoparto` (`id_tipo_parto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_06datosembarazo`
--

LOCK TABLES `t_06datosembarazo` WRITE;
/*!40000 ALTER TABLE `t_06datosembarazo` DISABLE KEYS */;
INSERT INTO `t_06datosembarazo` VALUES (1,1,1,'2010-02-15','2010-10-25',35,3.25),(2,2,2,'2012-05-20','2012-12-10',38,3.70),(3,3,1,'2011-12-10','2012-07-15',32,2.90),(4,4,3,'2013-08-01','2013-03-10',40,3.80),(5,5,2,'2010-06-30','2010-03-05',37,3.45),(6,6,1,'2012-01-05','2012-09-15',38,3.60),(7,7,3,'2013-04-18','2013-12-01',39,3.75),(8,8,2,'2011-07-25','2011-04-10',36,3.30),(9,9,1,'2010-10-10','2011-05-20',34,3.15),(10,10,2,'2012-03-15','2012-11-30',40,3.90);
/*!40000 ALTER TABLE `t_06datosembarazo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_08tipoparto`
--

DROP TABLE IF EXISTS `t_08tipoparto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_08tipoparto` (
  `id_tipo_parto` int(11) NOT NULL,
  `tipo` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_tipo_parto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_08tipoparto`
--

LOCK TABLES `t_08tipoparto` WRITE;
/*!40000 ALTER TABLE `t_08tipoparto` DISABLE KEYS */;
INSERT INTO `t_08tipoparto` VALUES (1,'Parto Natural'),(2,'Cesárea'),(3,'Parto Inducido'),(4,'Parto por Fórceps'),(5,'Parto en el Agua');
/*!40000 ALTER TABLE `t_08tipoparto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_09enfermedadesembarazo`
--

DROP TABLE IF EXISTS `t_09enfermedadesembarazo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_09enfermedadesembarazo` (
  `id_enfermedad` int(11) NOT NULL,
  `id_embarazo` int(11) DEFAULT NULL,
  `enfermedad` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id_enfermedad`),
  KEY `id_embarazo` (`id_embarazo`),
  CONSTRAINT `t_09enfermedadesembarazo_ibfk_1` FOREIGN KEY (`id_embarazo`) REFERENCES `t_06datosembarazo` (`id_embarazo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_09enfermedadesembarazo`
--

LOCK TABLES `t_09enfermedadesembarazo` WRITE;
/*!40000 ALTER TABLE `t_09enfermedadesembarazo` DISABLE KEYS */;
INSERT INTO `t_09enfermedadesembarazo` VALUES (1,1,'Hipertensión gestacional'),(2,2,'Diabetes gestacional'),(3,3,'Infección urinaria'),(4,4,'Preeclampsia'),(5,5,'Anemia'),(6,6,'Síndrome HELLP'),(7,7,'Infección vaginal'),(8,8,'Colestasis del embarazo'),(9,9,'Malformaciones fetales'),(10,10,'Hiperémesis gravídica');
/*!40000 ALTER TABLE `t_09enfermedadesembarazo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_10historialeducativo`
--

DROP TABLE IF EXISTS `t_10historialeducativo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_10historialeducativo` (
  `id_historial` int(11) NOT NULL,
  `id_paciente` int(11) DEFAULT NULL,
  `id_institucion` int(11) DEFAULT NULL,
  `adaptacion` text COLLATE utf8mb4_unicode_ci,
  `relacion_docentes` text COLLATE utf8mb4_unicode_ci,
  `relacion_compañeros` text COLLATE utf8mb4_unicode_ci,
  `repitencia_escolar` text COLLATE utf8mb4_unicode_ci,
  `cambios_escuelas` text COLLATE utf8mb4_unicode_ci,
  `cambios_maestros` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id_historial`),
  KEY `id_paciente` (`id_paciente`),
  KEY `id_institucion` (`id_institucion`),
  CONSTRAINT `t_10historialeducativo_ibfk_1` FOREIGN KEY (`id_paciente`) REFERENCES `t_01paciente` (`Id_paciente`),
  CONSTRAINT `t_10historialeducativo_ibfk_2` FOREIGN KEY (`id_institucion`) REFERENCES `t_11caracteristicainstitu` (`id_institucion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_10historialeducativo`
--

LOCK TABLES `t_10historialeducativo` WRITE;
/*!40000 ALTER TABLE `t_10historialeducativo` DISABLE KEYS */;
INSERT INTO `t_10historialeducativo` VALUES (1,1,1,'Se adaptó bien a su nuevo entorno escolar.','Tiene una buena relación con sus docentes.','Se lleva bien con sus compañeros de clase.','No ha tenido repitencias escolares.','No ha cambiado de escuela.','Ha tenido un cambio de maestro en el último año.'),(2,2,2,'Tuvo dificultades en su adaptación inicial.','Presenta algunos conflictos con ciertos docentes.','Tiene amistades cercanas, pero también problemas con algunos compañeros.','Ha repetido un año escolar debido a problemas de aprendizaje.','Cambiado de escuela una vez.','Ha tenido cambios de maestros en múltiples ocasiones.'),(3,3,1,'Se adaptó sin problemas a la institución.','Mantiene una relación cercana con sus docentes.','Tiene un grupo de amigos estable en clase.','No ha tenido repitencias escolares.','No ha cambiado de escuela.','Ha tenido cambios de maestros ocasionales.'),(4,4,3,'Necesitó apoyo para su adaptación.','Tiene una relación neutral con sus docentes.','A veces se siente excluido por sus compañeros.','Ha repetido un año escolar debido a problemas personales.','Cambiado de escuela una vez.','Ha tenido cambios de maestros en los últimos dos años.'),(5,5,2,'Se adaptó rápidamente a la nueva escuela.','Tiene una excelente relación con sus docentes.','Es muy sociable y se lleva bien con todos.','No ha tenido repitencias escolares.','No ha cambiado de escuela.','Ha tenido cambios de maestros de manera ocasional.'),(6,6,2,'Requirió apoyo emocional en su adaptación.','Tiene una relación cordial con sus docentes.','Tiene un pequeño grupo de amigos en clase.','Ha repetido un año escolar por motivos de salud.','Cambiado de escuela una vez.','Ha tenido cambios de maestros en el último año.'),(7,7,3,'Mostró ciertas dificultades en la adaptación.','Tiene una relación mixta con sus docentes.','Ha tenido altibajos en sus relaciones con los compañeros.','No ha tenido repitencias escolares.','Cambiado de escuela una vez.','Ha tenido cambios de maestros en los últimos años.'),(8,8,2,'Adaptación gradual a la institución.','Tiene una relación regular con sus docentes.','Se lleva bien con la mayoría de sus compañeros.','Ha repetido un año escolar por dificultades de aprendizaje.','Cambiado de escuela una vez.','Ha tenido cambios de maestros de manera ocasional.'),(9,9,1,'Requirió apoyo en su adaptación inicial.','Mantiene una relación cercana con sus docentes.','Es popular y tiene muchas amistades en clase.','No ha tenido repitencias escolares.','No ha cambiado de escuela.','Ha tenido cambios de maestros en el último año.'),(10,10,2,'Se adaptó sin problemas a la institución.','Tiene una relación neutral con sus docentes.','Tiene un grupo pequeño de amigos cercanos.','No ha tenido repitencias escolares.','No ha cambiado de escuela.','Ha tenido cambios de maestros de manera ocasional.');
/*!40000 ALTER TABLE `t_10historialeducativo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_11caracteristicainstitu`
--

DROP TABLE IF EXISTS `t_11caracteristicainstitu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_11caracteristicainstitu` (
  `id_institucion` int(11) NOT NULL,
  `institucion` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id_institucion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_11caracteristicainstitu`
--

LOCK TABLES `t_11caracteristicainstitu` WRITE;
/*!40000 ALTER TABLE `t_11caracteristicainstitu` DISABLE KEYS */;
INSERT INTO `t_11caracteristicainstitu` VALUES (1,'Institución privada'),(2,'Institución pública de gestión directa'),(3,'Institución pública de gestión privada');
/*!40000 ALTER TABLE `t_11caracteristicainstitu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_12estadovivienda`
--

DROP TABLE IF EXISTS `t_12estadovivienda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_12estadovivienda` (
  `id_estado` int(11) NOT NULL,
  `estado_vivienda` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_12estadovivienda`
--

LOCK TABLES `t_12estadovivienda` WRITE;
/*!40000 ALTER TABLE `t_12estadovivienda` DISABLE KEYS */;
INSERT INTO `t_12estadovivienda` VALUES (1,'Buen estado'),(2,'Regular estado'),(3,'Mal estado');
/*!40000 ALTER TABLE `t_12estadovivienda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_12infofamiliar`
--

DROP TABLE IF EXISTS `t_12infofamiliar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_12infofamiliar` (
  `id_informacion_familiar` int(11) NOT NULL,
  `id_paciente` int(11) DEFAULT NULL,
  `ambiente_familiar` text COLLATE utf8mb4_unicode_ci,
  `union_estable` enum('Sí','No') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tiempo_convivencia` text COLLATE utf8mb4_unicode_ci,
  `ingresos_padre` decimal(10,2) DEFAULT NULL,
  `ingresos_madre` decimal(10,2) DEFAULT NULL,
  `expectativas_padres` text COLLATE utf8mb4_unicode_ci,
  `dia_comun_menor` text COLLATE utf8mb4_unicode_ci,
  `id_estado_vivienda` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_informacion_familiar`),
  KEY `id_paciente` (`id_paciente`),
  KEY `id_estado_vivienda` (`id_estado_vivienda`),
  CONSTRAINT `t_12infofamiliar_ibfk_1` FOREIGN KEY (`id_paciente`) REFERENCES `t_01paciente` (`Id_paciente`),
  CONSTRAINT `t_12infofamiliar_ibfk_2` FOREIGN KEY (`id_estado_vivienda`) REFERENCES `t_12estadovivienda` (`id_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_12infofamiliar`
--

LOCK TABLES `t_12infofamiliar` WRITE;
/*!40000 ALTER TABLE `t_12infofamiliar` DISABLE KEYS */;
INSERT INTO `t_12infofamiliar` VALUES (1,1,'Ambiente familiar cálido y acogedor.','Sí','4 años',1500.00,1200.00,'Esperan que el menor destaque en sus estudios.','Día común incluye actividades escolares y juegos.',1),(2,2,'Hogar con armonía y respeto.','Sí','8 años',1800.00,900.00,'Desean que el menor sea autodisciplinado.','Día común implica actividades escolares y lectura.',2),(3,3,'Ambiente familiar lleno de amor y apoyo.','Sí','6 años',2000.00,1600.00,'Esperan que el menor desarrolle habilidades sociales.','Día común involucra juegos, tareas escolares y salidas.',2),(4,4,'Hogar con respeto a la individualidad.','No','10 años',2200.00,2000.00,'Desean que el menor tenga éxito académico.','Día común abarca estudio, deportes y tiempo en familia.',2),(5,5,'Ambiente familiar con comunicación abierta.','Sí','5 años',1800.00,1100.00,'Esperan que el menor sea creativo.','Día común incluye estudio, juegos y actividades al aire libre.',1),(6,1,'Ambiente tranquilo y afectuoso en casa','Sí','10 años',1500.00,1200.00,'Esperamos que termine su educación secundaria','Jugar en el parque',1),(7,2,'Hogar con gran participación en actividades culturales','No','7 años',2000.00,1800.00,'Queremos que aprenda un idioma extranjero','Ver películas en familia',2),(8,3,'Familia unida y comprometida con actividades deportivas','Sí','12 años',1800.00,1600.00,'Esperamos que destaque en el ámbito escolar','Visitar a los abuelos los fines de semana',3),(9,4,'Ambiente tenso debido a diferencias entre los padres','No','5 años',1400.00,1300.00,'Queremos que mejore su rendimiento académico','Jugar videojuegos',1),(20,5,'Casa con muchas actividades al aire libre','Sí','8 años',1700.00,1500.00,'Esperamos que sea un líder en su grupo escolar','Salir en bicicleta los domingos',2);
/*!40000 ALTER TABLE `t_12infofamiliar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_13datosesion`
--

DROP TABLE IF EXISTS `t_13datosesion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_13datosesion` (
  `id_sesiones` int(11) NOT NULL,
  `id_paciente` int(11) DEFAULT NULL,
  `fecha_sesion` date DEFAULT NULL,
  `hora_sesion` time DEFAULT NULL,
  `duracion` int(11) DEFAULT NULL,
  `id_tipo_sesion` int(11) DEFAULT NULL,
  `id_desarrollo_psicomotor` int(11) DEFAULT NULL,
  `id_desarrollo_lenguaje` int(11) DEFAULT NULL,
  `observacion` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id_sesiones`),
  KEY `id_paciente` (`id_paciente`),
  KEY `id_tipo_sesion` (`id_tipo_sesion`),
  KEY `id_desarrollo_psicomotor` (`id_desarrollo_psicomotor`),
  KEY `id_desarrollo_lenguaje` (`id_desarrollo_lenguaje`),
  CONSTRAINT `t_13datosesion_ibfk_1` FOREIGN KEY (`id_paciente`) REFERENCES `t_01paciente` (`Id_paciente`),
  CONSTRAINT `t_13datosesion_ibfk_2` FOREIGN KEY (`id_tipo_sesion`) REFERENCES `t_14tipossesion` (`id_tipo_sesion`),
  CONSTRAINT `t_13datosesion_ibfk_3` FOREIGN KEY (`id_desarrollo_psicomotor`) REFERENCES `t_16desarrollopsicomotor` (`id_desarrollo_psicomotor`),
  CONSTRAINT `t_13datosesion_ibfk_4` FOREIGN KEY (`id_desarrollo_lenguaje`) REFERENCES `t_15desarrollolenguaje` (`id_desarrollo_lenguaje`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_13datosesion`
--

LOCK TABLES `t_13datosesion` WRITE;
/*!40000 ALTER TABLE `t_13datosesion` DISABLE KEYS */;
INSERT INTO `t_13datosesion` VALUES (1,1,'2023-08-20','10:00:00',60,1,1,1,'Avance en sostén cefálico.'),(2,2,'2023-08-21','15:30:00',45,2,2,3,'Trabajó en habilidades de sentarse y pararse.'),(3,3,'2023-08-22','11:00:00',30,3,4,2,'Enfoque en el gateo y coordinación.'),(4,4,'2023-08-23','09:15:00',50,1,3,4,'Evaluación de la marcha y equilibrio.'),(5,5,'2023-08-24','14:45:00',40,2,5,5,'Trabajo en desarrollo del lenguaje oracional.'),(6,6,'2023-08-25','16:30:00',55,3,1,1,'Observación de avances en sostén cefálico.'),(7,7,'2023-08-26','12:20:00',35,1,2,3,'Continuación en desarrollo de sentarse y pararse.'),(8,8,'2023-08-27','13:45:00',70,2,3,2,'Enfoque en el gateo y coordinación motora.'),(9,9,'2023-08-28','17:00:00',45,3,4,4,'Evaluación del progreso en la marcha y equilibrio.'),(10,10,'2023-08-29','09:30:00',50,1,5,5,'Trabajo en desarrollo del lenguaje oracional.');
/*!40000 ALTER TABLE `t_13datosesion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_14tipossesion`
--

DROP TABLE IF EXISTS `t_14tipossesion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_14tipossesion` (
  `id_tipo_sesion` int(11) NOT NULL,
  `nombre_tipo` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_tipo_sesion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_14tipossesion`
--

LOCK TABLES `t_14tipossesion` WRITE;
/*!40000 ALTER TABLE `t_14tipossesion` DISABLE KEYS */;
INSERT INTO `t_14tipossesion` VALUES (1,'Evaluación Inicial'),(2,'Estimulación Cognitiva'),(3,'Apoyo Escolar'),(4,'Desarrollo Emocional'),(5,'Orientación Vocacional'),(6,'Estrategias de Aprendizaje'),(7,'Reforzamiento Positivo'),(8,'Habilidades Sociales'),(9,'Resolución de Conflictos'),(10,'Terapia Lúdica');
/*!40000 ALTER TABLE `t_14tipossesion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_15desarrollolenguaje`
--

DROP TABLE IF EXISTS `t_15desarrollolenguaje`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_15desarrollolenguaje` (
  `id_desarrollo_lenguaje` int(11) NOT NULL,
  `descripcion` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id_desarrollo_lenguaje`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_15desarrollolenguaje`
--

LOCK TABLES `t_15desarrollolenguaje` WRITE;
/*!40000 ALTER TABLE `t_15desarrollolenguaje` DISABLE KEYS */;
INSERT INTO `t_15desarrollolenguaje` VALUES (1,'Gorjeo'),(2,'Balbuceo'),(3,'Primeras palabras'),(4,'Frases'),(5,'Lenguaje oracional'),(6,'Se le entendió'),(7,'Uso de mímica'),(8,'Presentó tartamudez');
/*!40000 ALTER TABLE `t_15desarrollolenguaje` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_16desarrollopsicomotor`
--

DROP TABLE IF EXISTS `t_16desarrollopsicomotor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_16desarrollopsicomotor` (
  `id_desarrollo_psicomotor` int(11) NOT NULL,
  `descripcion` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id_desarrollo_psicomotor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_16desarrollopsicomotor`
--

LOCK TABLES `t_16desarrollopsicomotor` WRITE;
/*!40000 ALTER TABLE `t_16desarrollopsicomotor` DISABLE KEYS */;
INSERT INTO `t_16desarrollopsicomotor` VALUES (1,'Sostén cefálico'),(2,'Sentarse'),(3,'Pararse'),(4,'Gateo'),(5,'Marcha');
/*!40000 ALTER TABLE `t_16desarrollopsicomotor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_17datosfacturacion`
--

DROP TABLE IF EXISTS `t_17datosfacturacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_17datosfacturacion` (
  `id_facturas` int(11) NOT NULL,
  `id_paciente` int(11) DEFAULT NULL,
  `id_forma_pago` int(11) DEFAULT NULL,
  `fecha_factura` date DEFAULT NULL,
  `tipo_monotributo` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cuil` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `costo` decimal(10,2) DEFAULT NULL,
  `pagado` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id_facturas`),
  KEY `id_paciente` (`id_paciente`),
  KEY `id_forma_pago` (`id_forma_pago`),
  CONSTRAINT `t_17datosfacturacion_ibfk_1` FOREIGN KEY (`id_paciente`) REFERENCES `t_01paciente` (`Id_paciente`),
  CONSTRAINT `t_17datosfacturacion_ibfk_2` FOREIGN KEY (`id_forma_pago`) REFERENCES `t_18formaspago` (`id_forma_pago`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_17datosfacturacion`
--

LOCK TABLES `t_17datosfacturacion` WRITE;
/*!40000 ALTER TABLE `t_17datosfacturacion` DISABLE KEYS */;
INSERT INTO `t_17datosfacturacion` VALUES (1,1,1,'2023-08-01','Monotributo A','20-12345678-6',150.00,1),(2,2,2,'2023-08-05','Monotributo B','27-23456789-7',200.00,1),(3,3,3,'2023-08-10','Monotributo C','30-34567890-8',180.00,0),(4,4,4,'2023-08-15','Monotributo D','24-45678901-9',250.00,0),(5,5,5,'2023-08-20','Monotributo E','22-56789012-0',170.00,1),(6,6,1,'2023-08-25','Monotributo A','25-67890123-1',220.00,0),(7,7,2,'2023-08-30','Monotributo B','23-78901234-2',190.00,1),(8,8,3,'2023-09-01','Monotributo C','26-89012345-3',280.00,0),(9,9,4,'2023-09-05','Monotributo D','29-90123456-4',210.00,1),(10,10,5,'2023-09-10','Monotributo E','21-01234567-5',230.00,0);
/*!40000 ALTER TABLE `t_17datosfacturacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_18formaspago`
--

DROP TABLE IF EXISTS `t_18formaspago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_18formaspago` (
  `id_forma_pago` int(11) NOT NULL,
  `nombre_forma` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_forma_pago`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_18formaspago`
--

LOCK TABLES `t_18formaspago` WRITE;
/*!40000 ALTER TABLE `t_18formaspago` DISABLE KEYS */;
INSERT INTO `t_18formaspago` VALUES (1,'Efectivo'),(2,'Tarjeta de crédito'),(3,'Transferencia bancaria'),(4,'Cheque'),(5,'Pago en línea');
/*!40000 ALTER TABLE `t_18formaspago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuario` (
  `UsuarioID` int(11) NOT NULL AUTO_INCREMENT,
  `NombreUsuario` varchar(255) NOT NULL,
  `Apellido` varchar(255) DEFAULT NULL,
  `Contraseña` varchar(255) NOT NULL,
  `RolID` int(11) DEFAULT NULL,
  `Email` varchar(255) NOT NULL,
  `PreguntaSeguridad` varchar(255) DEFAULT NULL,
  `RespuestaSeguridad` varchar(255) DEFAULT NULL,
  `FechaRegistro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `IntentosFallidos` int(11) DEFAULT '0',
  PRIMARY KEY (`UsuarioID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'santy','umeres','qwert',1,'santiago@gmail.com','¿Color favorito?','Rojo','2024-06-13 00:55:26',0),(9,'santy112',NULL,'zxcvb',2,'santy@gmail.com','¿animal favorito?','gatos','2024-06-13 04:07:25',0),(10,'santiagor','lopez','123456789',1,'vamp@gmiail.com','¿animal favorito?','perros','2024-06-21 00:45:29',0);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-02  3:07:59
