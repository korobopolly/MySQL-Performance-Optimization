CREATE TABLE user_activity_logs (
id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT,
activity_type VARCHAR(50),
activity_timestamp DATETIME,
additional_info TEXT
);

SHOW GLOBAL VARIABLES LIKE 'local_infile';

TRUNCATE TABLE user_activity_logs;

SELECT COUNT(*) FROM user_activity_logs;

SELECT * FROM user_activity_logs LIMIT 100;
