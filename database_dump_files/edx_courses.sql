-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: edx
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses` (
  `course_id` int NOT NULL AUTO_INCREMENT,
  `cat_id` int DEFAULT NULL,
  `course_name` varchar(45) DEFAULT NULL,
  `fee` int DEFAULT NULL,
  PRIMARY KEY (`course_id`),
  UNIQUE KEY `p_id_UNIQUE` (`course_id`),
  KEY `cat_id_idx` (`cat_id`),
  CONSTRAINT `cat_id` FOREIGN KEY (`cat_id`) REFERENCES `catagories` (`cat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1035 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES (1001,1111,'C programming',500),(1002,1111,'Python3',600),(1005,1111,'RISC V',400),(1006,1111,'Verilogs',500),(1007,1111,'TL Verilogs',700),(1008,1112,'Classical',3000),(1009,1112,'Pop',2500),(1010,1112,'Acoustic',2000),(1011,1112,'Guitar',3500),(1012,1112,'Piano',3000),(1013,1113,'AutoCAD',1500),(1014,1113,'Photoshop',1500),(1015,1113,'Blender',2000),(1016,1113,'Illustrator',1600),(1017,1113,'After Effects',2000),(1018,1114,'System Design',750),(1019,1114,'High speed computation',850),(1020,1114,'Micro Architecture',950),(1021,1115,'Sublime Pixel',450),(1022,1115,'Master Photography',750),(1023,1115,'ShotOn',1000),(1024,1116,'Mechanics & Design',1500),(1025,1116,'Hardware & Design',1200),(1026,1117,'Xamrin',1500),(1027,1117,'Android SDK',2500),(1028,1117,'Visual Studio',1500),(1029,1117,'Game Devolopment',1400),(1030,1118,'React JS',1500),(1031,1118,'Node JS',1500),(1032,1118,'Angular JS',2000),(1033,1118,'HTML CSS JS',1000),(1034,1118,'Python Flask',1200);
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-03 18:48:56
