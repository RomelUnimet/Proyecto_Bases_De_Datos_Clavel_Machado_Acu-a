-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: elbo_degon3
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `api_bill`
--

DROP TABLE IF EXISTS `api_bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_bill` (
  `id` int NOT NULL AUTO_INCREMENT,
  `is_delivery` tinyint(1) NOT NULL,
  `date_time` datetime(6) NOT NULL,
  `subtotal` double NOT NULL,
  `availible` tinyint(1) NOT NULL,
  `client_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_bill_client_id_6fa63cfa_fk_api_client_id` (`client_id`),
  CONSTRAINT `api_bill_client_id_6fa63cfa_fk_api_client_id` FOREIGN KEY (`client_id`) REFERENCES `api_client` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `api_billproduct`
--

DROP TABLE IF EXISTS `api_billproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_billproduct` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `discount` double NOT NULL,
  `availible` tinyint(1) NOT NULL,
  `batch_id` int NOT NULL,
  `bill_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_billproduct_batch_id_28c4ab1d_fk_api_productbatch_id` (`batch_id`),
  KEY `api_billproduct_bill_id_id_d77bda7b_fk_api_bill_id` (`bill_id_id`),
  CONSTRAINT `api_billproduct_batch_id_28c4ab1d_fk_api_productbatch_id` FOREIGN KEY (`batch_id`) REFERENCES `api_productbatch` (`id`),
  CONSTRAINT `api_billproduct_bill_id_id_d77bda7b_fk_api_bill_id` FOREIGN KEY (`bill_id_id`) REFERENCES `api_bill` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `api_category`
--

DROP TABLE IF EXISTS `api_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `availible` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `api_client`
--

DROP TABLE IF EXISTS `api_client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_client` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ci` varchar(60) NOT NULL,
  `name` varchar(60) NOT NULL,
  `last_name` varchar(60) NOT NULL,
  `is_meber` tinyint(1) NOT NULL,
  `availible` tinyint(1) NOT NULL,
  `zone_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_client_zone_id_9f0fc443_fk_api_zone_id` (`zone_id`),
  CONSTRAINT `api_client_zone_id_9f0fc443_fk_api_zone_id` FOREIGN KEY (`zone_id`) REFERENCES `api_zone` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `api_currencyexchange`
--

DROP TABLE IF EXISTS `api_currencyexchange`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_currencyexchange` (
  `id` int NOT NULL AUTO_INCREMENT,
  `bs_exchange` double NOT NULL,
  `euro_exchange` double NOT NULL,
  `availible` tinyint(1) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `api_delivery`
--

DROP TABLE IF EXISTS `api_delivery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_delivery` (
  `id` int NOT NULL AUTO_INCREMENT,
  `address` varchar(200) NOT NULL,
  `min_time` time(6) NOT NULL,
  `delivered` tinyint(1) NOT NULL,
  `availible` tinyint(1) NOT NULL,
  `bill_id_id` int NOT NULL,
  `delivery_boy_id` int NOT NULL,
  `zone_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_delivery_bill_id_id_93394aed_fk_api_bill_id` (`bill_id_id`),
  KEY `api_delivery_zone_id_1cc0e9c0_fk_api_zone_id` (`zone_id`),
  KEY `api_delivery_delivery_boy_id_9ed9c759_fk_api_employee_id` (`delivery_boy_id`),
  CONSTRAINT `api_delivery_bill_id_id_93394aed_fk_api_bill_id` FOREIGN KEY (`bill_id_id`) REFERENCES `api_bill` (`id`),
  CONSTRAINT `api_delivery_delivery_boy_id_9ed9c759_fk_api_employee_id` FOREIGN KEY (`delivery_boy_id`) REFERENCES `api_employee` (`id`),
  CONSTRAINT `api_delivery_zone_id_1cc0e9c0_fk_api_zone_id` FOREIGN KEY (`zone_id`) REFERENCES `api_zone` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `api_employee`
--

DROP TABLE IF EXISTS `api_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_employee` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ci` varchar(60) NOT NULL,
  `name` varchar(60) NOT NULL,
  `last_name` varchar(60) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `points` int NOT NULL,
  `adress` varchar(200) NOT NULL,
  `gender` varchar(60) NOT NULL,
  `birth_date` date NOT NULL,
  `job_id` varchar(60) NOT NULL,
  `email` varchar(254) NOT NULL,
  `date_hired` date NOT NULL,
  `availible` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `api_local`
--

DROP TABLE IF EXISTS `api_local`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_local` (
  `id` int NOT NULL AUTO_INCREMENT,
  `address` varchar(200) NOT NULL,
  `opening_time` time(6) NOT NULL,
  `closing_time` time(6) NOT NULL,
  `availible` tinyint(1) NOT NULL,
  `manager_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_local_manager_id_2e127c29_fk_api_employee_id` (`manager_id`),
  CONSTRAINT `api_local_manager_id_2e127c29_fk_api_employee_id` FOREIGN KEY (`manager_id`) REFERENCES `api_employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `api_membership`
--

DROP TABLE IF EXISTS `api_membership`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_membership` (
  `id` int NOT NULL AUTO_INCREMENT,
  `points` int NOT NULL,
  `phone` bigint NOT NULL,
  `gender` varchar(60) NOT NULL,
  `address` varchar(200) NOT NULL,
  `birth_date` date NOT NULL,
  `email` varchar(254) NOT NULL,
  `date_registered` date NOT NULL,
  `availible` tinyint(1) NOT NULL,
  `client_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_membership_client_id_e8fb21fc_fk_api_client_id` (`client_id`),
  CONSTRAINT `api_membership_client_id_e8fb21fc_fk_api_client_id` FOREIGN KEY (`client_id`) REFERENCES `api_client` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `api_monthemployee`
--

DROP TABLE IF EXISTS `api_monthemployee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_monthemployee` (
  `id` int NOT NULL AUTO_INCREMENT,
  `month` varchar(20) NOT NULL,
  `year` int NOT NULL,
  `availible` tinyint(1) NOT NULL,
  `employee_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_monthemployee_employee_id_ffc5bb57_fk_api_employee_id` (`employee_id`),
  CONSTRAINT `api_monthemployee_employee_id_ffc5bb57_fk_api_employee_id` FOREIGN KEY (`employee_id`) REFERENCES `api_employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `api_payment`
--

DROP TABLE IF EXISTS `api_payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_payment` (
  `id` int NOT NULL AUTO_INCREMENT,
  `payment_method` varchar(60) NOT NULL,
  `currency` varchar(60) NOT NULL,
  `total` double NOT NULL,
  `account_n` bigint NOT NULL,
  `availible` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `api_payment_bill`
--

DROP TABLE IF EXISTS `api_payment_bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_payment_bill` (
  `id` int NOT NULL AUTO_INCREMENT,
  `availible` tinyint(1) NOT NULL,
  `bill_id` int NOT NULL,
  `payment_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_payment_bill_bill_id_b2d2ad2b_fk_api_bill_id` (`bill_id`),
  KEY `api_payment_bill_payment_id_9a87adf6_fk_api_payment_id` (`payment_id`),
  CONSTRAINT `api_payment_bill_bill_id_b2d2ad2b_fk_api_bill_id` FOREIGN KEY (`bill_id`) REFERENCES `api_bill` (`id`),
  CONSTRAINT `api_payment_bill_payment_id_9a87adf6_fk_api_payment_id` FOREIGN KEY (`payment_id`) REFERENCES `api_payment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `api_pickup`
--

DROP TABLE IF EXISTS `api_pickup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_pickup` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pick_up_time` time(6) NOT NULL,
  `delivered` tinyint(1) NOT NULL,
  `bill_id_id` int NOT NULL,
  `local_id` int NOT NULL,
  `availible` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_pickup_bill_id_id_a0acce50_fk_api_bill_id` (`bill_id_id`),
  KEY `api_pickup_local_id_0d2cd9ba_fk_api_local_id` (`local_id`),
  CONSTRAINT `api_pickup_bill_id_id_a0acce50_fk_api_bill_id` FOREIGN KEY (`bill_id_id`) REFERENCES `api_bill` (`id`),
  CONSTRAINT `api_pickup_local_id_0d2cd9ba_fk_api_local_id` FOREIGN KEY (`local_id`) REFERENCES `api_local` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `api_product`
--

DROP TABLE IF EXISTS `api_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(60) NOT NULL,
  `hall` int NOT NULL,
  `availible` tinyint(1) NOT NULL,
  `category_id` int NOT NULL,
  `provider_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_product_provider_id_5f170ca1_fk_api_provider_id` (`provider_id`),
  KEY `api_product_category_id_a2b9d1e7_fk_api_category_id` (`category_id`),
  CONSTRAINT `api_product_category_id_a2b9d1e7_fk_api_category_id` FOREIGN KEY (`category_id`) REFERENCES `api_category` (`id`),
  CONSTRAINT `api_product_provider_id_5f170ca1_fk_api_provider_id` FOREIGN KEY (`provider_id`) REFERENCES `api_provider` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `api_productbatch`
--

DROP TABLE IF EXISTS `api_productbatch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_productbatch` (
  `id` int NOT NULL AUTO_INCREMENT,
  `expiration_date` date NOT NULL,
  `actual_quantity` bigint NOT NULL,
  `cost` double NOT NULL,
  `discount` int NOT NULL,
  `price` double NOT NULL,
  `point_cost` int NOT NULL,
  `availible` tinyint(1) NOT NULL,
  `product_id` int NOT NULL,
  `elaboration_date` date NOT NULL,
  `local_id` int NOT NULL,
  `quantity_sold` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_productbatch_product_id_033086d4_fk_api_product_id` (`product_id`),
  KEY `api_productbatch_local_id_797c859c_fk_api_local_id` (`local_id`),
  CONSTRAINT `api_productbatch_local_id_797c859c_fk_api_local_id` FOREIGN KEY (`local_id`) REFERENCES `api_local` (`id`),
  CONSTRAINT `api_productbatch_product_id_033086d4_fk_api_product_id` FOREIGN KEY (`product_id`) REFERENCES `api_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `api_provider`
--

DROP TABLE IF EXISTS `api_provider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_provider` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `main_phone` bigint NOT NULL,
  `phone` bigint NOT NULL,
  `address` varchar(200) NOT NULL,
  `email` varchar(254) NOT NULL,
  `availible` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `api_zone`
--

DROP TABLE IF EXISTS `api_zone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_zone` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `cost` double NOT NULL,
  `availible` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-23 13:47:28
