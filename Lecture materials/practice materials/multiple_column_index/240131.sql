CREATE TABLE orders (
order_id INT AUTO_INCREMENT,
customer_id INT,
order_date DATE,
product_id INT,
quantity INT,
status VARCHAR(50),
PRIMARY KEY (order_id)
);

SELECT * FROM orders
WHERE customer_id = 3905
  AND order_date > '2023-11-04'
ORDER BY order_date DESC
LIMIT 10;

EXPLAIN SELECT * FROM orders
WHERE customer_id = 3905
  AND order_date > '2023-11-04'
ORDER BY order_date DESC
LIMIT 10;

DROP INDEX idx_order_date_customer_id ON orders;

CREATE INDEX idx_order_date_customer_id ON orders(order_date, customer_id);

CREATE INDEX idx_customer_id_order_date ON orders(customer_id, order_date);

ANALYZE TABLE orders UPDATE HISTOGRAM ON customer_id, status WITH 100 BUCKETS;

USE information_schema;

SELECT * FROM COLUMN_STATISTICS
 WHERE TABLE_NAME = 'orders';