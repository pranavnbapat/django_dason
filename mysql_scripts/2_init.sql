CREATE DATABASE IF NOT EXISTS `django_dason` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE django_dason;

CREATE USER 'pranav'@'%' IDENTIFIED BY 'asdasdasd';

GRANT ALL PRIVILEGES ON `django_dason`.* TO 'pranav'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;
