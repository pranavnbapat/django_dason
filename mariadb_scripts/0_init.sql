CREATE DATABASE IF NOT EXISTS `django_euf` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE django_euf;

CREATE USER 'euf_admin'@'localhost' IDENTIFIED BY 'asdasdasd';

GRANT ALL PRIVILEGES ON `django_euf`.* TO 'euf_admin'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;
