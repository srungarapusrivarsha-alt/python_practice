class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_details(self):
        print("name of person:",self.name)
        print("age is :",self.age)
class student(person):
    def __init__(self, name, age,roll_no,course):
        super().__init__(name,age)
        self.roll_no=roll_no
        self.course=course
    def study(self):
        print(f"{self.name} is studying course of {self.course}")
std=student("veena",22,"22p71a6696","cse(ai&ml)")
std.display_details()
std.study()



class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def start(self):
        print("vehicle started")
    def stop(self):
        print("vehicle stopped")
class car(vehicle):
    def __init__(self,brand,model,fuel_type):
        super().__init__(brand,model)
        self.fuel_type=fuel_type
    def drive(self):
        print(f"{self.brand} with fuel_type {self.fuel_type} is driven...")
c=car("suzuki","innova","petrol")
c.start()
c.drive()
c.stop()


class employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
    def display_employee(self):
        print("employee_id is:",self.emp_id)
        print("employee_name is :",self.name)
        print("employee_salary:",self.salary)
class developer(employee):
    def __init__(self, emp_id, name, salary,programming_language):
        super().__init__(emp_id, name, salary)
        self.programming_language=programming_language
    def write_code(self):
        print(f"developer with name of  {self.name} with {self.emp_id} is developing application by writing code in programming language of {self.programming_language}")
d=developer(101,"varsha",500000,"python")
print(d.name)
print(d.emp_id)
print(d.salary)
print()
d.display_employee()
d.write_code()

# multiple inheriance
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        if amount<=0:
            print("enter valid amount")
        else:
            self.balance+=amount
            print("amount after deposition:",self.balance)
            print("amount deposited successfully....")
    def withdraw(self,amount):
        if amount>=self.balance:
            print("please withdraw valid amount")
        else:
            self.balance-=amount
            print("amount after withdraw:",self.balance)
            print("amount withdrawn successfully...")
    def check_balance(self):
        print("The total amount:",self.balance)
class savings_account(BankAccount):
    def add_interest(self,rate):
        interest=self.balance*rate/100
        self.balance+=interest
        print(f"Amount of savings account after applied interest is {self.balance}")
s=savings_account(123456,300000)
s.deposit(20000)
s.withdraw(30000)
s.add_interest(20)
s.check_balance()


class teacher():
    def __init__(self,teacher_name):
        self.teacher_name=teacher_name
    def teach(self):
        print("teaching python")
class researcher():
    def research(self):
        print("researching ai ")
class professor(teacher,researcher):
    def guide_students(self):
        print("guiding students")
p=professor("mr.sirajjudin")
print(p.teacher_name)
p.teach()
p.research()
p.guide_students()


class camera:
    def take_photo(self):
        print("camera is accessing for taking pictures")
class music_player:
    def play_music(self):
        print("we can play music")
class smart_phone(camera,music_player):
    def mobile(self):
        print("mobile is applicable for both camera and playing music")
s=smart_phone()
s.take_photo()
s.play_music()
s.mobile()


class person:
    def __init__(self,name,department):
        self.name=name
        self.department=department
    def display_details(self):
        print("name:",self.name)
        print("department:",self.department)
class employee(person):
    def __init__(self,name,department):
        super().__init__(name,department)
    def work(self):
        print(f"employee {self.name}in department {self.department} is working.. ")
class manager(employee):
    def approve_leaf(self):
        print("leave approved successfully...")
m=manager("varsha","IT")
m.display_details()
m.work()
m.approve_leaf()

class book:
    def read(self):
        print("reading the book..")
class ebook(book):
    def download(self):
        print("downloading ebook....")
        print("**downloaded successfully**")
class programming_book(ebook):
    def practice_code(self):
        print("practicing code in python programming language")
pb=programming_book()
pb.read()
pb.download()
pb.practice_code()

class account:
    def create_account(self):
        print("account created..")
class savings_account(account):
        def deposit(self):
         print("amount deposited successfully in account...")
class premium_savings(savings_account):
    def add_interest(self):
        print("interest added successfully....")
ps=premium_savings()
ps.create_account()
ps.deposit()
ps.add_interest()

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
email=email_notification()
sms=sms_notification()
wtsapp=whatsapp_notification()
email.send()
sms.send()
wtsapp.send()


