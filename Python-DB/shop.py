import sqlite3
 
 
def connect():
    conn = sqlite3.connect("webshop.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn
 
 
def list_products(conn):
    cursor = conn.execute("SELECT product_id, name, price, stock FROM products")
    for pid, name, price, stock in cursor.fetchall():
        print(f"{pid:>3}  {name:<20} {price:>8.2f} kr  ({stock} in stock)")
 
 
def search_customers(conn):
    city = input("City: ")
    cursor = conn.execute(
        "SELECT first_name, last_name FROM customers WHERE city = ?", (city,))
    rows = cursor.fetchall()
    if not rows:
        print("No customers found.")
    for first, last in rows:
        print(first, last)
 
 
def add_product(conn):
    name = input("Name: ")
    category = input("Category: ")

    while True:
        try:
            price = float(input("Price: "))
            break
        except ValueError:
            print("Please enter a valid number")

    stock = int(input("Stock: "))
    conn.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock))
    conn.commit()
    print("Saved!")

def update_stock(conn):
    product_id = input("Type product Id: ")
    stock = input("Add new quantity for stock: ")
    cursor = conn.execute("UPDATE products SET stock = ? WHERE product_id = ?",(stock,product_id,))
    conn.commit()
    print("Saved!")

def show_order(conn):
    order_id = input("Type the order Id: ")
    cursor = conn.execute("SELECT products.name, order_items.quantity " \
    "FROM order_items " \
    "JOIN products ON products.product_id = order_items.product_id " \
    "WHERE order_items.order_id = ?", (order_id,))
    # Need a better way to show data :-P 
    for name, quantity in cursor.fetchall():
        print(f"Product: {name:<20} quantity: {quantity}")

def best_selling(conn):
    
    print("Best selling products")
 
 
def main():
    conn = connect()
    while True:
        print("\n1) List products  2) Search customers  3) Add product  4) Update Stock  5)Show recepit  6)Best selling products  0) Quit")
        choice = input("> ")
        if choice == "1":
            list_products(conn)
        elif choice == "2":
            search_customers(conn)
        elif choice == "3":
            add_product(conn)
        elif choice == "4":
            update_stock(conn)
        elif choice == "5":
            show_order(conn)
        elif choice == "6":
             best_selling(conn)
        elif choice == "0":
            break
    conn.close()
 
 
main()