-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.11.2-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.4.0.6659
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for django_euf
CREATE DATABASE IF NOT EXISTS `django_euf` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `django_euf`;

-- Dumping structure for table django_euf.admin_menu_master
DROP TABLE IF EXISTS `admin_menu_master`;
CREATE TABLE IF NOT EXISTS `admin_menu_master` (
  `id` smallint(6) NOT NULL AUTO_INCREMENT,
  `menu_name` varchar(20) NOT NULL,
  `menu_icon` varchar(10) NOT NULL,
  `menu_route` varchar(20) NOT NULL,
  `menu_order` smallint(6) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `menu_name` (`menu_name`),
  UNIQUE KEY `menu_route` (`menu_route`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_euf.admin_menu_master: ~6 rows (approximately)
DELETE FROM `admin_menu_master`;
INSERT INTO `admin_menu_master` (`id`, `menu_name`, `menu_icon`, `menu_route`, `menu_order`, `status`, `deleted`, `deleted_at`, `created_at`, `updated_at`) VALUES
	(1, 'Dashboard', 'home', 'dashboard', 1, 1, 0, NULL, '2023-04-06 20:11:12.417713', '2023-04-06 20:11:12.417713'),
	(2, 'Users', 'users', 'users', 2, 1, 0, NULL, '2023-04-06 20:11:41.639915', '2023-04-06 20:11:41.639915'),
	(3, 'Sample Form', 'list', 'my-form', 3, 1, 0, NULL, '2023-04-06 21:59:57.474732', '2023-04-06 21:59:57.474732'),
	(4, 'Knowledge Objects', 'link', 'knowledge-objects', 4, 1, 0, NULL, '2023-04-06 22:00:09.641949', '2023-04-06 22:00:09.641949'),
	(5, 'PDF2Text (API)', 'file-text', 'pdf2text', 5, 1, 0, NULL, '2023-04-06 22:01:27.687624', '2023-04-06 22:01:27.687624'),
	(6, 'Pagination', 'book-open', 'pagination', 6, 1, 0, NULL, '2023-04-08 09:15:01.889719', '2023-04-08 09:15:01.889719');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
