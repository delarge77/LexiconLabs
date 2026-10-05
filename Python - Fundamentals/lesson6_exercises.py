# A
# 1
# squares = []
# for number in range(20):
#     squares.append(number ** 2)
# print(squares)

# squares = [number ** 2 for number in range(20)]
# print(squares)

# 2
# even_numbers = [number for number in range(101) if number % 2 == 0]
# print(even_numbers)

# 3
# names = ["  alessandro pinto  ", "MARIA NOLBERG", "  alicia valkirya", "matteo PRESLEY  "]
# formatted_names = [name.strip().title() for name in names]
# print(formatted_names)

# 4
# scores = [45, 63, 79, 85, 90, 93]
# passed_scores = [score for score in scores if score >= 70]
# print(passed_scores)

# 5
# scores = [45, 63, 79, 85, 90, 93]
# passed_scores = [(score, "PASS" if score >= 70 else "FAIL") for score in scores]
# print(passed_scores)

# 6
# Already done in that way :-P

# B
# 1
# numbers_squares = {number: number ** 2 for number in range(11)}
# print(numbers_squares)

# 2
# words = ["Alessandro", "Maria", "Alicia", "Matteo","Schummi", "Apple"]
# words_mapping = {word: len(word) for word in words}
# print(words_mapping)

# 3
# dulicates = ["Alessandro", "Maria", "Alicia", "Matteo","Schummi", "Apple", "Alessandro", "Maria", "Alicia", "Matteo","Schummi", "Apple"]
# removed_duplicates = {name.strip().lower() for name in dulicates}
# print(removed_duplicates)

# 4
# products = {
#     "laptop": 1200,
#     "mouse": 25,
#     "keyboard": 80,
#     "monitor": 300,
#     "headphones": 50
# }

# threshold = 100

# cheap_products = {
#     product: price
#     for product, price in products.items()
#     if price < threshold
# }

# print(cheap_products)

# 5
# students = [
#     {"name":"Alessandro", "score": 50},
#     {"name":"Maria", "score": 70},
#     {"name":"Alicia", "score": 90},
#     {"name":"Matteo", "score": 90},
#     {"name":"Schummi", "score": 75},
#     {"name":"Apple", "score": 70},
# ]

# students_passed = {
#     student["name"]: "PASS" if student["score"] >= 70 else "FAIL"
#     for student in students
# }

# print(students_passed)

# C
# 1
# playlist = ["A", "B", "C", "D", "E", "F"]
# enumerated_playlist = { song:index for index, song in enumerate(playlist, start= 1) }
# print(enumerated_playlist)

# 2
# tasks = ["Study Python", "Do homework", "Go shopping", "Clean the house"]
# enumarated_tasks = { f"task{index}":task for index, task in enumerate(tasks, start=1) }
# print(enumarated_tasks)

# 3
# threshold = 10
# values = [20, 30, 10, 40]
# indexes_above_threshold = [index for index, value in enumerate(values) if value > threshold ]
# print(indexes_above_threshold)

# 4
# names = ["Alessandro", "Maria", "Alicia", "Matteo"]
# for index in range(len(names)):
#     print(index, names[index])

# names = ["Alessandro", "Maria", "Alicia", "Matteo"]
# for index, name in enumerate(names):
#     print(index, name)
# enumerate() is clearer because you directly get both the index and the value 


# D
# 1
# names = ["Alessandro", "Maria", "Alicia", "Matteo"]
# scores = [70, 90, 80, 80]
# combine = {name:score for name, score in zip(names, scores)}
# print(combine)

# 2
# names = ["Alessandro", "Maria", "Alicia", "Matteo"]
# scores = [70, 90, 80, 80]
# combine = dict(zip(names, scores))
# print(combine)

# 3
# product_name = ["Apple", "Banana", "Potatoes"]
# prices = ["20.00", "34.00", "70.00"]
# stock = [True, True, False]

# products = [
#     {"name": name, "price": price, "stock": in_stock}
#     for name, price, in_stock in zip(product_name, prices, stock)
# ]

# print(products)

# 4
# product_name = ["Apple", "Banana"]
# prices = ["20.00", "34.00", "70.00"]
# combine = dict(zip(product_name, prices))
# print(combine)
# Result - {'Apple': '20.00', 'Banana': '34.00'} 

# 5
# names = ["Alessandro", "Maria", "Alicia"]
# scores = [70, 90, 80]

# for name, score in zip(names, scores):
#     print(name, score)

# 6
# a = 10
# b = 20
# a, b = b, a

# print(a, b)

# E
# 1
# words = ["apple", "cat", "banana", "dog", "elephant"]
# sorted_words = sorted(words, key=lambda word: len(word))
# print(sorted_words)

# 2
# students = [
#     {"name": "Anna", "score": 85},
#     {"name": "David", "score": 92},
#     {"name": "Sara", "score": 78},
#     {"name": "Leo", "score": 95}
# ]

# ascending = sorted(students, key=lambda student: student["score"])
# descending = sorted(students, key=lambda student: student["score"], reverse=True)

# print(ascending)
# print(descending)

# 3
# products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Mouse", "price": 25},
#     {"name": "Keyboard", "price": 80},
#     {"name": "Monitor", "price": 300}
# ]

# sorted_products = sorted(products, key=lambda product: product["price"])
# print(sorted_products)

# 4
# people = [
#     {"first_name": "John", "last_name": "Smith"},
#     {"first_name": "Anna", "last_name": "Brown"},
#     {"first_name": "David", "last_name": "Wilson"},
#     {"first_name": "Sara", "last_name": "Anderson"}
# ]

