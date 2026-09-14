# Part A 
# def greet():
#     print("Greetings!")

# def show_course_name():
#     print("System Developer Python and AI - Training Exercises")

# def print_separator():
#     print(" - ")

# print(greet(),print_separator(), show_course_name())
# print(show_course_name(),print_separator(), greet())
# print(print_separator(),greet(), show_course_name())

# def greet_person(name: str) -> str:
#     city = "Marstrand"
#     print(f"Hello {name} this city is:{city}")

# print(greet_person("Alessandro"))
# def add(a: int, b: int) -> int:
#     return a + b

# def subtract(a: int, b: int) -> int:
#     return a - b

# def multiply(a: int, b: int) -> int:
#     return a * b

# def devide(a: int, b: int) -> int:
#     return a // b

# print(add(2, 2))
# print(subtract(2, 2))
# print(multiply(2, 2))
# print(devide(2, 2))

# def calculate_area(width: float, height:float) -> float:
#     return width * height

# def doubleArea(witdh: float, height: float) -> float:
#     return calculate_area(witdh, height) * 2.0

# print(doubleArea(6, 3))


# def is_even(number: int) -> bool:
#     return number % 2 == 0 

# def get_larger(a: int, b:int) -> int:
#     if a > b:
#         return a
#     return b

# print(get_larger(1, 7))
# print(get_larger(4, 1))

# def classify_score(score: float) -> str:
#     if score >= 7.0:
#         return "PASS"
#     return "FAIL"

# print(classify_score(8))
# print(classify_score(6.9))
# print(classify_score(9))

# def format_name(firsName: str, lastName:str) -> str:
#     return f"First name: {firsName}, second name: {lastName}"

# print(format_name("Alessandro", "Pinto"))

# def calculate_discount(price: float, percent:int) -> float:
#     discount = price * (percent / 100)
#     return price - discount

# print(calculate_discount(235, 10))


# def greet():
#     print("Have a good day") 
#     return "Have a terrible day"

# greeting_new_customer = greet
# print(f"Greeting new customer {greeting_new_customer()}")

# def greet(name:str, greeting="Hello") -> str:
    # greeting = "Good morning"
    # return f"{greeting} {name}"

# print(greet("Alessandro"))

# def calculate_price(price:float, quantity=1, discount=0) -> float:
#     """Calculate total price with disccount over total value"""
#     percent = price * (discount / 100)
#     return price * quantity - percent


# print(calculate_price(300))
# print(calculate_price(300, 1, 10))
# print(calculate_price(300, 2, 10))


# def create_profile(name:str, city= "unknown", active= True) -> dict:
#     return {
#         "name": name,
#         "city": city,
#         "active": active
#     }

# print(create_profile("Alessandro"))
# print(create_profile("Alessandro", "Marstrand"))
# print(create_profile("Alessandro", "Göteborg", False))


# print(create_profile("Stockholm", True, "Alessandro"))

# def calculate_total(numbers) -> int:
#     total = 0
#     for number in numbers:
#         total = total + number
#     return total

# print(calculate_total([1,2,3,4]))

# def count_even(numbers) -> int:
#     total = 0
#     for number in numbers:
#         if number % 2 == 0:
#             total = total + 1 
#     return total

# print(count_even([1,2,3,4]))

# def create_long_words(words, minimumLength:int) -> list:
#     new_list = []
#     for word in words:
#         if len(word) > minimumLength:
#             new_list.append(word)

#     return new_list

# print(create_long_words(["Elephant", "Maria", "Cat", "Alessandro"], 5))

# def find_students(students, name):
#     for student in students:
#         if student["name"] == name:
#             return student
        
#     return "NONE"

# print(find_students([{"name":"Alessandro"}, 
#                      {"name":"Maria"}, 
#                      {"name":"Alicia"}, 
#                      {"name":"Matteo"}, 
#                      {"name":"Apple"}, 
#                      {"name":"Schummi"}], "Apple"))


# def average_score(students) -> int:
#     total_score = 0 
#     for student in students:
#         total_score = total_score + student["score"]

#     return total_score / len(students)

# print(average_score([{"name":"Alessandro", "score":80}, 
#                      {"name":"Maria", "score":89},
#                      {"name":"Alicia", "score":100},
#                      {"name":"Matteo", "score":100},
#                      {"name":"Schummi", "score":100},
#                      {"name":"Apple", "score":100}]))


# def get_active_users(users:list) -> list:
#     active_users = []
#     for user in users:
#         if user["active"] == True:
#             active_users.append(user)
#     return active_users

# print(get_active_users([{"Name": "Alessandro", "active":False},
#                         {"Name": "Maria", "active":True},
#                         {"Name": "Alicia", "active":True},
#                         {"Name": "Matteo", "active":True},
#                         {"Name": "Apple", "active":True},
#                         {"Name": "Schummi", "active":True}]))

# def celsius_to_fahrenheit(celsius):
#     return celsius * 9 / 5 + 32

# def classify_temperature(celsius):
#     if celsius < 10:
#         return "cold"
#     elif celsius < 25:
#         return "warm"
#     else:
#         return "hot"

# def format_report(celsius):
#     fahrenheit = celsius_to_fahrenheit(celsius)
#     category = classify_temperature(celsius)

#     return f"{celsius}°C = {fahrenheit}°F ({category})"

# print(format_report(20))


# def calculate_subtotal(prices):
#     total = 0

#     for price in prices:
#         total += price

#     return total


# def calculate_discount(subtotal, percent):
#     return subtotal * (percent / 100)


# def calculate_final_total(subtotal, discount):
#     return subtotal - discount


# prices = [100, 50, 25]
# discount_percent = 10

# subtotal = calculate_subtotal(prices)
# discount = calculate_discount(subtotal, discount_percent)
# final_total = calculate_final_total(subtotal, discount)

# print("Subtotal:", subtotal)
# print("Discount:", discount)
# print("Final total:", final_total)






# Part F - Applied challenge: Event registration processor 
 
# 1. Create functions to normalize a participant name, validate an age range using boolean return values, calculate a registration fee based on age/student status, and create a participant dictionary. 
# 2. Create at least eight participant dictionaries using your functions. 
# 3. Write a function that receives the participant list and returns the total expected registration revenue. 
# 4. Write a function that returns only student participants. 
# 5. Write a function that returns the oldest participant. 
# 6. Write a function that creates a readable summary string for one participant. 
# 7. Keep input/output responsibilities separate from calculation functions as much as possible.








