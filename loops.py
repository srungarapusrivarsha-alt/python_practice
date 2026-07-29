for  i in range(1,11,1):
    print(i)

    
for i in range(10,0,-1):
    print(i)


for i in range(1,51):
    if i%2==0:
        print(i)


for i in range(1,51):
    if 1%2!=0:
        print(i)


n=int(input("enter number:"))
total=0
for i in range(1,n+1):
    total=total+i
    print(total)


number=int(input("enter a number to get multiplication"))
for i in range (1,11):
    print(number,"*",i,"=",number*i)


students=int(input("enter no of students"))
present=0
absent=0
for i in range (1,students+1):
    status=input("enter status P/A:--").upper()
    if status=="P":
        present+=1
    elif status=="A":
        absent+=1
    else :
        print("enter valid input ie either P/A")
attendance=(present/students)*100
print("no of students:",students)
print("no of presents:",present)
print("no of absentees:",absent)
print("attendance:",round(attendance,2))



questions = [
    "1. Python is developed by?",
    "2. Keyword to define a function?",
    "3. Extension of Python file?",
    "4. Which loop repeats until condition becomes False?",
    "5. Which keyword exits a loop?"
]
answers = [
    "guido",
    "def",
    ".py",
    "while",
    "break"
]
score=0
for i in range (len(questions)):
    print(questions[i])
    user=input("enter answer here provided question:-")
    if user==answers[i]:
        print("correct answer")
        score+=1
    else:
        print("wrong answer please try again")
percentage=(score/len(questions))*100
if percentage>=90:
    grade="A"
elif percentage>=70:
    grade="B"
elif percentage>=50:
    grade="C"
else:
    print("FAIL")
print("*"*5,"student answer report","*"*5)
print("correct answers:",score)
print("percentage:",percentage)
print("grade:",grade)




student=[]
while True:
    print("1.add student")
    print("2.view student")
    print("3.search student")
    print("4.count")
    print("5.exit")
    choice=int(input("enter  your choice:-"))
    if choice==1:
        name=input("enter name")
        student.append(name)
        print("student added successfully")
    elif choice ==2:
        if len(student)==0:
            print("no student found")
        else:
            print("student list")
            for i in student:
                print(i)
    elif choice ==3:
        i=input("enter student to search")
        if i in student:
            print(i)
        else:
            print("student not found")
    elif choice==4:
        print("count of students:",len(student))
    elif choice==5:
        print("exit")
        print("thankyou!")
        break
    else:
        print("invalid choice")