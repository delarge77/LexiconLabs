# A

# Exercise 1 - Write a program that classifies a number as positive, negative or zero.
# number = int(input("Enter a number: "))

# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")

# Exercise 2 - Ask for an age and classify it into at least four age groups using if/elif/else.
# age = int(input("Enter your age: "))

# if age < 13:
#     print("Child")
# elif age < 18:
#     print("Teenager")
# elif age < 65:
#     print("Adult")
# else:
#     print("Senior")

# Exercise 3 - Create a login check using a stored username and password.
# Both must match.
# stored_username = "admin"
# stored_password = "python123"

# username = input("Enter your username: ")
# password = input("Enter your password: ")

# if username == stored_username and password == stored_password:
#     print("Login successful")
# else:
#     print("Invalid username or password")

# Exercise 4 - Given a score from 0-100, print a grade using at least five ranges.
# Think carefully about condition order.
# score = int(input("Enter your score: "))

# if score >= 90:
#     print("Grade A")
# elif score >= 80:
#     print("Grade B")
# elif score >= 70:
#     print("Grade C")
# elif score >= 60:
#     print("Grade D")
# else:
#     print("Grade F")

# Exercise 5 - Create a shipping rule based on order total and whether the customer is a member.
# Use and/or.
# order_total = float(input("Enter order total: "))
# member = input("Are you a member? (yes/no): ")

# if order_total >= 50 or member == "yes":
#     print("Free shipping")
# else:
#     print("Shipping fee: $5")


# Exercise 6 - Write five expressions using ==, !=, >, <, >= and <=
# and predict each boolean result before running.
# print(10 == 10)
# print(10 != 5)
# print(20 > 15)
# print(5 < 3)
# print(10 >= 10)
# print(8 <= 5)

# B
# Exercise 1 - Create examples with empty string, non-empty string, zero, non-zero integer,
# empty list and non-empty list. Test each directly in an if statement.
# empty_string = ""
# non_empty_string = "Python"
# zero = 0
# non_zero_integer = 10
# empty_list = []
# non_empty_list = ["Python", "Java"]

# if empty_string:
#     print("The string is not empty")
# else:
#     print("The string is empty")

# if non_empty_string:
#     print("The string is not empty")

# if zero:
#     print("Zero is True")
# else:
#     print("Zero is False")

# if non_zero_integer:
#     print("Non-zero integer is True")

# if empty_list:
#     print("The list is not empty")
# else:
#     print("The list is empty")

# if non_empty_list:
#     print("The list is not empty")


# Exercise 2 - Ask for a language and check whether it exists in a predefined list
# of supported languages.
# supported_languages = ["Python", "Java", "JavaScript", "Swift", "C++"]
# language = input("Enter a programming language: ")

# if language in supported_languages:
#     print("This language is supported")
# else:
#     print("This language is not supported")


# Exercise 3 - Create a list of blocked usernames and reject a supplied username
# if it appears in the list.
# blocked_usernames = ["admin", "root", "blocked_user", "spam"]
# username = input("Enter your username: ")

# if username in blocked_usernames:
#     print("Username rejected")
# else:
#     print("Username accepted")


# Exercise 4 - Use not to express at least two conditions in a readable way.
# username = input("Enter your username: ")

# if not username:
#     print("Username cannot be empty")

# password = input("Enter your password: ")

# if not password:
#     print("Password cannot be empty")

# C
# Exercise 1 - Loop over a list of names and print a numbered greeting for each.
# names = ["Alessandro", "Brett", "Andy", "Marcus"]
# number = 1

# for name in names:
#     print(f"{number}. Hello, {name}!")
#     number += 1


# Exercise 2 - Loop over numbers 1-50 and print only even numbers.
# for number in range(1, 51):
#     if number % 2 == 0:
#         print(number)


# Exercise 3 - Calculate the sum of a list manually using a loop rather than sum().
# numbers = [10, 20, 30, 40, 50]
# total = 0

# for number in numbers:
#     total += number

# print(total)


# Exercise 4 - Find the largest number in a list manually without max().
# numbers = [15, 42, 8, 73, 21]
# largest = numbers[0]

# for number in numbers:
#     if number > largest:
#         largest = number

