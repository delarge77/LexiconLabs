#A
# Exercise 1 - Create a list of at least eight programming languages.
# Access the first, last, third and second-to-last values.
# programming_languages = ["Python", "Java", "C++", "JavaScript", "Swift", "Kotlin", "C#", "Ruby"]
# print(programming_languages[0])
# print(programming_languages[-1])
# print(programming_languages[2])
# print(programming_languages[-2])

# Exercise 2 - Print three different slices of the list, then print the list
# in reverse order using slicing.
# print(programming_languages[0:3])
# print(programming_languages[2:5])
# print(programming_languages[5:])
# print(programming_languages[::-1])

# Exercise 3 - Use append, insert, remove and pop.
# After each operation, print the list so the change is visible.
# programming_languages.append("Go")
# print(programming_languages)
# programming_languages.insert(1, "PHP")
# print(programming_languages)
# programming_languages.remove("Java")
# print(programming_languages)
# programming_languages.pop()
# print(programming_languages)

# Exercise 4 - Create a numeric list. Calculate its length, minimum,
# maximum and sum using built-in functions.
# numbers = [10, 25, 5, 40, 15, 30]
# print(len(numbers))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# Exercise 5 - Sort one list ascending and another descending.
# .sort() changes the original list, while sorted() creates a new sorted list.
# numbers_ascending = [8, 3, 10, 1, 6]
# numbers_ascending.sort()
# print(numbers_ascending)
# numbers_descending = [8, 3, 10, 1, 6]
# numbers_descending.sort(reverse=True)
# print(numbers_descending)
# numbers = [8, 3, 10, 1, 6]
# sorted_numbers = sorted(numbers)
# print(numbers)
# print(sorted_numbers)

# Exercise 6 - Demonstrate the reference/copy issue using list_b = list_a.
# Then fix it with .copy().
# list_a = ["Python", "Java", "Swift"]
# list_b = list_a
# list_b.append("C++")
# print(list_a)
# print(list_b)

# Fix the reference/copy issue using .copy()
# list_a = ["Python", "Java", "Swift"]
# list_b = list_a.copy()
# list_b.append("C++")
# print(list_a)
# print(list_b)

# B
# Exercise 1 - Create a tuple representing RGB values.
# Unpack it into three variables and print them.
# rgb = (255, 128, 0)
# red, green, blue = rgb
# print(red)
# print(green)
# print(blue)

# Exercise 2 - Create a tuple containing a person's name, age and city.
# Unpack and use the values in a formatted sentence.
# person = ("Alessandro", 41, "Gothenburg")
# name, age, city = person
# print(f"{name} is {age} years old and lives in {city}.")

# Exercise 3 - Attempt to reason about changing one tuple element.
# Explain in a comment why tuples are useful when values should not be changed.
# rgb = (255, 128, 0)
# Tuples cannot be changed after they are created.
# This makes them useful when values should stay fixed.
# rgb[0] = 100

# Exercise 4 - Create a list containing at least four coordinate tuples such as (10, 20).
# Access individual x and y values.
# coordinates = [
#     (10, 20),
#     (30, 40),
#     (50, 60),
#     (70, 80)
# ]
# x, y = coordinates[0]
# print(f"x = {x}")
# print(f"y = {y}")

# C 
# Exercise 1 - Create a list containing duplicate course names.
# Convert it to a set and compare the lengths before and after.
# courses = ["Python", "Java", "Python", "JavaScript", "Python", "C++", "JavaScript"]
# print(len(courses))
# course_set = set(courses)
# print(len(course_set))

# Exercise 2 - Create two sets representing skills of two developers.
# Find skills they share, skills only the first has, and all skills represented by either person.
# developer1 = { "Python", "Git", "SQL", "Docker", "JavaScript"}
# developer2 = { "Python", "Git", "Java", "Docker"}
# shared_skills = developer1.intersection(developer2)
# only_first = developer1.difference(developer2)
# all_skills = developer1.union(developer2)
# print(f"Shared skills: {shared_skills}")
# print(f"Only developer 1 has: {only_first}")
# print(f"All skills: {all_skills}")

# Exercise 3 - Create a set and practice add, remove/discard and membership testing.
# skills = {"Python", "Git", "SQL"}
# skills.add("Docker")
# print(skills)
# skills.remove("SQL")
# print(skills)
# skills.discard("Java")
# print(skills)
# print("Python" in skills)
# print("Java" in skills)

# Exercise 4 - Explain in comments why a set is a better choice than a list
# for one real-world uniqueness problem.

# A set is a better choice for storing unique email addresses
# because a set automatically removes duplicate values.
# A list can contain the same email address multiple times,
# while a set keeps only one occurrence of each email address.
# email_addresses = ["john@example.com", "alex@example.com", "maria@example.com"]
# unique_email_addresses = set(email_addresses)
# print(unique_email_addresses)


# D
# Exercise 1 - Create a dictionary for a laptop with brand, model, RAM, storage and price.
# Read every value by key.
# laptop = {"brand": "Apple", "model": "MacBook Pro", "RAM": "16GB", "storage": "512GB", "price": 1999}
# print(laptop["brand"])
# print(laptop["model"])
# print(laptop["RAM"])
# print(laptop["storage"])
# print(laptop["price"])

