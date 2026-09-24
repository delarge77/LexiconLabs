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
class Printer:
    def display_status(self):
        return "Printer"

class Screen:
    def display_status(self):
            return "Screen"

objs = [Printer(), Screen()]
for objc in objs:
     print(objc.display_status())

# It works because both have the same method name

# D

