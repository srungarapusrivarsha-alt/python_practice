def welcome():
    print("welcome ....")
welcome()

def add(a,b):
    print("sum is:",a+b)
num1=int(input("enter num 1:"))
num2=int(input("enter num 2:"))
add(num1,num2)

def sub(a,b):
    print("diff is :",a-b)
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
sub(num1,num2)

def even(num): 
    if num%2==0:
        print("even")
    else:
        print("odd")
i=int(input("enter number:--"))
even(i)

def area_rect(l,b):
    area=l*b
    print("area is :--",area)
l=int(input("enter number length:-")) 
b=int(input("enter number breadth:-"))
area_rect(l,b)   

def simple_interest(p,t,r):
    interest=(p*t*r)/100
    print("simple interest is :-",interest)
p=float(input("enter principal:"))
t=float(input("enter time:"))
r=float(input("enter rate of interest:"))
simple_interest(p,t,r)

def prime(num):
    if num<1:
        print("not prime")
        return
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            return
    else:
        print("prime number")
num=int(input("enter a number:-"))
prime(num)

def reverse(text):
    print("reverse:",text[::-1])
text=input("enter text:")
reverse(text)   

def emp_sal(basic,bonus,tax):
    salary=basic+bonus-tax
    print("final salary:",salary)
basic=float(input("enter basic amount:"))
bonus=float(input("enter bonus salary:"))
tax=float(input(("enter tax paid:")))
emp_sal(basic,bonus,tax)    


students=[]
def show_menu():
    print("student profile")
    print("1.add student")
    print("2.view student")
    print("3.search student")
    print("4.update student")
    print("5.delete student")
def add_student():
    name=input("enter name:")
    marks=int(input("enter marks:"))
    student={
        "name":name,
        "marks":marks
    }
    students.append(student)
    print("student added successfully...")
    print(students)
def view_students():
    if len(students)==0:
        print("no students found")
        return
    for student in students:
        print("student name:",student["name"])
        print("student marks:",student["marks"])
def search_student():
    search=input("enter name :")
    for student in students:
     if student["name"]==search:
         print("student name:",student["name"])
         print("student marks:",student["marks"])
         return
    print("student not found")
def main():
    while True:
     show_menu()    
     choice=int(input("enter your choice:-"))
     if choice ==1:
        add_student()
     elif choice ==2:
       view_students()
     elif choice ==3:
        search_student()
     elif choice ==6:
        print("exit")
        print("thankyou")
        break
main()