# Exercise 2 - Update the price, add an operating_system key and remove one key.
# laptop["price"] = 1799
# laptop["operating_system"] = "macOS"
# laptop.pop("storage")
# print(laptop)

# Exercise 3 - Use get() for both an existing and a missing key.
# Compare it conceptually with direct indexing.
# print(laptop.get("brand"))
# print(laptop.get("storage"))

# Direct indexing gives an error if the key does not exist.
# get() returns None if the key does not exist.
# Exercise 4 - Print keys, values and items separately.
# print(laptop.keys())
# print(laptop.values())
# print(laptop.items())

# Exercise 5 - Create a dictionary mapping five course names to number of study hours.
# Calculate the total hours using the dictionary values.
# courses = {"Python": 40, "SQL": 30, "Git": 20, "JavaScript": 35, "AI": 25}
# total_hours = sum(courses.values())
# print(f"Total study hours: {total_hours}")

# E
# Exercise 1 - Create a list of at least five dictionaries representing books
# with title, author, pages and available.
# books = [
#     {
#         "title": "The Hobbit",
#         "author": "J.R.R. Tolkien",
#         "pages": 310,
#         "available": True
#     },
#     {
#         "title": "1984",
#         "author": "George Orwell",
#         "pages": 328,
#         "available": False
#     },
#     {
#         "title": "Dune",
#         "author": "Frank Herbert",
#         "pages": 412,
#         "available": True
#     },
#     {
#         "title": "The Shining",
#         "author": "Stephen King",
#         "pages": 447,
#         "available": True
#     },
#     {
#         "title": "Dracula",
#         "author": "Bram Stoker",
#         "pages": 336,
#         "available": False
#     }
# ]

# Exercise 2 - Access the title of the third book and the availability
# of the last book.
# print(books[2]["title"])
# print(books[-1]["available"])

# Exercise 3 - Change one nested value and add a new key to one book.
# books[0]["pages"] = 320
# books[0]["genre"] = "Fantasy"
# print(books[0])

# Exercise 4 - Create a dictionary where each key is a department
# and each value is a list of employee names.
# employees = {
#     "IT": ["Alessandro", "John", "Maria"],
#     "Marketing": ["Peter", "Anna"],
#     "Sales": ["David", "Lisa", "Mark"],
#     "HR": ["Sarah", "James"]
# }
# print(employees)

# Exercise 5 - Create a structure for three courses where each course
# contains a name, teacher and list of topics.
# Print one specific topic using chained indexing.
# courses = [
#     {
#         "name": "Python",
#         "teacher": "John",
#         "topics": ["Variables", "Lists", "Dictionaries"]
#     },
#     {
#         "name": "SQL",
#         "teacher": "Anna",
#         "topics": ["SELECT", "WHERE", "JOIN"]
#     },
#     {
#         "name": "Git",
#         "teacher": "Peter",
#         "topics": ["Commit", "Branch", "Merge"]
#     }
# ]
# print(courses[0]["topics"][1])

# F
# Exercise 1 - Create a catalogue containing at least eight movies, games or books.
# Each item must be a dictionary with at least four useful fields.
# catalogue = [
#     {
#         "title": "The Matrix",
#         "type": "Movie",
#         "year": 1999,
#         "genre": "Sci-Fi",
#         "rating": 8.7
#     },
#     {
#         "title": "Back to the Future",
#         "type": "Movie",
#         "year": 1985,
#         "genre": "Sci-Fi",
#         "rating": 8.5
#     },
#     {
#         "title": "Die Hard",
#         "type": "Movie",
#         "year": 1988,
#         "genre": "Action",
#         "rating": 8.2
#     },
#     {
#         "title": "The Hobbit",
#         "type": "Book",
#         "year": 1937,
#         "genre": "Fantasy",
#         "rating": 4.3
#     },
#     {
#         "title": "Dune",
#         "type": "Book",
#         "year": 1965,
#         "genre": "Sci-Fi",
#         "rating": 4.6
#     },
#     {
#         "title": "The Witcher 3",
#         "type": "Game",
#         "year": 2015,
#         "genre": "RPG",
#         "rating": 9.5
#     },
#     {
#         "title": "Doom",
#         "type": "Game",
#         "year": 1993,
#         "genre": "Action",
#         "rating": 9.0
#     },
#     {
#         "title": "The Shining",
#         "type": "Book",
#         "year": 1977,
#         "genre": "Horror",
#         "rating": 4.4
#     }
# ]


# Exercise 2 - Store all item dictionaries in one list.
# All the dictionaries are already stored in the catalogue list above.
# print(catalogue)


# Exercise 3 - Create a set containing all unique categories/genres represented in the catalogue.
# genres = {"Sci-Fi", "Action", "Fantasy", "RPG", "Horror"}
# print(genres)

