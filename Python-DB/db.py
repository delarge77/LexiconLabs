import sqlite3

conn = sqlite3.connect("webshop.db")
cursor = conn.cursor()

# cursor.execute("SELECT first_name, last_name, city FROM customers")
# for first_name, last_name, city in cursor.fetchall():
#     print(f"{first_name:<10} {last_name:<20} {city}")

# max_price = float(input("Type max price: "))
# cursor.execute("SELECT name, price FROM PRODUCTS WHERE price <= ?", (max_price,))
# for name, price in cursor.fetchall():
#     print(f"{name:<20} {price:>8.2f} kr")

# category = input("Type category: ")
# cursor.execute("SELECT COUNT (*) FROM products WHERE category= ?", (category,))
# quantity = cursor.fetchone()[0]
# print(f"The numbers of products in category {category} are {quantity}")