# sorted_people = sorted(people, key=lambda person: person["last_name"])
# print(sorted_people)

# 5
# students = [
#     {"name": "Anna", "score": 85},
#     {"name": "David", "score": 92},
#     {"name": "Sara", "score": 78}
# ]


# def get_score(student):
#     return student["score"]

# sorted_students = sorted(students, key=get_score)
# print(sorted_students)

# Using Lambda

# sorted_students = sorted( students, key=lambda student: student["score"])
# print(sorted_students)

# F
# 1
# products = [
#     {"name": "  Apple ", "category": "Fruit", "price": 20.00, "stock": True},
#     {"name": "BANANA", "category": " fruit ", "price": 34.50, "stock": True},
#     {"name": "  potatoes", "category": "VEGETABLE", "price": 70.00, "stock": False},
#     {"name": "ToMaTo", "category": "Vegetable ", "price": 15.99, "stock": True},
#     {"name": "  ORANGE  ", "category": " FRUIT", "price": 25.00, "stock": True},
#     {"name": "milk", "category": "DAIRY", "price": 18.50, "stock": False},
#     {"name": " CHEESE ", "category": " dairy ", "price": 45.00, "stock": True},
#     {"name": "bread", "category": "Bakery", "price": 22.00, "stock": True},
#     {"name": "  BUTTER", "category": " bakery ", "price": 32.75, "stock": False},
#     {"name": "EGGS  ", "category": "DAIRY", "price": 29.90, "stock": True},
#     {"name": "  Chicken", "category": "MEAT ", "price": 89.99, "stock": True},
#     {"name": "BEEF  ", "category": " meat", "price": 129.50, "stock": False}
# ]

# 2
# cleaned_products = [
#     {
#         **product,
#         "name": product["name"].strip().title(),
#         "category": product["category"].strip().title()
#     }
#     for product in products
# ]

# print(cleaned_products)

# 3
# in_stock_products = [
#     product
#     for product in cleaned_products
#     if product["stock"] > 0
# ]

# print(in_stock_products)

# 4
# categories = {
#     product["category"]
#     for product in cleaned_products
# }

# print(categories)

# 5
# inventory_values = {
#     product["name"]: product["price"] * product["stock"]
#     for product in cleaned_products
# }

# print(inventory_values)

# 6
# sorted_inventory = sorted(
#     inventory_values.items(),
#     key=lambda item: item[1],
#     reverse=True
# )

# print(sorted_inventory)

# 7
# for rank, (name, value) in enumerate(sorted_inventory, start=1):
#     print(f"{rank}. {name} - ${value}")

# 8
# product_names = [product["name"] for product in cleaned_products]
# stock_values = [product["stock"] for product in cleaned_products]

# for name, stock in zip(product_names, stock_values):
#     print(f"{name}: {stock} units")

# 9
# over_complicated = [
#     product["name"]
#     for product in cleaned_products
#     if product["stock"] > 0
#     if product["price"] * product["stock"] > 500
#     if product["category"] in {"Electronics", "Audio", "Mobile", "Cameras"}
# ]

# valuable_products = []

# # It is easier to read, understand, debug, and maintain.
# for product in cleaned_products:
#     if product["stock"] > 0 and product["price"] * product["stock"] > 500:
#         valuable_products.append(product["name"])

# G
# 1
# numbers = [[1, 2], [3, 4], [5, 6]]
# flattened = [number for group in numbers for number in group]
# print(flattened)

# 2
# table = [[i * j for j in range(1, 11)] for i in range(1, 11)]
# print(table)

# 3
# names = ["Anna", "David", "Sara", "Leo"]
# scores = [85, 55, 92, 78]

# passing_students = [
#     {"name": name, "score": score}
#     for name, score in zip(names, scores)
#     if score >= 60
# ]

# print(passing_students)

# 4
# scores = [78, 92, 55, 81, 67, 95, 73]

# Using loops
# has_failed = False

# for score in scores:
#     if score < 60:
#         has_failed = True
#         break

# all_passed = True

# for score in scores:
#     if score < 60:
#         all_passed = False
#         break

# print(has_failed)
# print(all_passed)

# Using any() and all():
# has_failed = any(score < 60 for score in scores)
# all_passed = all(score >= 60 for score in scores)

# print(has_failed)
# print(all_passed)

# 5

# a
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Before
# squares = []
# for number in numbers:
#     squares.append(number ** 2)

# # Pythonic
# squares = [number ** 2 for number in numbers]

# b
# names = ["Alessandro", "Maria", "Alicia", "Matteo", "Apple", "Schummi"]
# # Before
# for i in range(len(names)):
#     print(i, names[i])

# # Pythonic
# for i, name in enumerate(names):
#     print(i, name)

# c
# names = ["Alessandro", "Maria", "Alicia", "Matteo", "Apple", "Schummi"]
# scores = [1, 2, 3, 4, 5, 6] 
# # Before
# for i in range(len(names)):
#     print(names[i], scores[i])

# # Pythonic
# for name, score in zip(names, scores):
#     print(name, score)

# d
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Before
# squares = {}

# for number in numbers:
#     squares[number] = number ** 2

# # Pythonic
# squares = {number: number ** 2 for number in numbers}

# e
# scores = [1, 2, 3, 4, 5, 6]
# # Before
# found = False

# for score in scores:
#     if score >= 90:
#         found = True
#         break

# # Pythonic
# found = any(score >= 90 for score in scores)