from api_client import get_json
import requests
# 1
# products = get_json("https://fakestoreapi.com/products/")
# sorted_products = sorted(products, key=lambda product: product["price"], reverse=False)
# for sorted_product in sorted_products:
#     print(f"Product name: {sorted_product.get('title')} === price: {sorted_product.get('price')}")

# 2
# categories = get_json("https://fakestoreapi.com/products/categories")
# print(categories)
# category = input("Type category: ")
# while category not in categories:
#     print("Invalid category! Please choose one of the available options.")
#     category = input("Type category: ").strip()
        
# url = f"https://fakestoreapi.com/products/category/{category}"
# result = get_json(url)
# cheapest_product = min(result, key=lambda product: product["price"])
# print(len(result), cheapest_product)

# 4
# new_product = {
#     "title": "New Product",
#     "price": 19.99,
#     "description": "New description",
#     "image": "image",
#     "category": "electronics"
# }

# result = requests.post("https://fakestoreapi.com/products/", json=new_product)
# print(result.status_code)

# result = requests.patch("https://fakestoreapi.com/products/7", json={"price":99.99})
# print(result.status_code)



