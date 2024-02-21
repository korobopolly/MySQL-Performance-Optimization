SHOW VARIABLES LIKE 'performance_schema';

UPDATE performance_schema.setup_instruments SET ENABLED = 'YES', TIMED = 'YES' WHERE NAME LIKE 'statement/%';
UPDATE performance_schema.setup_instruments SET ENABLED = 'YES', TIMED = 'YES' WHERE NAME LIKE 'stage/%';
UPDATE performance_schema.setup_consumers SET ENABLED = 'YES' WHERE NAME LIKE 'events_stages%';
UPDATE performance_schema.setup_consumers SET ENABLED = 'YES' WHERE NAME LIKE 'events_statements%';

CREATE TABLE index_orders (
id INT AUTO_INCREMENT PRIMARY KEY,
customer_id INT NOT NULL,
order_date DATE NOT NULL,
total_amount DECIMAL(10, 2) NOT NULL
);

CREATE INDEX idx_customer_order ON index_orders(customer_id,order_date);

SHOW SESSION VARIABLES LIKE 'eq_range_index_dive_limit';

SELECT *
FROM index_orders
WHERE customer_id IN (101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120);

SELECT *
FROM index_orders FORCE INDEX (idx_customer_order)
WHERE customer_id IN (101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120);

SELECT *
FROM index_orders
WHERE customer_id IN (101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140);

SELECT *
FROM index_orders FORCE INDEX (idx_customer_order)
WHERE customer_id IN (101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140);

SELECT stages.EVENT_ID, statements.EVENT_ID, statements.END_EVENT_ID, statements.SQL_TEXT, stages.EVENT_NAME, stages.TIMER_WAIT/1000000000 AS Time
FROM performance_schema.events_stages_history_long AS stages
JOIN performance_schema.events_statements_history_long AS statements
ON (stages.EVENT_ID >= statements.EVENT_ID AND stages.EVENT_ID <= statements.END_EVENT_ID)
WHERE stages.EVENT_NAME LIKE '%statistics%'
AND statements.SQL_TEXT LIKE '%FROM index_orders%'
AND statements.SQL_TEXT NOT LIKE '%SELECT stages.EVENT_ID,%'
ORDER BY statements.EVENT_ID DESC;


TRUNCATE TABLE performance_schema.events_statements_history_long;
TRUNCATE TABLE performance_schema.events_stages_history_long;
