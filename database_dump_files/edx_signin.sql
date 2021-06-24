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
-- Table structure for table `signin`
--

DROP TABLE IF EXISTS `signin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `signin` (
  `signin_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`signin_id`),
  UNIQUE KEY `signin_id_UNIQUE` (`signin_id`),
  KEY `user_id_idx` (`user_id`),
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `signin`
--

LOCK TABLES `signin` WRITE;
/*!40000 ALTER TABLE `signin` DISABLE KEYS */;
INSERT INTO `signin` VALUES (1,101,'temp@gmail.com','2021-02-28 19:40:00'),(2,102,'venkatkum@gmail.com','2021-02-28 19:45:38'),(3,103,'venkatkumar102000@gmail.com','2021-02-28 19:49:32'),(4,104,'ajay@gmail.com','2021-03-03 11:00:21'),(25,105,'sreeram@gmail.com','2021-03-04 18:50:24'),(26,105,'sreeram@gmail.com','2021-03-04 18:50:50'),(27,106,'ishitha@gmail.com','2021-03-04 18:56:49'),(28,106,'venkatkumar102000@gmail.com','2021-03-04 18:57:30'),(29,107,'hey123@gmail.com','2021-03-06 12:01:44'),(30,108,'dinesh@gmail.com','2021-03-06 18:05:11'),(31,108,'ajay@gmail.com','2021-03-07 11:40:35'),(32,108,'ishitha@gmail.com','2021-03-07 11:44:58'),(33,108,'ishitha@gmail.com','2021-03-07 22:05:38'),(34,108,'ajay@gmail.com','2021-03-08 20:00:45'),(35,108,'ajay@gmail.com','2021-03-08 20:18:37'),(44,103,'venkatkumar102000@gmail.com','2021-03-24 14:23:58'),(45,104,'ajay@gmail.com','2021-03-24 14:28:27'),(46,103,'venkatkumar102000@gmail.com','2021-03-24 15:18:03'),(47,106,'ishitha@gmail.com','2021-03-26 11:35:59'),(48,109,'masthan@gmail.com','2021-03-26 11:36:33'),(49,103,'venkatkumar102000@gmail.com','2021-03-26 11:38:31'),(50,104,'ajay@gmail.com','2021-03-29 08:56:18'),(51,103,'venkatkumar102000@gmail.com','2021-03-29 08:56:38'),(52,106,'ishitha@gmail.com','2021-03-31 15:09:09'),(53,110,'abc@gmail.com','2021-03-31 16:04:03'),(54,103,'venkatkumar102000@gmail.com','2021-03-31 16:06:43'),(55,104,'ajay@gmail.com','2021-05-01 12:36:01'),(56,104,'ajay@gmail.com','2021-05-01 18:42:52'),(57,104,'ajay@gmail.com','2021-05-01 18:45:23'),(58,104,'ajay@gmail.com','2021-05-01 18:47:45'),(59,104,'ajay@gmail.com','2021-05-01 18:56:34'),(60,103,'venkatkumar102000@gmail.com','2021-05-01 19:02:44'),(61,104,'ajay@gmail.com','2021-05-01 19:05:22'),(62,103,'venkatkumar102000@gmail.com','2021-05-02 18:50:45'),(64,112,'sreevani@gmail.com','2021-05-03 10:44:28'),(65,109,'masthan@gmail.com','2021-05-03 17:25:43'),(66,108,'dinesh@gmail.com','2021-05-03 17:26:03');
/*!40000 ALTER TABLE `signin` ENABLE KEYS */;
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
