class student:
    pass
class employee:
    pass
class car:
    pass
class book:
    pass
s1=student()
s2=student()
s3=student()

e1=employee()
e2= employee()
e3=employee()

c1=car()
c2=car()
c3=car()

b1=book()
b2=book()
b3=book()

print(id(s1))
print(id(s2))
print(id(s3))

print(id(e1))
print(id(e2))
print(id(e3))


# variables in oops 
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("varsha",22)
print("name:",s1.name)
print("age:",s1.age)
s2=student("rak",22)
print(s2.name,s2.age)


class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("ram",22)
s2=student("raj",24)
s3=student("rai",25)
print("name:",s1.name)
print("name:",s2.name)
print("name:",s3.name)
print("age:",s1.age)
print("age:",s2.age)
print("age:",s3.age)


class student:
    def __init__(self,name,marks,standard):
        self.name=name
        self.marks=marks
        self.standard=standard
s1=student("varsha",99,7)
s1.marks=100
print(s1.marks)
print(s1.name)
print(s1.standard)

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("ravi",19)
del s1.name
print(hasattr(s1,s1.name))


class student:
    college="svit"
    def __init__(self):
        self.name="varsha"
        self.branch="cse(ai&ml)"
s=student()
print(s.college)
print(s.name)
print(s.branch)
print(s.__dict__)

class theatre:
    movie="spiderMan"
    def __init__(self):
        self.place="kphb"
        self.time="3:00'clock PM"
t=theatre()
t.movie="svsc"
print(t.movie)
print(t.place)
print(t.time)
print(t.__dict__)


class market:
    place="Bhagyanagar_Colony"
    def __init__(self,vegs,leafy):
        self.vegs=vegs
        self.leafy=leafy
m=market("tomato","spinach")
if hasattr(m,"vegs"):
    print("market has vegetables.......")
else:
    print("market has only leafy vegetables.....")

class student:
    college="svit"
    def __init__(self,name,age,marks,course):
        self.name=name
        self.age=age
        self.marks=marks
        self.cousre=course
s1=student("varsha",22,190,"cse")
s2=student("akki",23,170,"ds")
s3=student("veena",21,180,"iot")
s4=student("raj",22,187,"aiml")
students=[s1,s2,s3,s4]
for i in students:
    print("name:",i.name)
    print("age:",i.age)
    print("course:",i.cousre)
    print("college:",i.college)


class bank:
    bank_name="HDFC"
    def __init__(self,acc_num,holder_name,balance):
        self.acc_num=acc_num
        self.holder_name=holder_name
        self.balance=balance
b=bank("12345","varsha",200000)
b1=bank("78910","nithya",300000)
b2=bank("14390","veena",90000)
print(b1.acc_num)
print(b1.holder_name)
print(b1.balance)
print(b.bank_name)
print(b.acc_num)
print(b.holder_name)
print(b.balance)
bank.bank_name="SBI"
print(bank.bank_name)
# instance methods
class student:
    def intro(self):
        print("welcoome to python coding..")
std=student()
std.intro() 

class student1:
    def __init__(self,name,course):
        self.name=name
        self.course=course
    def student_info(self):
        print("name of student is:",self.name)
        print ("course specialised with:",self.course)
std1=student1("sri varsha","cse(ai&ml)")
std1.student_info()

class Bank_Account:
    def __init__(self,acc_num,balance,pin):
        self.__acc_num=acc_num
        self.__balance=balance
        self.__pin=pin
    def deposit(self,amount):
        if amount>=0:
         self.__balance+=amount
         print("amount deposited successfully....")
        else:
            print("invalid amount ")
    def withdraw(self,pin,amount):
        if pin!=self.__pin:
            print("enter valid pin..")
        elif amount<=0:
            print("enter valid amount")
        else:
            self.__balance-=amount
            print("amount withdrawn successfully...")
    def check_balance(self,pin):
        if pin!=self.__pin:
            print("enter valid pin to check your balance")
        else:
            print("balance is:",self.__balance)
b=Bank_Account(1234567,800000,12345)
b.deposit(4000)
b.withdraw(12345,7000)
b.check_balance(12345)

class Animal:
    def speak(self):
        print("Animal makes a noise")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")

class Cat(Animal):
    pass

my_dog = Dog()
my_cat = Cat()

my_dog.speak()
my_cat.speak()




    

