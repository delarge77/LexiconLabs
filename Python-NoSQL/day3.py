from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 3
# db.create_collection("newsletter_signups", validator={"$jsonSchema": {
# "required": ["email"],
# "properties": {
# "email": {"bsonType": "string"},
# "source": {"bsonType": "string", "enum": ["web", "store"]}}}})

# db.newsletter_signups.insert_one({"email":"alessandro.pinto@hotmail.com", "source":"web"})
# print(db.newsletter_signups.count_documents({}))
# for newsletter_signup in db.newsletter_signups.find({}):
#     print(newsletter_signup["email"], newsletter_signup["source"])

# db.newsletter_signups.insert_one({"email":"alessandro@pinto.com", "source":"Instagram"})
# db.newsletter_signups.insert_one({"email":1, "source":"web"})

# 4
# for customerInCity in db.customers.aggregate([{"$group": 
#                                                {"_id": "$city",
#                                                 "count": {"$sum": 1}}},
#                                                 {"$sort": {"count": -1}},
#                                                 {"$project": {"city": "$_id","count": 1, "_id": 0}}]):
#     print(customerInCity)

# 5
# for product in db.products.aggregate([{"$group":
#                                        {"_id":"$category", 
#                                         "cheapest": {"$min": "$price"}, 
#                                         "most_expensive": {"$max": "$price"}}}]):

#     print(product)
    

