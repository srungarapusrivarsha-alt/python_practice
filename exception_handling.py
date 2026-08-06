# student percentage calculator
try:
    name=input("enter your name:")
    marks=[]
    for i in range(1,6):
        mark=float(input("enter subject{i} marks"))
        marks.append(mark)
        if mark <0 or mark>100:
            raise ValueError("the mark should be between 0 to 100")
except ValueError:
    print("invalid marks")
else:
    total=sum(marks)
    percentage=total/5
    print("**student percentage**")
    print("student name :",name)
    print("total marks:",total)
    print("perecentage:",percentage)
finally:
    print("report view")    


try:
    print("**menu**")
    print("1.add")
    print("2.subtract")
    print("3.divide")
    print("4.multiply")
    choice=int(input("enter the choice"))
    num1=float(input("enter num1:"))
    num2=float(input("enter num2:"))
    if choice==1:
        result=num1+num2
    elif choice==2:
        result=num1-num2
    elif choice==3:
        result=num1/num2
    elif choice==4:
        result=num1*num2
    else :
        raise ValueError("invalid menu choice")
except ValueError:
     print("enter proper value") 
     pass
except ZeroDivisionError:
    print("number cannot divisible by 0")
else:
    print("result=",result)
finally:
    print("completed successfully")


class banking_application(Exception):
    pass
balance=float(input("enter your bank balance:"))
while True:
    try:
        print("**menu**")
        print("1.deposit")
        print("2.withdraw")
        print("3.check balance")
        print("4.exit")
        choice=int(input("enter choice to perform operation:"))
        if choice==1:
            amount=float(input("enter amount here:"))
            if amount <=0:
                raise ValueError("enter valid amount")
            balance+=amount
            print("amount deposited successfully..")
            print("balance is:",balance)
        
        elif choice==3:
            print("check balance",balance)
        elif choice==2:
            amount=float(input("enter amount to withdraw"))
            if amount<=0:
                raise ValueError("invalid number")
            elif amount>balance:
                raise ValueError("insufficient balance")
            else:
                balance-=amount
                print("amount withdrawn successfully...")
        elif choice==4:
            print("exited..")
            print("thankyou!!!")
            break
        
    except ValueError:
        print("enter valid number")
    finally:
        print("completed......")