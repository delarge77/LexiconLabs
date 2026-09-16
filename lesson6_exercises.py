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






















