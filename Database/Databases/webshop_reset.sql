-- SQL & databases course  ·  RESET: rebuilds the webshop exactly as it is after Day 3
-- WARNING: deletes the webshop tables in the open database and creates them again.
-- DB Browser: open webshop.db > Execute SQL > open this file > F5 > Ctrl+S

DROP VIEW IF EXISTS order_totals;
DROP VIEW IF EXISTS customer_orders;
DROP VIEW IF EXISTS sales_for_analysts;
DROP VIEW IF EXISTS customer_overview;
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS order_sheet;
DROP TABLE IF EXISTS big_orders;
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
  customer_id INTEGER PRIMARY KEY,
  first_name  TEXT NOT NULL,
  last_name   TEXT NOT NULL,
  email       TEXT UNIQUE,
  city        TEXT,
  joined_date TEXT
);

CREATE TABLE products (
  product_id INTEGER PRIMARY KEY,
  name       TEXT NOT NULL,
  category   TEXT,
  price      REAL,
  stock      INTEGER
);

INSERT INTO customers VALUES
(1,'Anna','Lindqvist','anna.lindqvist@example.com','Uppsala','2024-03-14'),
(2,'Erik','Johansson','erik.j@example.com','Stockholm','2023-11-02'),
(3,'Sara','Ahmed','sara.ahmed@example.com','Göteborg','2025-01-20'),
(4,'Johan','Berg','johan.berg@example.com','Uppsala','2022-06-30'),
(5,'Maria','Nilsson','maria.n@example.com','Malmö','2025-08-11'),
(6,'Ali','Hassan','ali.hassan@example.com','Stockholm','2024-09-05'),
(7,'Emma','Karlsson','emma.k@example.com','Västerås','2023-02-17'),
(8,'Oskar','Persson','oskar.p@example.com','Uppsala','2025-05-28'),
(9,'Fatima','Yilmaz','fatima.y@example.com','Göteborg','2024-12-01'),
(10,'Lukas','Ek','lukas.ek@example.com',NULL,'2026-01-09');

INSERT INTO products VALUES
(1,'Hoodie Black','Clothing',599,25),
(2,'T-shirt White','Clothing',249,60),
(3,'Cap Logo','Accessories',199,40),
(4,'Sneakers Classic','Shoes',1199,12),
(5,'Water Bottle','Accessories',149,0),
(6,'Joggers Grey','Clothing',499,18),
(7,'Backpack Urban','Accessories',749,8),
(8,'Running Shoes','Shoes',1399,5),
(9,'Socks 3-pack','Clothing',129,100),
(10,'Beanie','Accessories',179,30),
(11,'Rain Jacket','Clothing',1299,0),
(12,'Sandals','Shoes',399,22);

