CREATE TABLE coupons (
id INT AUTO_INCREMENT PRIMARY KEY,
status VARCHAR(20) NOT NULL,
user_id INT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
expires_at DATETIME
);

START TRANSACTION;

SELECT * FROM coupons
WHERE status = 'available'
ORDER BY id
LIMIT 100
FOR UPDATE;

show processlist;
KILL 33;

UPDATE coupons SET status = 'available';
UPDATE coupons SET user_id = NULL;
COMMIT;