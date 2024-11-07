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
-- Table structure for table `t_01paciente`
--

DROP TABLE IF EXISTS `t_01paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_01paciente` (
  `Id_paciente` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) CHARACTER SET utf8mb4 DEFAULT NULL,
  `Apellido` varchar(50) CHARACTER SET utf8mb4 DEFAULT NULL,
  `DNI` varchar(20) CHARACTER SET utf8mb4 DEFAULT NULL,
  `Fecha_nacimiento` date DEFAULT NULL,
  `Fecha_registro` date DEFAULT NULL,
  `Observaciones` text CHARACTER SET utf8mb4,
  `Id_padre` int(11) DEFAULT NULL,
  `Id_genero` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id_paciente`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COMMENT='Tabla almacena información básica de los pacientes, incluyendo datos personales, fechas importantes y relaciones con otros registros (padre y género)';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_01paciente`
--

LOCK TABLES `t_01paciente` WRITE;
/*!40000 ALTER TABLE `t_01paciente` DISABLE KEYS */;
INSERT INTO `t_01paciente` VALUES (1,'Ana','García','12345678','2010-05-15','2023-07-01','Sin alergias conocidas',1,2),(2,'Juan','López','23456789','2012-08-20','2023-07-05','Problemas de concentración en clase',2,1),(3,'María','Martínez','34567890','2011-03-10','2023-07-10','Fobia a los espacios cerrados',3,2),(4,'Pedro','Rodríguez','45678901','2013-11-25','2023-07-15','Intereses en música y arte',4,1),(5,'Luisa','Pérez','56789012','2010-07-30','2023-07-20','Dificultades en matemáticas',5,2),(6,'Carlos','Gómez','67890123','2012-01-12','2023-07-25','Historial de déficit de atención',2,1),(7,'Laura','Díaz','78901234','2013-06-05','2023-08-01','Intereses en deportes y actividad física',6,2),(8,'José','Hernández','89012345','2011-09-18','2023-08-05','Experiencias de ansiedad social',7,1),(9,'Sofía','Ramírez','90123456','2010-12-08','2023-08-10','Dificultades en lectura comprensiva',8,2),(10,'Andrés','Torres','01234567','2012-02-28','2023-08-15','Historial de terapia de lenguaje',8,1),(16,'carlos','tevez','142432','2014-07-10','2024-08-08','as',NULL,1),(17,'santiago','umeres','410037566','1998-03-31','2024-08-15','minecraft',NULL,1),(18,'carlos','villan','142432','2010-04-25','2024-10-15','',NULL,1),(19,'carlos','lopez','142432','2010-02-12','2024-06-11','minecraft',NULL,1);
/*!40000 ALTER TABLE `t_01paciente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_02direccionpaciente`
--

DROP TABLE IF EXISTS `t_02direccionpaciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_02direccionpaciente` (
  `id_direccion` int(11) NOT NULL AUTO_INCREMENT,
  `id_paciente` int(11) DEFAULT NULL,
  `direccion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `ciudad` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `estado` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `codigo_postal` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_direccion`),
  KEY `id_paciente` (`id_paciente`),
  CONSTRAINT `t_02direccionpaciente_ibfk_1` FOREIGN KEY (`id_paciente`) REFERENCES `t_01paciente` (`Id_paciente`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COMMENT='Tabla almacena la información de las direcciones de los pacientes, incluyendo la relación con el paciente correspondiente';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_02direccionpaciente`
--

LOCK TABLES `t_02direccionpaciente` WRITE;
/*!40000 ALTER TABLE `t_02direccionpaciente` DISABLE KEYS */;
INSERT INTO `t_02direccionpaciente` VALUES (1,1,'Calle 123, Colonia Primavera','Ciudad de México','CDMX','12345'),(2,1,'Av. Central, Urbanización Los Pinos','Lima','Lima','54321'),(3,3,'Paseo del Sol, Barrio Vista Hermosa','Guadalajara','Jalisco','67890'),(4,4,'Rua das Flores, Bairro Centro','São Paulo','São Paulo','98765'),(5,5,'123 Main Street, Apartment 4B','New York','NY','54321'),(6,6,'Carrera 45, Conjunto Residencial Los Laureles','Bogotá','Bogotá','12345'),(7,7,'Avenida del Deporte, Sector Los Olivos','Santiago','Metropolitana','67890'),(8,8,'Calle 18, Barrio San Juan','San Salvador','San Salvador','98765'),(9,9,'Avenida Principal, Urbanización Los Robles','Caracas','Distrito Capital','54321'),(10,10,'Rua das Pedras, Condomínio Recanto Feliz','Rio de Janeiro','Rio de Janeiro','12345'),(11,10,'Avenida Central, Conjunto Residencial Los Pájaros','Quito','Pichincha','67890'),(12,18,'barrio margarita','esquina','corrientes','3459'),(13,2,'barrio margarita','goya','corrientes','3459'),(14,16,'barrio belgrano','goya','corrientes','3459');
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
  `Nombre` varchar(50) CHARACTER SET utf8mb4 DEFAULT NULL,
  PRIMARY KEY (`Id_genero`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabla se relaciona con la tabla "t_01paciente" a través de la columna "Id_genero", lo que permite asignar un género a cada paciente.';
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
-- Table structure for table `t_03padres_madres`
--

DROP TABLE IF EXISTS `t_03padres_madres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_03padres_madres` (
  `id_padre` int(11) NOT NULL AUTO_INCREMENT,
  `nombres` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `apellido` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `telefono` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ocupacion` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id_nivel_educacion` int(11) DEFAULT NULL,
  `Fecha_nacimiento` date DEFAULT NULL,
  `tipo_relacion` varchar(200) CHARACTER SET utf8mb4 DEFAULT NULL,
  PRIMARY KEY (`id_padre`),
  KEY `id_nivel_educacion` (`id_nivel_educacion`),
  CONSTRAINT `t_03padres_madres_ibfk_1` FOREIGN KEY (`id_nivel_educacion`) REFERENCES `t_05niveleseducacion` (`id_nivel`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8 COMMENT='Tabla almacena información detallada sobre los padres y madres de los pacientes, incluyendo datos personales, ocupación, nivel de educación y tipo de relación con el paciente.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_03padres_madres`
--

LOCK TABLES `t_03padres_madres` WRITE;
/*!40000 ALTER TABLE `t_03padres_madres` DISABLE KEYS */;
INSERT INTO `t_03padres_madres` VALUES (2,'María','López','987-654-3210','Profesora',4,'1985-06-25',NULL),(4,'Laura','Rodríguez','777-888-9999','Ama de casa y maestra',NULL,'1992-09-02',NULL),(41,'Maria','Lopez','3777675402','Maestra',NULL,'1995-10-09',NULL),(42,'Lourdes','Quiroz','246598','Abogada',3,'1989-09-09',NULL),(43,'Valeria','Fernandez','3777986545','Comerciante',3,'1998-12-07',NULL),(44,'Alma','chaz','1255123','Vendedora',3,'2000-08-08',NULL),(45,'Maria','villan','12541351','Maestra',3,'1998-07-09',NULL),(46,'lucas','afas','12412','panadero',3,'1998-03-09',NULL),(47,'sdfsd','afas','3777896572','Maestra',3,'1990-05-12',NULL),(48,'Maria','afas','12412','Maestra',3,'1998-10-09',NULL),(49,'sad','asd','123','wqewq',3,'1998-02-12',NULL),(50,'Tiara','Aguirres','124124','insipida',NULL,'2000-04-24',NULL),(51,'pepo','ponpin','3777896572','panadero',2,'2000-04-12',NULL),(52,'furra','tiara','12412','manca',4,'2000-04-25',NULL);
/*!40000 ALTER TABLE `t_03padres_madres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_04direccionpadre`
--

DROP TABLE IF EXISTS `t_04direccionpadre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_04direccionpadre` (
  `id_direccion` int(11) NOT NULL AUTO_INCREMENT,
  `id_padre` int(11) DEFAULT NULL,
  `direccion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `ciudad` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id_estado_vivienda` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_direccion`),
  KEY `id_padre` (`id_padre`),
  KEY `id_estado_vivienda` (`id_estado_vivienda`),
  CONSTRAINT `t_04direccionpadre_ibfk_2` FOREIGN KEY (`id_estado_vivienda`) REFERENCES `t_12estadovivienda` (`id_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COMMENT='Tabla almacena la información de las direcciones de los padres y madres, incluyendo la relación con el padre o madre correspondiente. Es similar a la tabla "t_02direccionpaciente", pero para los padres y madres en lugar de los pacientes.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_04direccionpadre`
--

LOCK TABLES `t_04direccionpadre` WRITE;
/*!40000 ALTER TABLE `t_04direccionpadre` DISABLE KEYS */;
INSERT INTO `t_04direccionpadre` VALUES (3,2,'RQWRQ','RQWRQ',1),(5,4,'ASDAS','DASDA',2),(10,9,'Rua das Pedras, Condomínio Recanto Feliz','Rio de Janeiro',2),(11,9,'Rua das Flores, Apartamento 2C','Rio de Janeiro',2),(12,10,'Avenida Central, Edificio Azul','Lima',1),(13,10,'Calle 15, Urbanización Bella Vista','Lima',1),(14,1,'Calle 1, No. 123','Ciudad 1',1),(15,1,'Calle 2, No. 456','Ciudad 2',2),(16,2,NULL,NULL,NULL),(17,3,'Calle 4, No. 1011','Ciudad 4',2);
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
  `nivel` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id_nivel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabla almacena la información de los diferentes niveles de educación que pueden tener los padres o madres de los pacientes. ';
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabla almacena la información relacionada con el embarazo de las madres, incluyendo la fecha de inicio y fin del embarazo, el tipo de parto, la semana de gestación y el peso del bebé al nacer. Como mencionas, esta tabla solo sería relevante para las madres.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_06datosembarazo`
--

LOCK TABLES `t_06datosembarazo` WRITE;
/*!40000 ALTER TABLE `t_06datosembarazo` DISABLE KEYS */;
INSERT INTO `t_06datosembarazo` VALUES (1,1,1,'2020-01-01','2020-08-01',30,3.50),(2,2,2,'2020-02-01','2020-09-01',32,3.80),(3,3,1,'2020-03-01','2020-10-01',35,4.00),(4,4,2,'2020-04-01','2020-11-01',30,3.20),(5,5,1,'2020-05-01','2020-12-01',33,3.60),(6,6,2,'2020-06-01','2021-01-01',31,3.40),(7,7,1,'2020-07-01','2021-02-01',34,3.90),(8,8,2,'2020-08-01','2021-03-01',29,3.10),(9,9,1,'2020-09-01','2021-04-01',36,4.20),(10,10,2,'2020-10-01','2021-05-01',30,3.50),(11,1,1,'2022-01-01','2022-10-01',40,3.50);
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
  `tipo` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_tipo_parto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabla almacena la información de los diferentes tipos de parto que pueden ocurrir.';
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
  `id_embarazo` int(11) DEFAULT NULL,
  `enfermedad` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `id_embarazo` (`id_embarazo`),
  CONSTRAINT `t_09enfermedadesembarazo_ibfk_1` FOREIGN KEY (`id_embarazo`) REFERENCES `t_06datosembarazo` (`id_embarazo`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COMMENT='Tabla almacena la información de las enfermedades que ocurrieron durante el embarazo de cada madre. La relación con la tabla "t_06datosembarazo" permite vincular cada enfermedad con el embarazo correspondiente.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_09enfermedadesembarazo`
--

LOCK TABLES `t_09enfermedadesembarazo` WRITE;
/*!40000 ALTER TABLE `t_09enfermedadesembarazo` DISABLE KEYS */;
INSERT INTO `t_09enfermedadesembarazo` VALUES (1,'Hipertensión',1),(2,'Gestación diabetes',2),(3,'Anemia',3),(4,'Infección urinaria',4),(5,'Hipertensión',5),(6,'Preeclampsia',6),(7,'Gestación diabetes',7),(8,'Anemia',8),(9,'Infección respiratoria',9),(10,'Hipertensión',10),(1,'Enfermedad X',11);
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
  `adaptacion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `relacion_docentes` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `relacion_compañeros` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `repitencia_escolar` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `cambios_escuelas` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `cambios_maestros` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id_historial`),
  KEY `id_paciente` (`id_paciente`),
  KEY `id_institucion` (`id_institucion`),
  CONSTRAINT `t_10historialeducativo_ibfk_1` FOREIGN KEY (`id_paciente`) REFERENCES `t_01paciente` (`Id_paciente`),
  CONSTRAINT `t_10historialeducativo_ibfk_2` FOREIGN KEY (`id_institucion`) REFERENCES `t_11caracteristicainstitu` (`id_institucion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabla almacena la información detallada sobre el historial educativo de cada paciente, incluyendo su adaptación, relaciones con docentes y compañeros, repitencia escolar, y cambios en escuelas y maestros.';
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
  `institucion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id_institucion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabla "t_11caracteristicainstitu" podría ser utilizada para almacenar información sobre el tipo de institución educativa, como si es pública o privada.';
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
  `estado_vivienda` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabla almacena la información sobre el estado de la vivienda de los pacientes, lo que puede ser útil para evaluar su situación habitacional y cómo puede afectar su salud o bienestar.';
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
  `ambiente_familiar` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `union_estable` enum('Sí','No') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tiempo_convivencia` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `ingresos_padre` decimal(10,2) DEFAULT NULL,
  `ingresos_madre` decimal(10,2) DEFAULT NULL,
  `expectativas_padres` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `dia_comun_menor` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `id_estado_vivienda` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_informacion_familiar`),
  KEY `id_paciente` (`id_paciente`),
  KEY `id_estado_vivienda` (`id_estado_vivienda`),
  CONSTRAINT `t_12infofamiliar_ibfk_1` FOREIGN KEY (`id_paciente`) REFERENCES `t_01paciente` (`Id_paciente`),
  CONSTRAINT `t_12infofamiliar_ibfk_2` FOREIGN KEY (`id_estado_vivienda`) REFERENCES `t_12estadovivienda` (`id_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabla almacena información detallada sobre la situación familiar de cada paciente, incluyendo el ambiente familiar, la unión estable, el tiempo de convivencia, los ingresos de los padres, las expectativas de los padres, y el estado de la vivienda familiar. ';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_12infofamiliar`
--

LOCK TABLES `t_12infofamiliar` WRITE;
/*!40000 ALTER TABLE `t_12infofamiliar` DISABLE KEYS */;
INSERT INTO `t_12infofamiliar` VALUES (1,1,'Ambiente familiar cálido y acogedor.','Sí','4 años',1500.00,1200.00,'Esperan que el menor destaque en sus estudios.','Día común incluye actividades escolares y juegos.',1),(2,2,'Hogar con armonía y respeto.','Sí','8 años',1800.00,900.00,'Desean que el menor sea autodisciplinado.','Día común implica actividades escolares y lectura.',2),(3,3,'Ambiente familiar lleno de amor y apoyo.','Sí','6 años',2000.00,1600.00,'Esperan que el menor desarrolle habilidades sociales.','Día común involucra juegos, tareas escolares y salidas.',2),(4,4,'Hogar con respeto a la individualidad.','No','10 años',2200.00,2000.00,'Desean que el menor tenga éxito académico.','Día común abarca estudio, deportes y tiempo en familia.',2),(5,5,'Ambiente familiar con comunicación abierta.','Sí','5 años',1800.00,1100.00,'Esperan que el menor sea creativo.','Día común incluye estudio, juegos y actividades al aire libre.',1),(6,6,'Ambiente tranquilo y afectuoso en casa','Sí','10 años',1500.00,1200.00,'Esperamos que termine su educación secundaria','Jugar en el parque',1),(7,7,'Hogar con gran participación en actividades culturales','No','7 años',2000.00,1800.00,'Queremos que aprenda un idioma extranjero','Ver películas en familia',2),(8,8,'Familia unida y comprometida con actividades deportivas','Sí','12 años',1800.00,1600.00,'Esperamos que destaque en el ámbito escolar','Visitar a los abuelos los fines de semana',3),(9,9,'Ambiente tenso debido a diferencias entre los padres','No','5 años',1400.00,1300.00,'Queremos que mejore su rendimiento académico','Jugar videojuegos',1),(20,10,'Casa con muchas actividades al aire libre','Sí','8 años',1700.00,1500.00,'Esperamos que sea un líder en su grupo escolar','Salir en bicicleta los domingos',2);
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
  `observacion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id_sesiones`),
  KEY `id_paciente` (`id_paciente`),
  KEY `id_tipo_sesion` (`id_tipo_sesion`),
  KEY `id_desarrollo_psicomotor` (`id_desarrollo_psicomotor`),
  KEY `id_desarrollo_lenguaje` (`id_desarrollo_lenguaje`),
  CONSTRAINT `t_13datosesion_ibfk_1` FOREIGN KEY (`id_paciente`) REFERENCES `t_01paciente` (`Id_paciente`),
  CONSTRAINT `t_13datosesion_ibfk_2` FOREIGN KEY (`id_tipo_sesion`) REFERENCES `t_14tipossesion` (`id_tipo_sesion`),
  CONSTRAINT `t_13datosesion_ibfk_3` FOREIGN KEY (`id_desarrollo_psicomotor`) REFERENCES `t_16desarrollopsicomotor` (`id_desarrollo_psicomotor`),
  CONSTRAINT `t_13datosesion_ibfk_4` FOREIGN KEY (`id_desarrollo_lenguaje`) REFERENCES `t_15desarrollolenguaje` (`id_desarrollo_lenguaje`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabla almacena información detallada sobre cada sesión de terapia o evaluación del paciente, incluyendo la fecha, hora, duración, tipo de sesión, desarrollo psicomotor y del lenguaje, y observaciones adicionales. ';
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
  `nombre_tipo` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_tipo_sesion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabla almacena la información de los diferentes tipos de sesiones que se pueden realizar con los pacientes.';
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
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id_desarrollo_lenguaje`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabla almacena la información de los diferentes niveles de desarrollo del lenguaje que pueden presentar los pacientes';
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
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id_desarrollo_psicomotor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabla almacena la información de los diferentes niveles de desarrollo psicomotor que pueden presentar los pacientes.';
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
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuario` (
  `UsuarioID` int(11) NOT NULL AUTO_INCREMENT,
  `NombreUsuario` varchar(50) CHARACTER SET latin1 NOT NULL,
  `Apellido` varchar(25) CHARACTER SET latin1 DEFAULT NULL,
  `Contraseña` varchar(20) CHARACTER SET latin1 NOT NULL,
  `Email` varchar(35) CHARACTER SET latin1 NOT NULL,
  `PreguntaSeguridad` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `RespuestaSeguridad` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `FechaRegistro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `UltimoIntentoFallido` int(11) DEFAULT '0',
  PRIMARY KEY (`UsuarioID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COMMENT='Tabla "usuario" es fundamental para el proceso de inicio de sesión y la seguridad del sistema.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'santi','umeres','qwert','santiago@gmail.com','¿Color favorito?','Rojo','2024-06-13 00:55:26',0),(9,'santy112',NULL,'123456','santy@gmail.com','¿animal favorito?','gatos','2024-06-13 04:07:25',0),(12,'santiago','umeres','P@ssw0rd!2023','tonta@gmail.com','¿En qué ciudad naciste?','goya','2024-07-05 04:45:25',0);
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

-- Dump completed on 2024-11-07  0:14:23
