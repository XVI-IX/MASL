CREATE DATABASE lcassessment;

USE lcassessment;

-- Create Operation
CREATE TABLE IF NOT EXISTS `users` {
  id INTEGER NOT NULL AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  other VARCHAR(255),
  email VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  profile_url VARCHAR(255),
  phone VARCHAR(255) UNIQUE NOT NULL,
  created_at DATETIME NOT NULL DEFAULT(CURRENT_TIMESTAMP()),
  modified_at DATETIME NOT NULL DEFAULT(CURRENT_TIMESTAMP()),
  PRIMARY KEY(id)
};


INSERT INTO `users` (username, first_name, last_name, other, email, password, profile_url, phone, created_at, modified_at)
VALUES
('mike_johnson', 'Mike', 'Johnson', 'Additional info', 'mike@examplemail.com', 'hashed_password', NULL, '123456789', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
('Morty', 'Rick', 'Roiland', 'Additional info', 'morty@rckandmorty.com', 'hashed_password', NULL, '123456789', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);


-- Update Operation
UPDATE `users`
SET username = 'lollisweet'
WHERE first_name = 'Mike';

-- Read Operation
SELECT * FROM `users`
WHERE first_name = 'Mike';

-- Delete Operation
DELETE FROM `users`
WHERE first_name = 'Mike';