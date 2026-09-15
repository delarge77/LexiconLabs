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
def nestedFunctionsOne():
    startDay = "Monday"
    def nestedFunctionTwo():
        print(startDay)
    nestedFunctionTwo()


nestedFunctionsOne()



