#A 
#Part 1: Variables and Data Types

# Exercise 1: Print your name, course, and subject
# print("Alesandro dos Santos Pinto")
# print("Python basics Course")
# print("Python Basics")

# Exercise 2: Create variables for name, age, height, and is_student
# name = "Alesandro"
# age = 30
# height = 1.85
# is_student = True

# print(name)
# print(type(name))
# print(age)
# print(type(age))
# print(height)
# print(type(height))
# print(is_student)
# print(type(is_student))

# Exercise 3: Change the value type of a variable to a different type and print its type 
# print(type(age))
# age = "Thirty"
# print(type(age))

# Exercise 4: Perform basic arithmetic operations with two numbers and print the results
# number1 = 10
# number2 = 5
# print(number1 + number2)
# print(number1 - number2)
# print(number1 * number2)
# print(number1 / number2)
# print(number1 // number2)
# print(number1 % number2)



# Exercise 5: Convert a string to an integer and a float, and perform arithmetic operations with them
# number_string = "10"
# number_int = int(number_string)
# print(number_int + number2)

# number_float = float(number_string)
# print(number_float + number2)
# str_number =  str(10)
# print(str_number + " is a string now")


#B
# Part 2: User Input and Output
# Exercise 1: Get user input for name and year of birth, calculate age, and print a message
# name = input("Enter your name: ")
# year_of_birth = int(input("Enter your year of birth: "))
# current_year = 2026
# age = current_year - year_of_birth
# print("Hello, " + name + "! You are " + str(age) + " years old.")

# Exercise 2: Get user input for price and discount percentage, calculate final price, and print the result
# price = float(input("Enter the price of the item: "))
# discount_percentage = float(input("Enter the discount percentage: "))
# discount_amount = price * (discount_percentage / 100)
# final_price = price - discount_amount
# print("The final price after a discount of " + str(discount_percentage) + "% is " + str(final_price))

# Exercise 3: Get user input for temperature in Celsius, convert it to Fahrenheit, and print the result
# temperature_celsius = float(input("Enter the temperature in Celsius: "))
# temperature_fahrenheit = (temperature_celsius * 9/5) + 32
# print(str(temperature_celsius) + "°C is equal to " + str(temperature_fahrenheit) + "°F.")

# Exercise 4: Get user input for the length and width of a room, calculate area and perimeter, and print the results
# room_length = float(input("Enter the length of the room in meters: "))
# room_width = float(input("Enter the width of the room in meters: "))
# room_area = room_length * room_width
# room_perimeter = 2 * (room_length + room_width)
# print("The area of the room is " + str(room_area) + " square meters.")
# print("The perimeter of the room is " + str(room_perimeter) + " meters.")


# Exercise 5: Get user input for name and year of birth, validate the input, calculate age, and print a message
# name = input("Enter your name: ")
# year_of_birth = input("Enter your year of birth: ")
# if year_of_birth.isdigit():
#     current_year = 2026
#     age = current_year - int(year_of_birth)
#     print("Hello, " + name + "! You are " + str(age) + " years old.")
# else:
#     print("Invalid input for year of birth. Please enter a valid number.")

#C
# Exercise 1: From a stored text, print its length, uppercase, lowercase, and stripped version
# text = "Mycket kompakt dimmaskin med effektivt förångningssystem Perfekt för små klubbar och barer. Denna dimmaskin är utrustad med en kraftfull pump som ger en jämn och tät dimma, vilket skapar en imponerande atmosfär på scenen eller dansgolvet. Med sin kompakta design är den lätt att transportera och installera, vilket gör den idealisk för mobila evenemang och mindre lokaler."
# print(len(text))
# print(text.upper())
# print(text.lower())
# print(text.strip())

# Exercise 2: Get user input for first name and last name, and print a greeting message using f-strings
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# print(f"Hello, {first_name} {last_name}! Welcome to the Python basics course.")

# Exercise 3: 
# str = "python programming"
# print(str[0])
# print(str[-1])
# print(str[0:7])
# print(str[0:12])
# print(str[::-1])

# Exercise 4: For first name and second name, create a username by combining parts of both names, and print the username
# first_name = input("Enter your first name: ").lower().replace(" ", "")
# second_name = input("Enter your second name: ").lower().replace(" ", "")
# username = first_name[0:3] + second_name[0:6]
# print(username)

# Exercise 5: For an email address, split it into the first part and last part, and print both parts
# email = input("Enter your email address: ")
# first_part = email.split("@")[0]
# last_part = email.split("@")[1]
# print("First part of the email: " + first_part)
# print("Last part of the email: " + last_part)

# Exercise 6: Replace a word in a string with another word, and print the modified string
# word = "We love java"
# print(word.replace("java", "python"))
# print(word)