# print(largest)


# Exercise 5 - Count how many words in a list have more than five characters.
# words = ["Python", "Java", "Programming", "Code", "Dictionary", "Loop"]
# count = 0

# for word in words:
#     if len(word) > 5:
#         count += 1

# print(count)


# Exercise 6 - Given a list of scores, count passes and failures using a threshold of 70.
# scores = [85, 62, 90, 55, 73, 68, 100]
# passes = 0
# failures = 0

# for score in scores:
#     if score >= 70:
#         passes += 1
#     else:
#         failures += 1

# print(f"Passes: {passes}")
# print(f"Failures: {failures}")


# Exercise 7 - Loop over a dictionary using keys, values and .items()
# in three separate examples.
# student = {
#     "name": "Alessandro",
#     "age": 41,
#     "city": "Gothenburg"
# }

# for key in student.keys():
#     print(key)

# for value in student.values():
#     print(value)

# for key, value in student.items():
#     print(f"{key}: {value}")

# D
# Exercise 1 - Use range to print 10 down to 1.
# for number in range(10, 0, -1):
#     print(number)


# Exercise 2 - Generate the multiplication table for a number supplied by the user.
# number = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")


# Exercise 3 - Use enumerate to print a playlist with track numbers starting at 1.
# playlist = [
#     "Back in Black",
#     "Pour Some Sugar on Me",
#     "Paradise City",
#     "Round and Round",
#     "Welcome to the Jungle"
# ]
# for number, song in enumerate(playlist, start=1):
#     print(f"{number}. {song}")


# Exercise 4 - Use nested loops to print coordinate pairs for x=1..3 and y=1..4.
# for x in range(1, 4):
#     for y in range(1, 5):
#         print(f"({x}, {y})")


# Exercise 5 - Create a simple 5x5 text grid using nested loops.
# for row in range(5):
#     for column in range(5):
#         print("*", end=" ")
#     print()

# E
# Exercise 1 - Create a countdown from 10 to 0.
# number = 10

# while number >= 0:
#     print(number)
#     number -= 1


# Exercise 2 - Ask repeatedly for a password until the correct password is entered.
# correct_password = "python123"
# password = input("Enter your password: ")

# while password != correct_password:
#     print("Incorrect password")
#     password = input("Enter your password: ")

# print("Correct password!")


# Exercise 3 - Create a menu that repeats until the user chooses 'quit'.
# The menu can simply print which option was selected.
# choice = input("Choose an option (start, help, quit): ")

# while choice != "quit":
#     print(f"You selected: {choice}")
#     choice = input("Choose an option (start, help, quit): ")

# print("Goodbye!")


# Exercise 4 - Ask the user for numbers until they enter 0.
# Keep a running total.
# total = 0
# number = int(input("Enter a number (0 to stop): "))

# while number != 0:
#     total += number
#     number = int(input("Enter a number (0 to stop): "))

# print(f"Total: {total}")


# Exercise 5 - Create a guessing loop with a fixed secret number.
# Tell the user whether each guess is too high or too low.
# secret_number = 42
# guess = int(input("Guess the number: "))

# while guess != secret_number:

#     if guess > secret_number:
#         print("Too high!")
#     else:
#         print("Too low!")

#     guess = int(input("Guess again: "))

# print("Correct! You guessed the number!")

# F
# Exercise 1 - Loop through numbers 1-100 and stop when you reach the first number
# divisible by both 7 and 9.
# for number in range(1, 101):
#     if number % 7 == 0 and number % 9 == 0:
#         print(f"First number found: {number}")
#         break


# Exercise 2 - Loop through a list of strings and skip empty strings using continue.
# words = ["Python", "", "Java", "", "Programming", "Code"]
# for word in words:
#     if not word:
#         continue

#     print(word)


# Exercise 3 - Search a list for a target name. Print 'found' and break when it appears;
# otherwise explain how you know it was not found.
# names = ["Alessandro", "Brett", "Andy", "Marcus"]
# target = input("Enter a name to search for: ")
# found = False

# for name in names:
#     if name == target:
#         print("Found")
#         found = True
#         break

# if not found:
#     print("The name was not found because the loop checked every name in the list.")


