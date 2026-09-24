class EmailNotification:
    def send(self):
        return "This is an EMAIL notification"

class SMSNotification:
    def send(self):
            return "This is an SMS notification"

class PushNotification:
    def send(self):
            return "This is an PUSH notification"


notifications = [EmailNotification(), SMSNotification(), PushNotification()]

for notification in notifications:
     print(notification.send())

# The loop doesnt need to know which exact objct is since all of them implement same method