CREATE DATABASE IF NOT EXISTS `django_euf` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE django_euf;

CREATE USER IF NOT EXISTS 'euf_admin'@'%' IDENTIFIED BY 'asdasdasd';

GRANT ALL PRIVILEGES ON `django_euf`.* TO 'euf_admin'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;