CREATE TABLE orders (
  order_id    INTEGER PRIMARY KEY,
  customer_id INTEGER NOT NULL,
  order_date  TEXT NOT NULL,
  status      TEXT NOT NULL DEFAULT 'new'
              CHECK (status IN ('new','shipped','delivered','cancelled')),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
  order_id   INTEGER NOT NULL,
  product_id INTEGER NOT NULL,
  quantity   INTEGER NOT NULL CHECK (quantity > 0),
  unit_price REAL NOT NULL,
  PRIMARY KEY (order_id, product_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO orders (order_id, customer_id, order_date, status)
VALUES (1, 1, '2026-01-05', 'delivered');

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (1, 1, 1, 599),
       (1, 3, 2, 199);

INSERT INTO orders (order_id, customer_id, order_date, status) VALUES
(2, 2, '2026-01-12', 'delivered'),
(3, 1, '2026-01-20', 'delivered'),
(4, 3, '2026-01-28', 'delivered'),
(5, 4, '2026-02-03', 'delivered'),
(6, 5, '2026-02-10', 'delivered'),
(7, 6, '2026-02-14', 'cancelled'),
(8, 2, '2026-02-21', 'delivered'),
(9, 8, '2026-02-27', 'shipped'),
(10, 9, '2026-03-04', 'shipped'),
(11, 1, '2026-03-09', 'shipped'),
(12, 3, '2026-03-15', 'new'),
(13, 6, '2026-03-18', 'new'),
(14, 4, '2026-03-22', 'new'),
(15, 2, '2026-03-28', 'new');

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
(2, 4, 1, 1199),
(3, 9, 3, 129),
(4, 2, 2, 249), (4, 6, 1, 499),
(5, 8, 1, 1399),
(6, 1, 1, 599), (6, 10, 1, 179),
(7, 7, 1, 749),
(8, 2, 1, 249), (8, 9, 2, 129),
(9, 11, 1, 1299),
(10, 3, 1, 199), (10, 2, 3, 249),
(11, 6, 2, 499),
(12, 4, 1, 1199), (12, 9, 1, 129),
(13, 1, 2, 599),
(14, 10, 2, 179), (14, 3, 1, 199),
(15, 8, 1, 1399), (15, 2, 1, 249);

SELECT c.first_name, c.last_name, o.status 
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id;

SELECT  customers.first_name, orders.order_id
FROM customers
JOIN orders ON orders.customer_id = customers.customer_id
WHERE customers.first_name like 'Erik';

SELECT  customers.first_name, customers.city, orders.order_id, orders.order_date
FROM customers
JOIN orders ON orders.customer_id = customers.customer_id
WHERE customers.city = 'Göteborg' 
ORDER By orders.order_date DESC;

SELECT order_items.order_id, products.name, products.category
FROM order_items
JOIN products ON products.product_id = order_items.product_id;

SELECT order_items.order_id ,products.name
FROM order_items
JOIN products ON products.product_id = order_items.product_id
WHERE products.category = 'Shoes';

SELECT products.name,  order_items.quantity ,  products.price, order_items.quantity * products.price AS line_total
FROM products
JOIN order_items ON order_items.product_id = products.product_id
WHERE order_items.order_id = 10;

SELECT customers.first_name , customers.last_name,  orders.order_date, products.name AS product_name
FROM customers
JOIN orders ON orders.customer_id = customers.customer_id
JOIN order_items ON order_items.order_id = orders.order_id
JOIN products ON products.product_id = order_items.product_id
WHERE products.name = 'Hoodie Black';

SELECT customers.first_name , orders.order_id
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.customer_id;

SELECT  products.product_id, products.name
FROM products
LEFT JOIN order_items ON order_items.product_id = products.product_id
WHERE order_items.product_id IS NULL;

SELECT customers.first_name,  products.name, order_items.quantity
FROM customers 
JOIN orders ON orders.customer_id = customers.customer_id
JOIN order_items ON order_items.order_id = orders.order_id
JOIN products ON products.product_id = order_items.product_id
WHERE customers.city = 'Uppsala';

SELECT * 
FROM products 
WHERE category IN ('Clothing' , 'Accessories') 
AND price BETWEEN 150 AND 500;

SELECT *
FROM orders
WHERE  strftime('%Y-%m', order_date) = '2026-02'
AND status <>   'cancelled';

SELECT orders.order_id, products.name, order_items.quantity, order_items.quantity * products.price AS total_value
FROM orders
JOIN order_items ON order_items.order_id = orders.order_id 
JOIN products ON products.product_id = order_items.product_id
WHERE  total_value > 500  ORDER BY total_value DESC;

SELECT DISTINCT customers.customer_id ,customers.first_name, customers.city
FROM customers
JOIN orders ON orders.customer_id = customers.customer_id 
WHERE customers.city IN ('Stockholm', 'Uppsala');

-- Revert eercises

SELECT count (*) FROM orders

SELECT * FROM orders;
SELECT * FROM customers
SELECT * FROM products
SELECT * FROM order_items
INSERT INTO customers VALUES (11, 'Leo', 'Falk', 'leo@falk.com', 'Uppsala', '2026-02-09' );
UPDATE  customers SET joined_date = '2026-10-09' WHERE customer_id = 11;
INSERT INTO orders VALUES(16, 11, '2026-10-09', 'new')
INSERT INTO order_items VALUES(16, 1, 1, 599.0);
INSERT INTO order_items VALUES(16, 9 , 2, 129.0);
SELECT customers.customer_id, customers.first_name, products.name, orders.status, products.price, order_items.quantity, order_items.quantity * order_items.unit_price AS total_value
FROM customers
JOIN  orders ON orders.customer_id = customers.customer_id
JOIN order_items ON order_items.order_id = orders.order_id
JOIN products ON products.product_id = order_items.product_id
WHERE customers.customer_id = 11

UPDATE  orders SET status = 'cancelled' WHERE order_id = 12;
DELETE FROM order_items WHERE order_id = 12;
UPDATE products set stock = 13 WHERE product_id = 4;
UPDATE products set stock = 101 WHERE product_id = 9;


ALTER TABLE products ADD COLUMN disccount_percent DEFAULT 0 CHECK ( disccount_percent BETWEEN 0 AND 90);
UPDATE products set disccount_percent = 20 WHERE category = 'Shoes';
SELECT *, price - (price * disccount_percent / 100) AS final_price FROM products;

SELECT products.name , products.category, orders.order_date
FROM products
LEFT JOIN order_items ON order_items.product_id = products.product_id
LEFT JOIN  orders ON orders.order_id = order_items.order_id ORDER BY products.name;

SELECT DISTINCT customers.first_name
FROM customers
JOIN orders ON orders.customer_id = customers.customer_id
JOIN order_items ON order_items.order_id = orders.order_id
JOIN products ON products.product_id = order_items.product_id
WHERE products.category = 'Shoes'; 

SELECT c1.first_name as customer1, c2.first_name as customer2, c1.city
FROM customers as c1
JOIN customers as c2 ON c1.city = c2.city
AND c1.customer_id < c2.customer_id
ORDER BY c1.city, c1.first_name; 
  
 UPDATE products set price = 649 WHERE product_id = 1
 
SELECT orders.order_id, products.name, order_items.unit_price, products.price
FROM orders
JOIN order_items ON order_items.order_id = orders.order_id 
JOIN products ON products.product_id = order_items.product_id
WHERE order_items.unit_price <> products.price;

 


















