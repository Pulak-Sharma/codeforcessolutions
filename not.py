class EmailNotification:
    def send(self):
        print("Sending Email Notification")
class SMSNotification:
    def send(self):
        print("Sending SMS Notification")
class PushNotification:
    def send(self):
        print("Sending Push Notification")
notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]
for notification in notifications:
    notification.send()
