-- LAB 1 Questions : 

SELECT first_name, email FROM CUSTOMERS;
SELECT * from PRODUCTS WHERE category = "Shoes";
SELECT * from CUSTOMERS WHERE city = "Uppsala";
SELECT * from products where price = 199;
SELECT * FROM products ORDER By name;
SELECT * FROM CUSTOMERS ORDER By joined_date;
SELECT * FROM products WHERE stock = 0;
SELECT * FROM customers  ORDER BY joined_date  DESC  LIMIT 3;
SELECT * FROM customers WHERE city IN ("Stockholm", "Göteborg");
SELECT name AS product , price AS price_sek FROM products;

-- Bonus questions 
SELECT * FROM products WHERE category in ("Clothing","Shoes") AND price > 1000;
SELECT name, price, stock ,  (price * stock)  AS stock_value FROM products WHERE stock > 0  ORDER By stock_value DESC;
SELECT * FROM CUSTOMERS WHERE first_name LIKE "____";
SELECT * FROM products ORDER By price ASC  LIMIT 5 OFFSET 5;
SELECT * from customers WHERE joined_date < "2025" AND city <>  "Uppsala" ORDER By city, last_name;

-- Extra Challenges
-- Level 1
SELECT * FROM products WHERE category <> "Accessories" AND stock > 0 AND name LIKE "% %" ORDER By category, price DESC ;  
SELECT * FROM customers  WHERE city LIKE "S%" OR city LIKE "M%" OR city ISNULL;
SELECT * FROM PRODUCTS WHERE category = "Shoes" ORDER by price DESC LIMIT 1 OFFSET 1;
SELECT * FROM customers WHERE joined_date > '2024-01-01' AND joined_date < '2026-01-01' ORDER BY joined_date DESC LIMIT 3;

-- Level2
SELECT first_name || ' ' || last_name  as "full_name" FROM customers ORDER By last_name ;
SELECT *,
       CASE 
	          WHEN price < 200 THEN 'Budget' 
	          WHEN price > 200 AND price < 799 THEN 'Mid' 
			  ELSE 'Premium'
		END AS price_level	  
FROM products ORDER By price_level;
SELECT first_name, COALESCE(city, "unknown") as city FROM customers;
SELECT * FROM customers WHERE strftime('%m', joined_date) <= '06';
SELECT name, LENGTH(name) AS name_length FROM products ORDER BY LENGTH(name) DESC LIMIT 1;
SELECT email, substr(email, 1, instr(email, '@') - 1) AS username FROM customers;

-- Level 3
