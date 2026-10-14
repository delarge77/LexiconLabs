from pymongo import MongoClient
from pprint import pprint
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# for product in db.products.find({"price":{"$gt":1000}}):
#     print(product["name"], product["price"])

# for order in db.orders.find({"status":{"$ne":"delivered"}}):
#     print(order["_id"], order["status"])

# for customer in db.customers.find({"city": {"$in": ["Stockholm", "Malmö"]}}):
#     print(customer)

# for product in db.products.find({"details.color":"white"}):
#     print(product)

# for product in db.products.find({"tags":"sport"},{"name":1, "tags":1, "_id":0}):
#     print(product)