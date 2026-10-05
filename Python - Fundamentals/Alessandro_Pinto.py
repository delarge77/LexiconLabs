# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}
]

# 1. Loop through the products.
# 2. Print the name of every product that is in stock.
# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
# 4. Print the total value.
# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.


# Write your solution below:
# 1. Loop through the products.
for product in products:
    print(product)

# 2. Print the name of every product that is in stock.
for product in products:
    print(product["name"])

# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
total_value_in_stock = 0
for product in products:
    total_value_per_product = product["price"] * product["stock"]
    print(total_value_per_product)
    total_value_in_stock = total_value_in_stock + total_value_per_product

# 4. Print the total value.
print("Total value in stock:", total_value_in_stock)

# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.
highest_price = 0
for product in products:
    if product["price"] > highest_price:
        highest_price = product["price"]
        print(product["name"])

# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score
#
# Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"
#
# Call create_result() using the scores above.
# Print both the average score and the final result.


# Write your solution below:
def calculate_average(scores):
    total = 0 
    for score in scores:
        total = total + score
    print("Total value", total / len(scores))
    return total / len(scores)

# # print(calculate_average(scores))
def create_result(scores):
    average = calculate_average(scores)
    if average >= 70:
        print("PASS")
        return "PASS"
    else:
        print("FAIL")
        return "FAIL"

create_result(scores)

# ==================================================
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter
# - receives any number of product prices using *args
# - receives optional settings using **kwargs
# - calculates the subtotal of all product prices
# - applies the discount percentage if "discount" exists
# - adds shipping if "shipping" exists
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.
# Write your solution below:

def calculate_order(customer_name, *product_prices, **settings):
    total_product_price = 0
    result = {"customer":customer_name}
    for product_price in product_prices:
        total_product_price = total_product_price + product_price 
    result["subtotal"] = total_product_price

    final_total = total_product_price

    if "discount" in settings:
        discount = settings["discount"]
        final_total = final_total - (final_total * discount / 100)
    if "shipping" in settings:
        shipping = settings["shipping"]
        final_total = final_total + shipping

    result["final_total"] = final_total
    result["settings"] = settings

    return result


result = calculate_order("Ana", *product_prices, **order_settings)
print(result)

# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.

# Write your solution below:
normalized_players_name = [player["name"].strip().title() for player in players]
print(normalized_players_name)

new_users = [player for player in players if player["score"]> 80 and player["active"] == True]
print(new_users)

sorted_players = sorted(players, key=lambda player: player["score"], reverse=True)
print(sorted_players)

def ranking(*players):
    for index, player in enumerate(players, start=1):
        print(f"{index}. {player['name'].strip().title()} - {player['score']}")

ranking(*sorted_players)

normalized_players = [
    {**player, "name": player["name"].strip().title()}
    for player in players
]

names = [player["name"] for player in normalized_players]
scores = [player["score"] for player in players]

for name, score in zip(names, scores):
    print(name, score)
