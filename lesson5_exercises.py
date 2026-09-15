# A
# 1
# course_name = "Good morning" 

# def greet():
#     course_name = "Good night"
#     print(course_name) # print the local created variable 


# greet()
# print(course_name) # prints the global variable

# 2
# def localCounter():
#     counter = 0

# counter

# 3
# Wrong way to do it 
# number_of_students = 0
# def increaseStudentsNumber():
#     number_of_students = number_of_students + 1 # There is no reference to number_of_students here

# print(number_of_students) 
# # Right way to do it
# number_of_students = 0
# def increaseStudentsNumber(studants):
#     return studants + 1 # There is no reference to number_of_students here
# number_of_students = increaseStudentsNumber(number_of_students)
# print(number_of_students)

# 4
# def nestedFunctionsOne():
#     startDay = "Monday"
#     def nestedFunctionTwo():
#         print(startDay)
#     nestedFunctionTwo()

# nestedFunctionsOne()

# 5
# # Bad
# list = [1, 2, 3]
# str = "Hello"
# sum = 10
# max = 100

# # Good
# numbers = [1, 2, 3]
# text = "Hello"
# total = 10
# maximum = 100

# B
# 1
# def add_all(*arg):
#     total = 0
#     for number in arg:
#         total = total + number
#     return total

# total = add_all(1, 2, 3, 4, 5)
# print(total) 

# 2
# def average(*arg):
#     total = 0
#     if len(arg) == 0:
#         return 0
#     else:
#         for number in arg:
#             total = total + number
#         return total // len(arg)


# average = average(1, 2, 3, 4, 5)
# print(average)

# 3
# def longest_word(*arg):
#     longest = ""
#     for word in arg:
#         if len(word) > len(longest):
#             longest = word
#     return longest

# longest = longest_word("Alicia dos Santos Pinto", "Maria", "Matteo Presley", "Alessandro")
# print(longest)

# 4
# def build_sentence(separator, *words):
#     sentence = ""
#     for word in words:
#         sentence += word
#         sentence += separator
#     return sentence


# sentence = build_sentence(" ", "Jag", "bor", "i", "Marstrand")
# print(sentence)

# 5
# def describe_scores(student_name, *scores):
#     return student_name, len(scores), sum(scores) // len(scores)

# student_name, number_of_scores, average = describe_scores("Alessandro", 1, 2, 3, 4, 5)
# print(f"{student_name}: {number_of_scores} scores and average:{average}")