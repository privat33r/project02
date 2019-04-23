-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: csmidn    Database: m207026
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

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
-- Table structure for table `MESSAGES`
--

DROP TABLE IF EXISTS `MESSAGES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MESSAGES` (
  `MessageID` int(11) NOT NULL AUTO_INCREMENT,
  `UserID` int(11) NOT NULL,
  `Message` varchar(140) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Timestamp` datetime NOT NULL,
  PRIMARY KEY (`MessageID`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MESSAGES`
--

LOCK TABLES `MESSAGES` WRITE;
/*!40000 ALTER TABLE `MESSAGES` DISABLE KEYS */;
INSERT INTO `MESSAGES` VALUES (27,20,'test','2019-04-13 21:27:49'),(28,1,'this is root','2019-04-13 21:30:43'),(29,1,'&lt;more examples&gt;','2019-04-13 21:32:11'),(30,1,'now now','2019-04-13 21:32:17'),(31,20,'testing','2019-04-13 21:32:29'),(32,20,'testing','2019-04-13 21:32:54'),(33,20,'testing','2019-04-13 21:33:50'),(34,20,'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhoverflowssssssssssssssssssss','2019-04-13 21:34:56'),(35,20,'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhoverflowssssssssssssssssssss','2019-04-13 21:36:07'),(36,20,'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhoverflowssssssssssssssssssss','2019-04-13 21:36:12'),(37,20,'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhoverflowssssssssssssssssssss','2019-04-13 21:37:58'),(38,1,'new message!','2019-04-13 21:44:36'),(39,3,'I am Ben','2019-04-13 23:43:52'),(40,28,'I am new user','2019-04-13 23:45:58'),(41,1,'&lt;empty message&gt;','2019-04-13 23:53:37');
/*!40000 ALTER TABLE `MESSAGES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Midshipmen`
--

DROP TABLE IF EXISTS `Midshipmen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Midshipmen` (
  `alpha` int(10) unsigned NOT NULL,
  `FirstName` char(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `LastName` char(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Company` tinyint(3) unsigned DEFAULT NULL,
  `Room` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Phone` char(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Email` char(40) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Major` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `SupList` enum('Y','N') COLLATE utf8mb4_unicode_ci DEFAULT 'N',
  PRIMARY KEY (`alpha`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Midshipmen`
--

LOCK TABLES `Midshipmen` WRITE;
/*!40000 ALTER TABLE `Midshipmen` DISABLE KEYS */;
INSERT INTO `Midshipmen` VALUES (200122,'John P.','Jones',13,'77552','410-293-0301','m200122@usna.edu','CyberSci','N'),(200190,'John','Smith',5,'54321','410-293-0001','m200190@usna.edu','CompSci','N'),(200312,'John','Doe',9,'98765','410-293-0003','m200312@usna.edu','ElecEng','N'),(200673,'Jane','Doe',7,'76543','410-293-0002','m200673@usna.edu','InfoTech','Y'),(200892,'Jason','Jones',19,'19333','410-293-0019','m200892@usna.edu','CompSci','N'),(201233,'Eugene','Fluckey',8,'22554','410-293-0219','m201233@usna.edu','CompSci','N'),(205269,'Chesty','Puller',28,'33485','410-293-5402','m205269@usna.edu','InfoTech','Y'),(208416,'Francis','Key',2,'84223','410-293-4403','m208416@usna.edu','MechEng','N'),(338416,'David','McCampbell',2,'84223','410-293-4403',NULL,'MarineEng','N');
/*!40000 ALTER TABLE `Midshipmen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PRODUCT`
--

DROP TABLE IF EXISTS `PRODUCT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PRODUCT` (
  `ProductID` int(11) NOT NULL,
  `PName` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `PDescription` varchar(256) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Price` int(11) NOT NULL,
  PRIMARY KEY (`ProductID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PRODUCT`
--

LOCK TABLES `PRODUCT` WRITE;
/*!40000 ALTER TABLE `PRODUCT` DISABLE KEYS */;
INSERT INTO `PRODUCT` VALUES (1,'T-Shirt','Spread the awareness by sporting the Alliance Shirt!',10),(2,'Cap','It\'s time the fat cats get a heart a attack.',15),(3,'Flat-Earth Model','This map have been used by Ancient Egyptians for star maps in some holy book.',35),(4,'Parallel Rule','To help navigate a flat earth.',18),(5,'Book','A best-seller!',20);
/*!40000 ALTER TABLE `PRODUCT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SALE`
--

DROP TABLE IF EXISTS `SALE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SALE` (
  `SaleID` int(11) NOT NULL AUTO_INCREMENT,
  `DeliveryAddress` varchar(256) COLLATE utf8mb4_unicode_ci NOT NULL,
  `CreditCard` char(16) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`SaleID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SALE`
--

LOCK TABLES `SALE` WRITE;
/*!40000 ALTER TABLE `SALE` DISABLE KEYS */;
/*!40000 ALTER TABLE `SALE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SALEITEM`
--

DROP TABLE IF EXISTS `SALEITEM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SALEITEM` (
  `SaleID` int(11) NOT NULL,
  `ProductID` int(11) NOT NULL,
  `Quantity` int(11) NOT NULL,
  PRIMARY KEY (`SaleID`,`ProductID`),
  KEY `FK_SI_P` (`ProductID`),
  CONSTRAINT `FK_SI_P` FOREIGN KEY (`ProductID`) REFERENCES `PRODUCT` (`ProductID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_SI_S` FOREIGN KEY (`SaleID`) REFERENCES `SALE` (`SaleID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SALEITEM`
--

LOCK TABLES `SALEITEM` WRITE;
/*!40000 ALTER TABLE `SALEITEM` DISABLE KEYS */;
/*!40000 ALTER TABLE `SALEITEM` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USERS`
--

DROP TABLE IF EXISTS `USERS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `USERS` (
  `UserID` int(11) NOT NULL AUTO_INCREMENT,
  `Username` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Password` varchar(256) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Admin` int(11) NOT NULL,
  PRIMARY KEY (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `USERS`
--

LOCK TABLES `USERS` WRITE;
/*!40000 ALTER TABLE `USERS` DISABLE KEYS */;
INSERT INTO `USERS` VALUES (1,'root','9c03c5265606e5da39ca2dcc5982d1be88ec2749904860cf37948bb6ee3fe501',1),(3,'Ben','e82717f400f3d5a886607e42cdd222d4474269fe0168757c5aa011a3253279c6',0),(18,'Test','4912b67eb5149534ffcccfa0337e3eb0cb3b544c0725c02b36f583130edc451d',0),(20,'Juan','2d9e6a03aa925bba6aa15ac85b6a730cb1d3fb4826122845ab4b7c25bd430b87',0),(21,'test1','c41f677df54114d19d9240b003cc062eec3692e18708da3ce59d1e1e3e12d9b7',0),(23,'Brandon','11699a110249549ccd175f44f61a00113a45642aa14ee3a6ce78712391968360',0),(27,'testacc','3c481c621f5beb0f8541220ce367fb40b03b1a26b2ea16fe9c2985872dd00e27',0),(28,'newuser','b5f40f203040f58897bc696f010d73cae885a9c61f519101b65e7deee6f65e58',0),(29,'testuser','52aff263939909080fd5483e2e84b921abcd46cfcc1af5eec42737eebb61338b',0),(30,'juan','3944fa675bb70e3b6792ac6a356cd945fc56be40b326abde3d98ecf5dadfc291',0);
/*!40000 ALTER TABLE `USERS` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-19  8:22:53
