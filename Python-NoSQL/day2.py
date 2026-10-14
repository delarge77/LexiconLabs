from pymongo import MongoClient
from pprint import pprint
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 1
# for product in db.products.find({"price":{"$gt":1000}}):
#     print(product["name"], product["price"])

# 2
# for order in db.orders.find({"status":{"$ne":"delivered"}}):
#     print(order["_id"], order["status"])

# 3
# for customer in db.customers.find({"city": {"$in": ["Stockholm", "Malmö"]}}):
#     print(customer)

# 4
# for product in db.products.find({"details.color":"white"}):
#     print(product)

# 5
# for product in db.products.find({"tags":"sport"},{"name":1, "tags":1, "_id":0}):
#     print(product)

# 6
# for product in db.products.find({}, {"_id":0,"name":1,"price":1}).sort("price", 1).limit(5):
#     print(product)

# 7
# for order in db.orders.find({"items.product_id":2}):
#     print(order)

# 8
# for product in db.products.find({"category":"Accessories"}):
#     print(product)

# db.products.update_many({"category":"Accessories"},{"$inc": {"price":+20}})

# for product in db.products.find({"category":"Accessories"}):
#     print(product)

# 9
# for product in db.products.find({"name":"Rain Jacket"}):
#     print(product)

# db.products.update_one({"name":"Rain Jacket"},{"$addToSet":{"tags":"new"}})
# db.products.update_one({"name":"Rain Jacket"},{"$set":{"restock_date":datetime.now()}})

# for product in db.products.find({"name":"Rain Jacket"}):
#     print(product)

# 10
# for order in db.orders.find({"status":"new", "order_date":{"$lt":datetime(2026, 3, 20)}}):
#     print(order)
# print(db.orders.count_documents({}))

# db.orders.delete_many({"status":"new", "order_date":{"$lt":datetime(2026, 3, 20)}})
# print(db.orders.count_documents({}))





    