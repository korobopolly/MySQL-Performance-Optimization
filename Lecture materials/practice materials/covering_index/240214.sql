SELECT * FROM orders;

CREATE TABLE cover_orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2) NOT NULL
);

CREATE INDEX idx_customer_id_order_date ON cover_orders(customer_id, order_date);
CREATE INDEX idx_covering ON cover_orders(customer_id, order_date,total_amount);

SELECT * FROM cover_orders
WHERE customer_id = 25675
ORDER BY  order_date DESC
LIMIT 10;

EXPLAIN SELECT * FROM cover_orders
WHERE customer_id = 25675
ORDER BY  order_date DESC
LIMIT 10;

EXPLAIN ANALYZE SELECT * FROM cover_orders
WHERE customer_id = 25675
ORDER BY  order_date DESC
LIMIT 10;