# Exercise 4 - Create a tuple for each item's immutable identifier plus release year,
# and include or associate it sensibly in your design.
# matrix_id = ("MOV001", 1999)
# back_to_future_id = ("MOV002", 1985)
# die_hard_id = ("MOV003", 1988)
# hobbit_id = ("BOOK001", 1937)
# dune_id = ("BOOK002", 1965)
# witcher_id = ("GAME001", 2015)
# doom_id = ("GAME002", 1993)
# shining_id = ("BOOK003", 1977)
# print(matrix_id)
# print(back_to_future_id)


# Exercise 5 - Perform at least ten manual retrieval/update operations that demonstrate
# nested indexing, membership and collection methods.
# print(catalogue[0]["title"])
# print(catalogue[1]["year"])
# print(catalogue[2]["genre"])
# print(catalogue[-1]["title"])

# catalogue[0]["rating"] = 9.0
# print(catalogue[0]["rating"])
# print("Sci-Fi" in genres)
# print("Comedy" in genres)

# genres.add("Comedy")
# print(genres)

# genres.remove("Comedy")
# print(genres)
# print(len(catalogue))

# Exercise 6 - Print a clean summary of the catalogue without using loops yet.
# Repetition is acceptable here because loops come next lesson.
# print(f"Title: {catalogue[0]['title']}, Type: {catalogue[0]['type']}, Year: {catalogue[0]['year']}, Genre: {catalogue[0]['genre']}")
# print(f"Title: {catalogue[1]['title']}, Type: {catalogue[1]['type']}, Year: {catalogue[1]['year']}, Genre: {catalogue[1]['genre']}")
# print(f"Title: {catalogue[2]['title']}, Type: {catalogue[2]['type']}, Year: {catalogue[2]['year']}, Genre: {catalogue[2]['genre']}")
# print(f"Title: {catalogue[3]['title']}, Type: {catalogue[3]['type']}, Year: {catalogue[3]['year']}, Genre: {catalogue[3]['genre']}")
# print(f"Title: {catalogue[4]['title']}, Type: {catalogue[4]['type']}, Year: {catalogue[4]['year']}, Genre: {catalogue[4]['genre']}")
# print(f"Title: {catalogue[5]['title']}, Type: {catalogue[5]['type']}, Year: {catalogue[5]['year']}, Genre: {catalogue[5]['genre']}")
# print(f"Title: {catalogue[6]['title']}, Type: {catalogue[6]['type']}, Year: {catalogue[6]['year']}, Genre: {catalogue[6]['genre']}")
# print(f"Title: {catalogue[7]['title']}, Type: {catalogue[7]['type']}, Year: {catalogue[7]['year']}, Genre: {catalogue[7]['genre']}")

# G
# Exercise 1 - Given two lists of usernames, determine duplicates and unique usernames using sets.
# usernames_1 = ["alex", "john", "maria", "peter", "lisa"]
# usernames_2 = ["john", "maria", "david", "anna", "lisa"]

# set_1 = set(usernames_1)
# set_2 = set(usernames_2)

# duplicates = set_1.intersection(set_2)
# unique_usernames = set_1.union(set_2)
# only_first = set_1.difference(set_2)
# only_second = set_2.difference(set_1)

# print(f"Duplicates: {duplicates}")
# print(f"All unique usernames: {unique_usernames}")
# print(f"Only in first list: {only_first}")
# print(f"Only in second list: {only_second}")


# Exercise 2 - Design a nested collection for a small online course platform:
# courses, teacher, students and topics. Do not write classes.
# courses = {
#     "Python": {
#         "teacher": "John",
#         "students": ["Alex", "Maria", "Peter"],
#         "topics": ["Variables", "Lists", "Dictionaries"]
#     },
#     "SQL": {
#         "teacher": "Anna",
#         "students": ["John", "Lisa", "David"],
#         "topics": ["SELECT", "WHERE", "JOIN"]
#     },
#     "Git": {
#         "teacher": "Peter",
#         "students": ["Alex", "Anna", "Maria"],
#         "topics": ["Commit", "Branch", "Merge"]
#     }
# }

# print(courses["Python"]["teacher"])
# print(courses["Python"]["students"])
# print(courses["Python"]["topics"])


# Exercise 3 - Create a dictionary-based inventory for five products.
# Update stock values manually and calculate total units using values.
# inventory = { "Laptop": 10, "Keyboard": 25, "Mouse": 30, "Monitor": 15, "Headphones": 20}
# inventory["Laptop"] = 8
# inventory["Mouse"] = 27
# total_units = sum(inventory.values())
# print(inventory)
# print(f"Total units: {total_units}")


# Exercise 4 - Write a short comparison in comments: list vs tuple vs set vs dictionary.
# Give one situation where each is the best fit.

# List:
# A list is ordered and can contain duplicate values.
# Best fit: storing a list of songs in a playlist.

# Tuple:
# A tuple is ordered and cannot be changed after creation.
# Best fit: storing fixed coordinates such as (10, 20).

# Set:
# A set stores unique values and is useful for membership testing.
# Best fit: storing unique usernames.

# Dictionary:
# A dictionary stores key-value pairs.
# Best fit: storing information about a product using keys such as name, price and stock.