# A
# class EmailNotification:
#     def send(self):
#         return "This is an EMAIL notification"

# class SMSNotification:
#     def send(self):
#             return "This is an SMS notification"

# class PushNotification:
#     def send(self):
#             return "This is an PUSH notification"


# notifications = [EmailNotification(), SMSNotification(), PushNotification()]

# for notification in notifications:
#      print(notification.send())

# The loop doesnt need to know which exact objct is since all of them implement same method

# B
# class Document:
#     def __init__(self, title) -> None:
#         self.title = title

#     def describe(self):
#         return self.title

# class PDFDocument(Document):
#     def describe(self):
#         return "This is a PDF Document"

# class TextDocument(Document):
#     def describe(self):
#             return "This is a TEXT Document"

# pdf1 = PDFDocument("pdf1")
# pdf2 = PDFDocument("pdf2")
# txt1 = TextDocument("txt1")
# txt2 = TextDocument("txt2")

# files = [pdf1, pdf2, txt1, txt2]

# for file in files:
#      print(file.title)
#      print(file.describe())

# C
# class Printer:
#     def display_status(self):
#         return "Printer"

# class Screen:
#     def display_status(self):
#             return "Screen"

# objs = [Printer(), Screen()]
# for objc in objs:
#      print(objc.display_status())

# It works because both have the same method name

# D
# class User:
#     pass

# class AdminUser(User):
#     pass

# admin_user = AdminUser()
# print(isinstance(admin_user, AdminUser))
# print(isinstance(admin_user, User))
# print(isinstance(admin_user, str))

# E
# class Product:
#     def __init__(self, name, price) -> None:
#         self.name = name
#         self.price = price

#     def __str__(self) -> str:
#         return f"Product name {self.name} and price: {self.price}"

# product1 = Product("Laptop", 2000)
# product2 = Product("Apple", 0.50)
# product3 = Product("vinyl", 180)
# print(product1, product2, product3)

# str_obj = str(product1)
# print(type(str_obj))

# F
# class Account:
#     def __init__(self, owner, balance) -> None:
#         self.owner = owner
#         self.balance = balance

#     def __str__(self):
#         return f"Owner : {self.owner} and balance: {self.balance}"

# class SavingAccount(Account):
#     def __init__(self, owner, balance, interest_rate) -> None:
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate

#     def __str__(self):
#         base_str = super().__str__()
#         return (base_str + f"Interest rate: {self.interest_rate}")

# account = Account("Alessandro", 6000000)
# saving = SavingAccount("Alessandro", 6000000, 0.25)

# print(account)
# print(saving)

# G
# class CPU:
#     def __init__(self, model) -> None:
#         self.model = model

# class Computer:
#     def __init__(self, brand, cpu: CPU) -> None:
#         self.brand = brand
#         self.cpu = cpu

# cpu = CPU("machintosh")
# computer = Computer("Apple", cpu)

# print(computer.brand)
# print(computer.cpu.model)

# Car has a Engine, Manager is a employee, Course has a teacher, Phone is a device

# H
# class Export:
#     def export(self, data)->str:
#         self.data = data
#         return "Base data"

# class Console(Export):
#     def export(self, data):
#         return "Console data"

#     def __str__(self):
#         return f"Return Console data {self.data}"

# class Text(Export):
#     def export(self, data):
#         return "Text data"

#     def __str__(self):
#             return f"Return Text data {self.data}"

# class Summary(Export):
#     def export(self, data):
#         return "Summary data"

#     def __str__(self):
#         return f"Return Summary data {self.data} "

# console = Console()
# text = Text()
# summary = Summary()

# exports =[console, text, summary]

# def exposure_data(exports):
#     for export in exports:
#         class_type = str(type(export))
#         print(export.export({class_type:f"data{class_type}"}))

# exposure_data(exports)

# class Example:
#      def export(self, data):
#         self.data = data
#         return "Example data"
     
#      def __str__(self):
#         return f"Return Example data {self.data} "

# exports.append(Example())
# exposure_data(exports)



