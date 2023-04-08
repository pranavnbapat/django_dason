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

-- Dumping structure for table django_euf.countries_master
DROP TABLE IF EXISTS `countries_master`;
CREATE TABLE IF NOT EXISTS `countries_master` (
  `id` smallint(6) NOT NULL AUTO_INCREMENT,
  `country` varchar(50) NOT NULL,
  `country_code` varchar(2) NOT NULL,
  `calling_code` varchar(4) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_euf.countries_master: ~27 rows (approximately)
DELETE FROM `countries_master`;
INSERT INTO `countries_master` (`id`, `country`, `country_code`, `calling_code`, `status`, `deleted`, `deleted_at`, `created_at`, `updated_at`) VALUES
	(1, 'Austria', 'AT', '+43', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(2, 'Belgium', 'BE', '+32', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(3, 'Bulgaria', 'BG', '+359', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(4, 'Croatia', 'HR', '+385', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(5, 'Cyprus', 'CY', '+357', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(6, 'Czech Republic', 'CZ', '+420', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(7, 'Denmark', 'DK', '+45', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(8, 'Estonia', 'EE', '+372', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(9, 'Finland', 'FI', '+358', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(10, 'France', 'FR', '+33', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(11, 'Germany', 'DE', '+49', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(12, 'Greece', 'GR', '+30', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(13, 'Hungary', 'HU', '+36', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(14, 'Ireland', 'IE', '+353', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(15, 'Italy', 'IT', '+39', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(16, 'Latvia', 'LV', '+371', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(17, 'Lithuania', 'LT', '+370', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(18, 'Luxembourg', 'LU', '+352', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(19, 'Malta', 'MT', '+356', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(20, 'Netherlands', 'NL', '+31', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(21, 'Poland', 'PL', '+48', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(22, 'Portugal', 'PT', '+351', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(23, 'Romania', 'RO', '+40', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(24, 'Slovakia', 'SK', '+421', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(25, 'Slovenia', 'SI', '+386', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(26, 'Spain', 'ES', '+34', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000'),
	(27, 'Sweden', 'SE', '+46', 1, 0, NULL, '2023-04-08 11:10:56.000000', '2023-04-08 11:10:56.000000');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
