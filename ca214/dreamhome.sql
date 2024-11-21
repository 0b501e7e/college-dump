-- MySQL dump 10.13  Distrib 8.0.26, for macos11 (x86_64)
--
-- Host: localhost    Database: dreamhome
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `branch`
--

DROP TABLE IF EXISTS `branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `branch` (
  `branchNo` char(5) NOT NULL,
  `street` varchar(35) DEFAULT NULL,
  `city` varchar(10) DEFAULT NULL,
  `postcode` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`branchNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branch`
--

LOCK TABLES `branch` WRITE;
/*!40000 ALTER TABLE `branch` DISABLE KEYS */;
INSERT INTO `branch` VALUES ('B002','56 Clover Dr','London','NW10 6EU'),('B003','163 Main St','Glasgow','G11 9QX'),('B004','32 Manse Rd','Bristol','BS99 1NZ'),('B005','22 Deer Rd','London','SW1 4EH'),('B007','16 Argyll St','Aberdeen','AB2 3SU');
/*!40000 ALTER TABLE `branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client` (
  `clientNo` char(5) NOT NULL,
  `fName` varchar(10) DEFAULT NULL,
  `lName` varchar(10) DEFAULT NULL,
  `telNo` char(15) DEFAULT NULL,
  `prefType` varchar(10) DEFAULT NULL,
  `maxRent` int DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`clientNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES ('CR56','Aline','Steward','0141-848-1825','Flat',350,'astewart@hotmail.com'),('CR62','Mary','Tregear','01224-196720','Flat',600,'maryt@hotmail.co.uk'),('CR74','Mike','Ritchie','01475-943-1728','House',750,'mritchie@yahoo.co.uk'),('CR76','John','Kay','0171-774-5632','Flat',425,'john.kay@gmail.com');
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `privateOwner`
--

DROP TABLE IF EXISTS `privateOwner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `privateOwner` (
  `ownerNo` char(5) NOT NULL,
  `fName` varchar(10) DEFAULT NULL,
  `lName` varchar(10) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `telNo` char(15) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`ownerNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `privateOwner`
--

LOCK TABLES `privateOwner` WRITE;
/*!40000 ALTER TABLE `privateOwner` DISABLE KEYS */;
INSERT INTO `privateOwner` VALUES ('CO40','Tina','Murphy','63 Well St. Glasgow G42','0141-943-1728','tinam@hotmail.com',NULL),('CO46','Joe','Keogh','2 Fergus Dr. Aberdeen AB2 ','01224-861212','jkeogh@lhh.com',NULL),('CO87','Carol','Farrel','6 Achray St. Glasgow G32 9DX','0141-357-7419','cfarrel@gmail.com',NULL),('CO93','Tony','Shaw','12 Park Pl. Glasgow G4 0QR','0141-225-7025','tony.shaw@ark.com',NULL);
/*!40000 ALTER TABLE `privateOwner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `propertyForRent`
--

DROP TABLE IF EXISTS `propertyForRent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `propertyForRent` (
  `propertyNo` char(5) NOT NULL,
  `street` varchar(35) DEFAULT NULL,
  `city` varchar(10) DEFAULT NULL,
  `postcode` varchar(10) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  `rooms` smallint DEFAULT NULL,
  `rent` int DEFAULT NULL,
  `ownerNo` char(5) NOT NULL,
  `staffNo` char(5) DEFAULT NULL,
  `branchNo` char(5) DEFAULT NULL,
  PRIMARY KEY (`propertyNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `propertyForRent`
--

LOCK TABLES `propertyForRent` WRITE;
/*!40000 ALTER TABLE `propertyForRent` DISABLE KEYS */;
INSERT INTO `propertyForRent` VALUES ('PA14','16 Holhead','Aberdeen','AB7 5SU','House',6,650,'CO46','SA9','B007'),('PG16','5 Novar Dr','Glasgow','G12 9AX','Flat',4,450,'CO93','SG14','B003'),('PG21','18 Dale Rd','Glasgow','G12','House',5,600,'CO87','SG37','B003'),('PG36','2 Manor Rd','Glasgow','G32 4QX','Flat',3,375,'CO93','SG37','B003'),('PG4','6 Lawrence St','Glasgow','G11 9QX','Flat',3,350,'CO40',NULL,'B003'),('PL94','6 Argyll St','London','NW2','Flat',4,400,'CO87','SL41','B005');
/*!40000 ALTER TABLE `propertyForRent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registration`
--

DROP TABLE IF EXISTS `registration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registration` (
  `clientNo` char(5) NOT NULL,
  `branchNo` char(5) NOT NULL,
  `staffNo` char(5) NOT NULL,
  `dateJoined` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registration`
--

LOCK TABLES `registration` WRITE;
/*!40000 ALTER TABLE `registration` DISABLE KEYS */;
INSERT INTO `registration` VALUES ('CR76','B005','SL41','2015-01-13'),('CR56','B003','SG37','2014-04-13'),('CR74','B003','SG37','2013-11-16'),('CR62','B007','SA9','2014-03-07');
/*!40000 ALTER TABLE `registration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `staffNo` char(5) NOT NULL,
  `fName` varchar(10) DEFAULT NULL,
  `lName` varchar(10) DEFAULT NULL,
  `position` varchar(10) DEFAULT NULL,
  `sex` char(1) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `salary` int DEFAULT NULL,
  `branchNo` char(5) DEFAULT NULL,
  PRIMARY KEY (`staffNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES ('SA9','Mary','Howe','Assistant','F','1990-02-19',9000,'B007'),('SG14','David','Ford','Supervisor','M','1978-03-24',18000,'B003'),('SG37','Ann','Beech','Assistant','F','1980-11-10',12000,'B003'),('SG5','Susan','Brand','Manager','F','1960-06-03',24000,'B003'),('SL21','John','White','Manager','M','1965-10-01',30000,'B005'),('SL41','Julie','Lee','Assistant','F','1985-06-13',9000,'B005');
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `viewing`
--

DROP TABLE IF EXISTS `viewing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `viewing` (
  `clientNo` char(5) NOT NULL,
  `propertyNo` char(5) NOT NULL,
  `viewDate` date DEFAULT NULL,
  `comment` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `viewing`
--

LOCK TABLES `viewing` WRITE;
/*!40000 ALTER TABLE `viewing` DISABLE KEYS */;
INSERT INTO `viewing` VALUES ('CR56','PA14','2015-05-24','too small'),('CR76','PG4','2015-04-20','too remote'),('CR56','PG4','2015-05-26',''),('CR62','PA14','2015-05-14','no dining room'),('CR56','PG36','2015-04-28','');
/*!40000 ALTER TABLE `viewing` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-22  0:12:45
