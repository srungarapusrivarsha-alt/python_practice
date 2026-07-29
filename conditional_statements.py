print("*"* 10)
print("STUDENT ANALYZER")
student_name=input("enter student name")
tel=int(input("enter telugu marks"))
hin=int(input("enter hindi marks"))
eng=int(input("enter english marks"))
math=int(input("enter math marks"))
sci=int(input("enter science marks"))
total_marks=tel+hin+eng+math+sci
average=total_marks/5
percentage=(total_marks/500)*100
if percentage>=90:
    print("grade A")
    grade ="A"
elif percentage>=70:
    print("grade B")

    grade ="B"
elif percentage>=50:
    print("grade C")
    grade ="C"
else :
    print("fail")
    grade ="F"
if percentage>=35:
    result="pass"
elif percentage>=60:
    result="distinction"
print("*"* 7)
print("student report view")
print("student_name:",student_name)
print("total_marks:",total_marks)
print("average_marks:",average)
print("percentage:",percentage)
print("grade:",grade)
print("result:",result)

print("*"* 10)
print("online shopping discount")
product_price=int(input("enter product price:"))
membership_type=input("enter membership_type of gold/silver/regular/coupon:")
coupon=input("enter coupon need yes/no:")
discount=0
if membership_type=="gold":
    discount=20
elif membership_type=="silver":
    discount=10
elif membership_type=="regular":
    discount=5
elif membership_type=="coupon":
    discount+=5
discount_amount=product_price*discount/100
total_amount=product_price-discount_amount
print("*"*20)
print("shopping bill")
print("*"*20)
print("product_price:",product_price)
print("membership_type:",membership_type)
print("coupon:",coupon)
print("discount_amount:",discount_amount)
print("total_amount:",total_amount)
print("*************THANK YOU ***************")


