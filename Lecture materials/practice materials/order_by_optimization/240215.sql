CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    created_at DATETIME
);

SELECT COUNT(*) FROM product;

SELECT * FROM product
ORDER BY created_at DESC, price ASC
LIMIT 10;

EXPLAIN SELECT * FROM product
ORDER BY created_at DESC, price ASC
LIMIT 10;

EXPLAIN ANALYZE SELECT * FROM product
ORDER BY created_at DESC, price ASC
LIMIT 10;

CREATE INDEX idx_created_at_price ON product(created_at DESC, price ASC);

SHOW VARIABLES LIKE 'sort_buffer_size';

SHOW STATUS LIKE 'sort_merge_passes';

SET SESSION sort_buffer_size = 10 * 262144;

EXPLAIN SELECT * FROM product
ORDER BY name
LIMIT 1000;

EXPLAIN ANALYZE SELECT * FROM product
ORDER BY name
LIMIT 1000;