-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.32 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table django_dason.account_emailaddress

USE django_dason;

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS `account_emailaddress`;
CREATE TABLE IF NOT EXISTS `account_emailaddress` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `primary` tinyint(1) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `account_emailaddress_user_id_2c513194_fk_auth_user_id` (`user_id`),
  CONSTRAINT `account_emailaddress_user_id_2c513194_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.account_emailaddress: ~0 rows (approximately)
DELETE FROM `account_emailaddress`;
/*!40000 ALTER TABLE `account_emailaddress` DISABLE KEYS */;
INSERT INTO `account_emailaddress` (`id`, `email`, `verified`, `primary`, `user_id`) VALUES
	(1, 'p.bapat@maastrichtuniversity.nl', 1, 1, 1);
/*!40000 ALTER TABLE `account_emailaddress` ENABLE KEYS */;

-- Dumping structure for table django_dason.account_emailconfirmation
DROP TABLE IF EXISTS `account_emailconfirmation`;
CREATE TABLE IF NOT EXISTS `account_emailconfirmation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `sent` datetime(6) DEFAULT NULL,
  `key` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email_address_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`),
  KEY `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` (`email_address_id`),
  CONSTRAINT `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` FOREIGN KEY (`email_address_id`) REFERENCES `account_emailaddress` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.account_emailconfirmation: ~0 rows (approximately)
DELETE FROM `account_emailconfirmation`;
/*!40000 ALTER TABLE `account_emailconfirmation` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_emailconfirmation` ENABLE KEYS */;