# Exercise 4 - Process a list of numeric values where negative values should be skipped
# and processing stops completely when the value 999 appears.
# numbers = [10, -5, 20, -3, 50, 999, 100, 200]

# for number in numbers:
#     if number == 999:
#         print("Processing stopped.")
#         break

#     if number < 0:
#         continue

#     print(number)

# G
# Exercise 1 - Create a list of dictionaries representing at least ten study sessions
# with subject and minutes.
# sessions = [
#     {"subject": "Python", "minutes": 45},
#     {"subject": "SQL", "minutes": 30},
#     {"subject": "Python", "minutes": 60},
#     {"subject": "Git", "minutes": 25},
#     {"subject": "Python", "minutes": 40},
#     {"subject": "SQL", "minutes": 50},
#     {"subject": "Git", "minutes": 35},
#     {"subject": "Python", "minutes": 55},
#     {"subject": "SQL", "minutes": 40},
#     {"subject": "Git", "minutes": 60}
# ]

# Exercise 2 - Loop through the sessions and calculate total minutes.
# total_minutes = 0

# for session in sessions:
#     total_minutes += session["minutes"]

# print(f"Total minutes: {total_minutes}")

# Exercise 3 - Calculate total minutes per subject using a dictionary that starts empty
# and is updated inside the loop.
# minutes_per_subject = {}

# for session in sessions:
#     subject = session["subject"]
#     minutes = session["minutes"]

#     if subject not in minutes_per_subject:
#         minutes_per_subject[subject] = 0

#     minutes_per_subject[subject] += minutes

# print(minutes_per_subject)

# Exercise 4 - Identify the longest study session without max(..., key=...).
# longest_session = sessions[0]

# for session in sessions:
#     if session["minutes"] > longest_session["minutes"]:
#         longest_session = session

# print(f"Longest session: {longest_session}")

# Exercise 5 - Print only sessions longer than 45 minutes.
# for session in sessions:
#     if session["minutes"] > 45:
#         print(f"{session['subject']}: {session['minutes']} minutes")

# Exercise 6 - Create a repeated menu that lets a user:
# view all sessions, view total time, filter by subject, or quit.
# while True:
#     print()
#     print("1. View all sessions")
#     print("2. View total time")
#     print("3. Filter by subject")
#     print("4. Quit")

#     choice = input("Choose an option: ")

#     if choice == "1":
#         for session in sessions:
#             print(f"{session['subject']}: {session['minutes']} minutes")

#     elif choice == "2":
#         print(f"Total study time: {total_minutes} minutes")

#     elif choice == "3":
#         subject = input("Enter subject: ")

#         for session in sessions:
#             if session["subject"] != subject:
#                 continue

#             print(f"{session['subject']}: {session['minutes']} minutes")

#     elif choice == "4":
#         print("Goodbye!")
#         break

#     else:
#         print("Invalid option. Please try again.")

# Exercise 7 - Use break/continue where they genuinely improve the flow.
# for session in sessions:

#     if session["minutes"] < 30:
#         continue

#     if session["minutes"] >= 60:
#         print("Found a 60-minute session!")
#         break

#     print(f"{session['subject']}: {session['minutes']} minutes")

# H
# Exercise 1 - Print FizzBuzz from 1 to 100:
# multiples of 3 -> Fizz, 5 -> Buzz, both -> FizzBuzz.
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# Exercise 2 - Given a sentence, count vowels without using .count() repeatedly.
# sentence = input("Enter a sentence: ")
# vowels = "aeiouAEIOU"
# vowel_count = 0

# for character in sentence:
#     if character in vowels:
#         vowel_count += 1

# print(f"Number of vowels: {vowel_count}")

# Exercise 3 - Find all duplicate values in a list using loops and collections.
# numbers = [1, 2, 3, 2, 4, 5, 3, 6, 1, 7]
# seen = set()
# duplicates = set()

# for number in numbers:
#     if number in seen:
#         duplicates.add(number)
#     else:
#         seen.add(number)

# print(f"Duplicates: {duplicates}")

# Exercise 4 - Build a simple text histogram:
# for each number in [3, 5, 2], print that many * characters.
# numbers = [3, 5, 2]

# for number in numbers:
#     print("*" * number)