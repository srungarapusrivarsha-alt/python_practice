# method overriding
class animal:
    def sound(self):
        print("animal makes sound..")
class dog(animal):
    def sound(self):
        print("dog says bow-bow")
class cat(animal):
    def sound(self):
        print("cat says meow-meow")
animal_sound=[cat(),dog()]
for i in animal_sound:
    i.sound()

# duck typing
# "it it is walking like duck making sound like duck thn treat it as duck"
# irrespective of object it works only on same method
class teacher:
    def work(self):
        print("teacher is working")
class engineer:
    def work(self):
        print("engineer is working")
class doctor:
    def work(self):
        print("doctor is working")
t=teacher()
e=engineer()
d=doctor()
def profession(person):
    person.work()
profession(t)
profession(e)
profession(d)

# method overloading in python
class shopping:
    def bill(self,*prices):
        return sum(prices)
s=shopping()
print(s.bill(200))
print(s.bill(200,400))
print(s.bill(200,400,600))

class notification:
    def send(self):
        print("sending notification")
class email_notification(notification):
    def send(self):
        print("sending email notification")
class sms_notification(notification):
    def send(self):
     print("sending sms notification")
class whatsapp_notification(notification):
    def send(self):
     print("sending whatsapp notification")
notifications=[email_notification(),sms_notification(),whatsapp_notification()]
for i in notifications:
    i.send()