#D

# Exercise 1: Given a string, print specific characters and slices of the string
# text = "python programming"

# print(text[0])       # p
# print(text[5])       # n
# print(text[-1])      # g
# print(text[-3])      # i
# print(text[0:6])     # python
# print(text[7:18])    # programming
# print(text[:6])      # python
# print(text[7:])      # programming
# print(text[::2])     # pto rgamn
# print(text[::-1])    # gnimmargorp nohtyp

# Exercise 2: Given a string, print specific characters and slices of the string
# str = "Artificial Intelligence"
# print(str[0])       # A
# print(str[5])       # i
# print(str[-1])      # e
# print(str[-3])      # g
# print(str[0:10])    # Artificial
# print(str[11:])     # Intelligence
# print(str[:10])     # Artificial
# print(str[11:])     # Intelligence
# print(str[::2])     # Aifi llnc
# print(str[::-1])    # ecnegilletnI laicifitrA

# Exercise 3: Given a string, print specific characters and slices of the string
# str = "Artificial Intelligence"
# print(str.split(" ")[0])  # Artificial
# print(str.split(" ")[1])  # Intelligence
# print(str.strip(" ")[0])  # Artificial
# print(str.strip(" ")[2])  # Intelligence
# print(str.replace("Artificial", "Machine"))  # Machine Intelligence

# Exercise 4: Given a string, change the first character to lowercase and print the modified string
# str = "Machine Learning"
# #str[0] = "m"  # This will raise an error because strings are immutable in Python
# str_new = "m" + str[1:]  # Correct way to change the first character
# print(str_new)  # machine Learning


#E
# Exercise 1 - Collect first name, last name, city, year of birth and favourite programming language
# name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# city = input("Enter your city: ")
# year_of_birth = int(input("Enter your year of birth: "))
# favorite_language = input("Enter your favourite programming language: ")

# Exercise 2 - Normalize text input so accidental surrounding spaces do not affect the result
# name = name.strip()
# last_name = last_name.strip()
# city = city.strip()
# favorite_language = favorite_language.strip()

# Exercise 3 - Create a generated user ID from parts of the person's name and year of birth
# user_id = name[:2].lower() + last_name[:2].lower() + str(year_of_birth)

# Exercise 4 - Print a clean multi-line summary using f-strings
# print(f"Name: {name} {last_name}, city:{city}, birth year:{year_of_birth}, favorite programming language:{favorite_language} and User Id:{user_id}")

# Exercise 5 - Print the initials, full name length excluding the space, and the favourite language reversed

# initials = name[0] + last_name[0]
# full_name_length = len(name) + len(last_name)
# reversed_language = favorite_language[::-1]

# print(f"Initials: {initials}")
# print(f"Full name length: {full_name_length}")
# print(f"Favourite language reversed: {reversed_language}")

# # Exercise 6 - Add at least three extra pieces of derived information using only concepts from Lesson 1
# city_initial = city[0]
# language_length = len(favorite_language)
# first_three_letters = favorite_language[:3]

# print(f"City initial: {city_initial}")
# print(f"Favourite language length: {language_length}")
# print(f"First three letters of favourite language: {first_three_letters}")


# F
# Exercise 1 - Create a simple seconds converter: input total seconds and calculate whole hours,
# remaining minutes and remaining seconds using // and %.

# total_seconds = int(input("Enter total seconds: "))

# hours = total_seconds // 3600
# remaining_seconds = total_seconds % 3600

# minutes = remaining_seconds // 60
# seconds = remaining_seconds % 60

# print(f"Hours: {hours}")
# print(f"Minutes: {minutes}")
# print(f"Seconds: {seconds}")


# Exercise 2 - Given a four-digit integer, extract and print each digit without converting the number
# to a string.

# number = int(input("Enter a four-digit number: "))

# thousands = number // 1000
# hundreds = (number // 100) % 10
# tens = (number // 10) % 10
# ones = number % 10

# print(thousands)
# print(hundreds)
# print(tens)
# print(ones)


# Exercise 3 - Create a text masking program that displays only the first two and last two characters
# of a supplied word, replacing the middle with * characters.

# word = input("Enter a word: ").strip()
# masked_word = word[:2] + "*" * (len(word) - 4) + word[-2:]
# print(masked_word)


# Exercise 4 - Write five short 'predict before running' examples that you could give to another
# student. Include at least one type conversion and two string slices.

# number = "12345"
# print(int(number) + 5)

# text = "Python"
# print(text[:3])

# text = "Programming"
# print(text[-4:])

# text = "Hello World"
# print(text[0:5])

# text = "Python"
# print(text[::-1])




















