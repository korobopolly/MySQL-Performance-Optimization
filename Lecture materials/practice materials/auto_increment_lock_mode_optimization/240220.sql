CREATE TABLE shopping_cart (
 cart_id INT AUTO_INCREMENT PRIMARY KEY,
 user_id INT NOT NULL,
 product_id INT NOT NULL,
 quantity INT NOT NULL,
 cart_added_date DATETIME NOT NULL
);

CREATE TABLE shopping_orders (
 order_id INT AUTO_INCREMENT PRIMARY KEY,
 user_id INT NOT NULL,
 product_id INT NOT NULL,
 quantity INT NOT NULL,
 order_date DATETIME NOT NULL
);

SELECT COUNT(*) FROM shopping_cart;

SELECT COUNT(*) FROM shopping_orders;

select * from shopping_orders;

SHOW GLOBAL VARIABLES LIKE 'innodb_autoinc_lock_mode';

TRUNCATE shopping_orders;
