CREATE TABLE chat_msgs (
  id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  sender_id INT NOT NULL,
  text TEXT NOT NULL COLLATE utf8mb4_unicode_ci,
  is_deleted BOOLEAN DEFAULT FALSE,
  deleted_at TIMESTAMP DEFAULT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UPDATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  -- add other message fields as needed
  FOREIGN KEY (sender_id) REFERENCES auth_user(id)
);

CREATE TABLE chat_msgs_recipients (
  message_id INT UNSIGNED NOT NULL,
  recipient_id INT NOT NULL,
  is_read BOOLEAN DEFAULT FALSE,
  is_deleted BOOLEAN DEFAULT FALSE,
  deleted_at TIMESTAMP DEFAULT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  -- add other recipient fields as needed
  FOREIGN KEY (message_id) REFERENCES chat_msgs(id),
  FOREIGN KEY (recipient_id) REFERENCES auth_user(id),
  PRIMARY KEY (message_id, recipient_id)
);