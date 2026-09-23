# A

# class BadTeam:
#     def __init__(self, name, members = []) -> None:
#         self.name = name
#         self.members = members

#     def add_member(self, member):
#         self.members.append(member)

# badTeam1 = BadTeam("Alessandro")
# badTeam2 = BadTeam("Maria")

# badTeam1.add_member([1, 2, 3, 4, 5])

# print(badTeam1.members)
# print(badTeam2.members)


# class Team:
#     def __init__(self, name, members = None):
#         self.name = name

#         if members is None:
#           members = []
#         self.members = members

#     def add_member(self, member):
#         self.members.append(member)

# team1 = Team("Alessandro")
# team2 = Team("Maria")

# team1.add_member([1, 2, 3, 4, 5])

# print(team1.members)
# print(team2.members)

# B
# movie = {"title":"The Godfather", "director":"Francis Ford Coppola", "rating":10}

# class Movie:
#     def __init__(self, title, director, rating) -> None:
#         self.title = title
#         self.director = director
#         self.rating = rating

#         def high_rated(self):
#             if self.rating > 90:
#                 return "Awesome Movie"
#             else: 
#                 return "Average Movie"

# C
# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

# class SavingsAccount(Account):
#     def __init__(self, owner, balance, interest_rate):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate

# account = Account("Alessandro", 60000)
# savings = SavingsAccount(account.owner, account.balance, 0.50)

# print(account.owner, account.balance)
# print(savings.owner, savings.balance, savings.interest_rate)

# D
# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def get_information(self):
#         return f"Employee {self.name}"

# class Developer(Employee):
#     def greetingDeveloper(self):
#         return f"{self.name} is a developer"

# class Teacher(Employee):
#     def greetingTeacher(self):
#             return f"{self.name} is a teacher"
    
# developer = Developer("Alessandro")
# teacher = Teacher("Maria")

# print(developer.greetingDeveloper())
# print(teacher.greetingTeacher())

# E
# class Device:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#         self.is_active = True

#         if self.year < 1990:
#             self.is_active = False

    

# class Laptop(Device):
#     def __init__(self, brand, year, ram_gb):
#         super().__init__(brand, year)
#         self.ram_gb = ram_gb

# class Mobile(Device):
#     def __init__(self, brand, year, model):
#         super().__init__(brand, year)
#         self.model = model

# laptop = Laptop("Apple", 1989, 256)
# mobile = Mobile("Apple", 2026, 256)


# print(laptop.brand, laptop.year, laptop.ram_gb, laptop.is_active)
# print(mobile.brand, mobile.year, mobile.model, mobile.is_active)

