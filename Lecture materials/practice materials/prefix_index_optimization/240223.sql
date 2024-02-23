CREATE TABLE world_cities (
city VARCHAR(100),
city_ascii VARCHAR(100),
lat DECIMAL(10, 7),
lng DECIMAL(10, 7),
country VARCHAR(100),
iso2 CHAR(2),
iso3 CHAR(3),
admin_name VARCHAR(100),
capital VARCHAR(50),
population BIGINT,
id INT PRIMARY KEY
);

SELECT COUNT(*) AS c, city
FROM world_cities
GROUP BY city
ORDER BY c DESC
LIMIT 10;

SELECT COUNT(*) AS c, LEFT(city,8) AS pref
FROM world_cities
GROUP BY pref
ORDER BY c DESC
LIMIT 10;

CREATE INDEX idx_city_prefix ON world_cities (city(8));