-- Dumping structure for table django_dason.auth_group
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.auth_group: ~1 rows (approximately)
DELETE FROM `auth_group`;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` (`id`, `name`) VALUES
	(1, 'contributors');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;

-- Dumping structure for table django_dason.auth_group_permissions
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.auth_group_permissions: ~0 rows (approximately)
DELETE FROM `auth_group_permissions`;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;

-- Dumping structure for table django_dason.auth_permission
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.auth_permission: ~60 rows (approximately)
DELETE FROM `auth_permission`;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 2, 'add_permission'),
	(6, 'Can change permission', 2, 'change_permission'),
	(7, 'Can delete permission', 2, 'delete_permission'),
	(8, 'Can view permission', 2, 'view_permission'),
	(9, 'Can add group', 3, 'add_group'),
	(10, 'Can change group', 3, 'change_group'),
	(11, 'Can delete group', 3, 'delete_group'),
	(12, 'Can view group', 3, 'view_group'),
	(13, 'Can add user', 4, 'add_user'),
	(14, 'Can change user', 4, 'change_user'),
	(15, 'Can delete user', 4, 'delete_user'),
	(16, 'Can view user', 4, 'view_user'),
	(17, 'Can add content type', 5, 'add_contenttype'),
	(18, 'Can change content type', 5, 'change_contenttype'),
	(19, 'Can delete content type', 5, 'delete_contenttype'),
	(20, 'Can view content type', 5, 'view_contenttype'),
	(21, 'Can add session', 6, 'add_session'),
	(22, 'Can change session', 6, 'change_session'),
	(23, 'Can delete session', 6, 'delete_session'),
	(24, 'Can view session', 6, 'view_session'),
	(25, 'Can add site', 7, 'add_site'),
	(26, 'Can change site', 7, 'change_site'),
	(27, 'Can delete site', 7, 'delete_site'),
	(28, 'Can view site', 7, 'view_site'),
	(29, 'Can add email address', 8, 'add_emailaddress'),
	(30, 'Can change email address', 8, 'change_emailaddress'),
	(31, 'Can delete email address', 8, 'delete_emailaddress'),
	(32, 'Can view email address', 8, 'view_emailaddress'),
	(33, 'Can add email confirmation', 9, 'add_emailconfirmation'),
	(34, 'Can change email confirmation', 9, 'change_emailconfirmation'),
	(35, 'Can delete email confirmation', 9, 'delete_emailconfirmation'),
	(36, 'Can view email confirmation', 9, 'view_emailconfirmation'),
	(37, 'Can add social account', 10, 'add_socialaccount'),
	(38, 'Can change social account', 10, 'change_socialaccount'),
	(39, 'Can delete social account', 10, 'delete_socialaccount'),
	(40, 'Can view social account', 10, 'view_socialaccount'),
	(41, 'Can add social application', 11, 'add_socialapp'),
	(42, 'Can change social application', 11, 'change_socialapp'),
	(43, 'Can delete social application', 11, 'delete_socialapp'),
	(44, 'Can view social application', 11, 'view_socialapp'),
	(45, 'Can add social application token', 12, 'add_socialtoken'),
	(46, 'Can change social application token', 12, 'change_socialtoken'),
	(47, 'Can delete social application token', 12, 'delete_socialtoken'),
	(48, 'Can view social application token', 12, 'view_socialtoken'),
	(49, 'Can add TOTP device', 13, 'add_totpdevice'),
	(50, 'Can change TOTP device', 13, 'change_totpdevice'),
	(51, 'Can delete TOTP device', 13, 'delete_totpdevice'),
	(52, 'Can view TOTP device', 13, 'view_totpdevice'),
	(53, 'Can add static device', 14, 'add_staticdevice'),
	(54, 'Can change static device', 14, 'change_staticdevice'),
	(55, 'Can delete static device', 14, 'delete_staticdevice'),
	(56, 'Can view static device', 14, 'view_staticdevice'),
	(57, 'Can add static token', 15, 'add_statictoken'),
	(58, 'Can change static token', 15, 'change_statictoken'),
	(59, 'Can delete static token', 15, 'delete_statictoken'),
	(60, 'Can view static token', 15, 'view_statictoken');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;

-- Dumping structure for table django_dason.auth_user
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.auth_user: ~1 rows (approximately)
DELETE FROM `auth_user`;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$260000$6VZfvPsfplcvrBhpN01nYT$2bWNS3/2WAP9NKPPp4C6UmBFgUTmJReS5Z3nwhjdLqE=', '2023-03-07 15:43:41.554382', 1, 'pranav', 'Pranav', 'Bapat', 'p.bapat@maastrichtuniversity.nl', 1, 1, '2023-03-02 12:54:10.000000'),
	(2, 'pbkdf2_sha256$260000$P3gNUSs5oXxB11Kqyebrmn$hoAHEaPyv73ZE6OvmM7d0HJkJCLCSFfAjOsP6PUhBKQ=', '2023-03-07 11:50:41.580294', 0, 'aaron37', 'Aaron', 'Wang', '', 1, 1, '2023-03-07 11:49:45.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;

-- Dumping structure for table django_dason.auth_user_groups
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.auth_user_groups: ~1 rows (approximately)
DELETE FROM `auth_user_groups`;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
	(1, 2, 1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;

-- Dumping structure for table django_dason.auth_user_user_permissions
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.auth_user_user_permissions: ~0 rows (approximately)
DELETE FROM `auth_user_user_permissions`;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;

-- Dumping structure for table django_dason.django_admin_log
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.django_admin_log: ~4 rows (approximately)
DELETE FROM `django_admin_log`;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
	(1, '2023-03-07 11:49:06.885019', '1', 'contributors', 1, '[{"added": {}}]', 3, 1),
	(2, '2023-03-07 11:49:45.400566', '2', 'aaron37', 1, '[{"added": {}}]', 4, 1),
	(3, '2023-03-07 11:50:02.103963', '2', 'aaron37', 2, '[{"changed": {"fields": ["First name", "Last name", "Staff status", "Groups"]}}]', 4, 1),
	(4, '2023-03-07 11:50:22.362186', '1', 'pranav', 2, '[{"changed": {"fields": ["First name", "Last name"]}}]', 4, 1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;

-- Dumping structure for table django_dason.django_content_type
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.django_content_type: ~15 rows (approximately)
DELETE FROM `django_content_type`;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(8, 'account', 'emailaddress'),
	(9, 'account', 'emailconfirmation'),
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(5, 'contenttypes', 'contenttype'),
	(14, 'otp_static', 'staticdevice'),
	(15, 'otp_static', 'statictoken'),
	(13, 'otp_totp', 'totpdevice'),
	(6, 'sessions', 'session'),
	(7, 'sites', 'site'),
	(10, 'socialaccount', 'socialaccount'),
	(11, 'socialaccount', 'socialapp'),
	(12, 'socialaccount', 'socialtoken');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;

-- Dumping structure for table django_dason.django_migrations
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.django_migrations: ~29 rows (approximately)
DELETE FROM `django_migrations`;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2023-03-02 12:53:37.482280'),
	(2, 'auth', '0001_initial', '2023-03-02 12:53:37.843279'),
	(3, 'account', '0001_initial', '2023-03-02 12:53:37.964280'),
	(4, 'account', '0002_email_max_length', '2023-03-02 12:53:37.990280'),
	(5, 'admin', '0001_initial', '2023-03-02 12:53:38.105279'),
	(6, 'admin', '0002_logentry_remove_auto_add', '2023-03-02 12:53:38.116279'),
	(7, 'admin', '0003_logentry_add_action_flag_choices', '2023-03-02 12:53:38.128280'),
	(8, 'contenttypes', '0002_remove_content_type_name', '2023-03-02 12:53:38.202282'),
	(9, 'auth', '0002_alter_permission_name_max_length', '2023-03-02 12:53:38.253284'),
	(10, 'auth', '0003_alter_user_email_max_length', '2023-03-02 12:53:38.290280'),
	(11, 'auth', '0004_alter_user_username_opts', '2023-03-02 12:53:38.300280'),
	(12, 'auth', '0005_alter_user_last_login_null', '2023-03-02 12:53:38.356279'),
	(13, 'auth', '0006_require_contenttypes_0002', '2023-03-02 12:53:38.359280'),
	(14, 'auth', '0007_alter_validators_add_error_messages', '2023-03-02 12:53:38.375280'),
	(15, 'auth', '0008_alter_user_username_max_length', '2023-03-02 12:53:38.430278'),
	(16, 'auth', '0009_alter_user_last_name_max_length', '2023-03-02 12:53:38.487278'),
	(17, 'auth', '0010_alter_group_name_max_length', '2023-03-02 12:53:38.511279'),
	(18, 'auth', '0011_update_proxy_permissions', '2023-03-02 12:53:38.525280'),
	(19, 'auth', '0012_alter_user_first_name_max_length', '2023-03-02 12:53:38.583278'),
	(20, 'otp_static', '0001_initial', '2023-03-02 12:53:38.708279'),
	(21, 'otp_static', '0002_throttling', '2023-03-02 12:53:38.786279'),
	(22, 'otp_totp', '0001_initial', '2023-03-02 12:53:38.858279'),
	(23, 'otp_totp', '0002_auto_20190420_0723', '2023-03-02 12:53:38.937278'),
	(24, 'sessions', '0001_initial', '2023-03-02 12:53:38.968281'),
	(25, 'sites', '0001_initial', '2023-03-02 12:53:38.987279'),
	(26, 'sites', '0002_alter_domain_unique', '2023-03-02 12:53:39.003281'),
	(27, 'socialaccount', '0001_initial', '2023-03-02 12:53:39.291278'),
	(28, 'socialaccount', '0002_token_max_lengths', '2023-03-02 12:53:39.366279'),
	(29, 'socialaccount', '0003_extra_data_default_dict', '2023-03-02 12:53:39.382279');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;

-- Dumping structure for table django_dason.django_session
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.django_session: ~2 rows (approximately)
DELETE FROM `django_session`;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('g9g8gag7q3s2gmpn1ro5o0nococ2oi4q', '.eJxVjMsOwiAQRf-FtSG0vKYu3fsNZIDBogZMaRON8d9tky50e8-5580cLvPolkaTy5EdWccOv5vHcKOygXjFcqk81DJP2fNN4Ttt_Fwj3U-7-xcYsY3rG1EHgBgHIUknA3aIKWlUdjAgFSmAIGQ02HvbiZWRkV2PJL1NikDjFm3UWq7F0fORpxc7is8XmuY_Xg:1pZZSy:lfbviL4BWU3JojgWRqDx2DtIwVCicid40zlT8K7kxps', '2023-03-21 15:43:04.045264'),
	('zpa284v9xx8byx6131o36ly3tx6osjzl', '.eJxVjDsOwjAQBe_iGll2_FtT0ucM1tq7xgGUSPlUiLuTSCmgfTPz3iLhtra0LTyngcRVaHH53TKWJ48HoAeO90mWaVznIctDkSddZD8Rv26n-3fQcGl7jegKAFFUhl31ECLV6tCG6MFYtgBFGfLY5aDVztgb3SGbHKplcCg-X-38OCE:1pZZTZ:vtvATLOfIXZ-I5PWQXlHsU6vY0sue0s2d6BnwLMY6KU', '2023-03-21 15:43:41.557410');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;

-- Dumping structure for table django_dason.django_site
DROP TABLE IF EXISTS `django_site`;
CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.django_site: ~0 rows (approximately)
DELETE FROM `django_site`;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
	(2, 'example.com', 'example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;

-- Dumping structure for table django_dason.otp_static_staticdevice
DROP TABLE IF EXISTS `otp_static_staticdevice`;
CREATE TABLE IF NOT EXISTS `otp_static_staticdevice` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `confirmed` tinyint(1) NOT NULL,
  `user_id` int NOT NULL,
  `throttling_failure_count` int unsigned NOT NULL,
  `throttling_failure_timestamp` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `otp_static_staticdevice_user_id_7f9cff2b_fk_auth_user_id` (`user_id`),
  CONSTRAINT `otp_static_staticdevice_user_id_7f9cff2b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `otp_static_staticdevice_chk_1` CHECK ((`throttling_failure_count` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.otp_static_staticdevice: ~1 rows (approximately)
DELETE FROM `otp_static_staticdevice`;
/*!40000 ALTER TABLE `otp_static_staticdevice` DISABLE KEYS */;
INSERT INTO `otp_static_staticdevice` (`id`, `name`, `confirmed`, `user_id`, `throttling_failure_count`, `throttling_failure_timestamp`) VALUES
	(1, 'backup', 1, 1, 0, NULL);
/*!40000 ALTER TABLE `otp_static_staticdevice` ENABLE KEYS */;

-- Dumping structure for table django_dason.otp_static_statictoken
DROP TABLE IF EXISTS `otp_static_statictoken`;
CREATE TABLE IF NOT EXISTS `otp_static_statictoken` (
  `id` int NOT NULL AUTO_INCREMENT,
  `token` varchar(16) COLLATE utf8mb4_unicode_ci NOT NULL,
  `device_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `otp_static_statictok_device_id_74b7c7d1_fk_otp_stati` (`device_id`),
  KEY `otp_static_statictoken_token_d0a51866` (`token`),
  CONSTRAINT `otp_static_statictok_device_id_74b7c7d1_fk_otp_stati` FOREIGN KEY (`device_id`) REFERENCES `otp_static_staticdevice` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.otp_static_statictoken: ~3 rows (approximately)
DELETE FROM `otp_static_statictoken`;
/*!40000 ALTER TABLE `otp_static_statictoken` DISABLE KEYS */;
INSERT INTO `otp_static_statictoken` (`id`, `token`, `device_id`) VALUES
	(1, 'bva555q3', 1),
	(2, 'n7bbufww', 1),
	(3, '3r5bmow3', 1);
/*!40000 ALTER TABLE `otp_static_statictoken` ENABLE KEYS */;

-- Dumping structure for table django_dason.otp_totp_totpdevice
DROP TABLE IF EXISTS `otp_totp_totpdevice`;
CREATE TABLE IF NOT EXISTS `otp_totp_totpdevice` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `confirmed` tinyint(1) NOT NULL,
  `key` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `step` smallint unsigned NOT NULL,
  `t0` bigint NOT NULL,
  `digits` smallint unsigned NOT NULL,
  `tolerance` smallint unsigned NOT NULL,
  `drift` smallint NOT NULL,
  `last_t` bigint NOT NULL,
  `user_id` int NOT NULL,
  `throttling_failure_count` int unsigned NOT NULL,
  `throttling_failure_timestamp` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `otp_totp_totpdevice_user_id_0fb18292_fk_auth_user_id` (`user_id`),
  CONSTRAINT `otp_totp_totpdevice_user_id_0fb18292_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `otp_totp_totpdevice_chk_1` CHECK ((`step` >= 0)),
  CONSTRAINT `otp_totp_totpdevice_chk_2` CHECK ((`digits` >= 0)),
  CONSTRAINT `otp_totp_totpdevice_chk_3` CHECK ((`tolerance` >= 0)),
  CONSTRAINT `otp_totp_totpdevice_chk_4` CHECK ((`throttling_failure_count` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.otp_totp_totpdevice: ~1 rows (approximately)
DELETE FROM `otp_totp_totpdevice`;
/*!40000 ALTER TABLE `otp_totp_totpdevice` DISABLE KEYS */;
INSERT INTO `otp_totp_totpdevice` (`id`, `name`, `confirmed`, `key`, `step`, `t0`, `digits`, `tolerance`, `drift`, `last_t`, `user_id`, `throttling_failure_count`, `throttling_failure_timestamp`) VALUES
	(1, '', 1, '24a57e65ef9ad31d66b23d93c251bc1e2a081d70', 30, 0, 6, 1, 0, 55940133, 1, 0, NULL);
/*!40000 ALTER TABLE `otp_totp_totpdevice` ENABLE KEYS */;

-- Dumping structure for table django_dason.socialaccount_socialaccount
DROP TABLE IF EXISTS `socialaccount_socialaccount`;
CREATE TABLE IF NOT EXISTS `socialaccount_socialaccount` (
  `id` int NOT NULL AUTO_INCREMENT,
  `provider` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `uid` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `extra_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialaccount_socialaccount_provider_uid_fc810c6e_uniq` (`provider`,`uid`),
  KEY `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id` (`user_id`),
  CONSTRAINT `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.socialaccount_socialaccount: ~0 rows (approximately)
DELETE FROM `socialaccount_socialaccount`;
/*!40000 ALTER TABLE `socialaccount_socialaccount` DISABLE KEYS */;
/*!40000 ALTER TABLE `socialaccount_socialaccount` ENABLE KEYS */;

-- Dumping structure for table django_dason.socialaccount_socialapp
DROP TABLE IF EXISTS `socialaccount_socialapp`;
CREATE TABLE IF NOT EXISTS `socialaccount_socialapp` (
  `id` int NOT NULL AUTO_INCREMENT,
  `provider` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `client_id` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `secret` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `key` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.socialaccount_socialapp: ~0 rows (approximately)
DELETE FROM `socialaccount_socialapp`;
/*!40000 ALTER TABLE `socialaccount_socialapp` DISABLE KEYS */;
/*!40000 ALTER TABLE `socialaccount_socialapp` ENABLE KEYS */;

-- Dumping structure for table django_dason.socialaccount_socialapp_sites
DROP TABLE IF EXISTS `socialaccount_socialapp_sites`;
CREATE TABLE IF NOT EXISTS `socialaccount_socialapp_sites` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `socialapp_id` int NOT NULL,
  `site_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialaccount_socialapp_sites_socialapp_id_site_id_71a9a768_uniq` (`socialapp_id`,`site_id`),
  KEY `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` (`site_id`),
  CONSTRAINT `socialaccount_social_socialapp_id_97fb6e7d_fk_socialacc` FOREIGN KEY (`socialapp_id`) REFERENCES `socialaccount_socialapp` (`id`),
  CONSTRAINT `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.socialaccount_socialapp_sites: ~0 rows (approximately)
DELETE FROM `socialaccount_socialapp_sites`;
/*!40000 ALTER TABLE `socialaccount_socialapp_sites` DISABLE KEYS */;
/*!40000 ALTER TABLE `socialaccount_socialapp_sites` ENABLE KEYS */;

-- Dumping structure for table django_dason.socialaccount_socialtoken
DROP TABLE IF EXISTS `socialaccount_socialtoken`;
CREATE TABLE IF NOT EXISTS `socialaccount_socialtoken` (
  `id` int NOT NULL AUTO_INCREMENT,
  `token` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `token_secret` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expires_at` datetime(6) DEFAULT NULL,
  `account_id` int NOT NULL,
  `app_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq` (`app_id`,`account_id`),
  KEY `socialaccount_social_account_id_951f210e_fk_socialacc` (`account_id`),
  CONSTRAINT `socialaccount_social_account_id_951f210e_fk_socialacc` FOREIGN KEY (`account_id`) REFERENCES `socialaccount_socialaccount` (`id`),
  CONSTRAINT `socialaccount_social_app_id_636a42d7_fk_socialacc` FOREIGN KEY (`app_id`) REFERENCES `socialaccount_socialapp` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table django_dason.socialaccount_socialtoken: ~0 rows (approximately)
DELETE FROM `socialaccount_socialtoken`;
/*!40000 ALTER TABLE `socialaccount_socialtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `socialaccount_socialtoken` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

SET FOREIGN_KEY_CHECKS = 1;

SELECT * FROM auth_permission LIMIT 5;