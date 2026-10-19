import requests 

def get_json(url, params=None, headers=None, timeout=5):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("The requesst took too long")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the server")
    except requests.exceptions.HTTPError as error:
        print(f"The server said no: {error.response.status_code}")
    except requests.exceptions.JSONDecodeError:
        print("The answer was not JSON")
    except requests.exceptions.RequestException as error:
        print(f"Someting else went wrong: {type(error).__name__}")
    return None

# 1
# products = get_json("https://fakestoreapi.com/products/")
# sorted_products = sorted(products, key=lambda product: product["price"], reverse=False)
# for sorted_product in sorted_products:
#     print(f"Product name: {sorted_product.get("title")} === price: {sorted_product.get("price")}")

# 2
categories = get_json("https://fakestoreapi.com/products/categories")
print(categories)
category = input("Type category: ")
while category not in categories:
    print("Invalid category! Please choose one of the available options.")
    category = input("Type category: ").strip()
        
url = f"https://fakestoreapi.com/products/category/{category}"
result = get_json(url)
cheapest_product = min(result, key=lambda product: product["price"])
print(len(result), cheapest_product)