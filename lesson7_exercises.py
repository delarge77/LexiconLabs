# A
# 1
# class Book():

#     def __init__(self, title, author, pages) -> None:
#         self.title = title
#         self.author = author
#         self.pages = pages


# book1 = Book("Guitar", "Fredrik", 800)
# book2 = Book("Bass", "Andy", 750)
# book3 = Book("Drums", "Mackey", 132)

# print(book1.title, book1.author, book1.pages)
# print(book2.title, book2.author, book2.pages)
# print(book3.title, book3.author, book3.pages)

# 2
# class Laptop():
#     def __init__(self, brand, model, ram_gb, price) -> None:
#         self.brand = brand
#         self.model = model
#         self.ram_gb = ram_gb
#         self.price = price

# laptop1 = Laptop("Apple", "model1", 256, 1000)
# laptop2 = Laptop("Ericsson", "model2", 128, 800)
# laptop3 = Laptop("Le novo", "model3", 256, 1500)

# # Before updating
# print(laptop2.price)

# laptop2.price = 650
# # After updating
# print(laptop2.price)

# 3
# class Laptop():
#     def __init__(self, brand, model, ram_gb, price) -> None:
#         self.brand = brand
#         self.model = model
#         self.ram_gb = ram_gb
#         self.price = price

# laptop1 = Laptop("Apple", "model", 256, 1000)
# laptop2 = Laptop("Apple", "model", 256, 1000)

# print(laptop1 is laptop2)

# 4
# class Laptop():
#     def __init__(self, brand, model, ram_gb, price = 1000) -> None:
#         self.brand = brand
#         self.model = model
#         self.ram_gb = ram_gb
#         self.price = price

# 5
# class Laptop():
#     def __init__(self, brand, model, ram_gb, price) -> None:
#         self.brand = brand
#         self.model = model
#         self.ram_gb = ram_gb
#         self.price = price

# laptop = Laptop(brand= "Apple", model= "Model", ram_gb= 256, price= 2000)
# print(laptop.brand, laptop.model, laptop.ram_gb, laptop.price)

# B
# 1
# class Book():
#     def __init__(self, title, author, pages) -> None:
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def is_long(self):
#         if self.pages >= 300:
#             return True
#         return False

# book1 = Book("Guitar", "Fredrik", 800)
# book2 = Book("Bass", "Andy", 750)
# book3 = Book("Drums", "Mackey", 132)

# print(book1.title, book1.author, book1.pages)
# print(book1.is_long())
# print(book2.title, book2.author, book2.pages)
# print(book2.is_long())
# print(book3.title, book3.author, book3.pages)
# print(book3.is_long())

# 2
# class BankAccount():
#     def __init__(self, owner, balance) -> None:
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, deposit):
#         self.balance = self.balance + deposit

# account1 = BankAccount("Alessandro", 550000)
# account1.deposit(40000)
# print(account1.owner, account1.balance)

# 3
# class BankAccount():
#     def __init__(self, owner, balance) -> None:
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, deposit):
#         self.balance = self.balance + deposit

#     def withdraw(self, withdraw):
#         if withdraw < self.balance:
#             self.balance = self.balance - withdraw
#             return self.balance
#         raise ValueError("Insufficient balance")


# account1 = BankAccount("Alessandro", 550000)
# account1.deposit(40000)
# print(account1.owner, account1.balance)
# account1.withdraw(90000)
# print(account1.owner, account1.balance)
# account1.withdraw(600000)
# print(account1.owner, account1.balance)

# 4
# class Task():
#     def __init__(self, title, completed = False) -> None:
#         self.title = title
#         self.completed = completed

#         def complete():
#             pass

#         def reopen():
#             pass

# 5
# task1 = Task("Rock is dead")
# task2 = Task("Rock is not dead", completed= True)

# task2.completed = False

# print(task1.completed)
# print(task2.completed)








