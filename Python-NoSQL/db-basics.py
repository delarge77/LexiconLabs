from pymongo import MongoClient
from bson import ObjectId
from pprint import pprint

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# SELECT * FROM products
# for product in db.products.find():
#     print(product)

# SELECT * FROM products WHERE category = Accessories
# for accessorie in db.products.find({"category": "Accessories"}):
#     print(accessorie)

# SELECT * FROM customers WHERE city = Göteborg
# for customer in db.customers.find({"city":"Göteborg"}):
#     print(customer["first_name"], customer["last_name"])

# SELECT name, price FROM products
# for product in db.products.find():
#     print(product["name"], product["price"])

# SELECT COUNT(*) FROM customers WHERE city = Uppsala
# print(db.customers.count_documents({"city":"Uppsala"}))

# SELECT stock FROM products WHERE name = Sandals
# print(db.products.find_one({"name":"Sandals"},["stock"]))

# SELECT name FROM customers WHERE newsletter = True
# for customer in db.customers.find({"newsletter": True}):
#     print(customer["first_name"])

# result = db.customers.insert_one(
#     {
#         "first_name":"Alessandro", "last_name":"Pinto", 
#         "email":"alessandro@pinto.com", 
#         "city":"Kungälv", 
#         "joined":"2026-10-13", 
#         "newsletter":True
#      }
# )
# print(result.inserted_id)
# customer = db.customers.find_one({"email": "alessandro@pinto.com"})
# pprint(customer)

# result = db.products.insert_many([
#     {"_id":13, "name": "Scarf", "category": "Accessories", "price":299, 
#      "stock":15, "tags":["winter"], "details": {"color": "red"}},
#     {"_id":14, "name": "Gloves", "category": "Accessories", "price":199,
#      "stock":20, "tags":["winter"], "details": {"color": "black"}}
# ])
# print(db.products.count_documents({}))

# for customer in db.customers.find():
#     print(customer["first_name"], customer["last_name"], customer.get("city", "Unknown city"))

# for order in db.orders.find():
#     print(f"Order {order['_id']}: {len(order['items'])} items")

# for i in db.customers.find({"$or": [{"city": "Uppsala"}, {"newsletter": True}]}):
#     pprint(i)
