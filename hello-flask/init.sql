CREATE DATABASE IF NOT EXISTS db;
USE db;

-- Create user and grant access
CREATE USER IF NOT EXISTS 'admin'@'%' IDENTIFIED BY 'admin123';
GRANT ALL PRIVILEGES ON db.* TO 'admin'@'%';
FLUSH PRIVILEGES;

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    description VARCHAR(100)
);

-- Insert test data
INSERT INTO users (name, description) VALUES
  ('maryam', 'donut');
