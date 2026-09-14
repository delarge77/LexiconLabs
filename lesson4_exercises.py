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


