#vowels or not
vowels=["a","e","i","o","u"]
letter=input("enter the letter:")
if letter==vowels:
    print("letter is vowel")
else:
    print("letter is consonant")

#age group classification
age=int(input("enter your age:"))
if age<=12:
    print("you are child")
elif age<=17:
    print("you are teanager")
elif age<=64:
    print("you are an adult")
else:
    print("you are senior")

#number classification
number=int(input("enter number:"))
if number>0:
    print("number is positive")
elif number==0:
    print("number is zero")
else:
    print("number is negative")

#leap year calender
year=int(input("enter the year:"))
if year%4==0 and year%100!=0 or year%400==0:
    print("leap year")
else:
    print("non leap year")

#calculator
num_1=int(input("enter number:"))
num_2=int(input("enter number:"))
operator=input("enter operator:")
if operator=="+":
    print("num_1+num_2")
elif operator=="-":
    print("num_1-num_2")
elif operator=="*":
    print("num_1*num_2")
elif operator=="/":
    print("num1/num_2")
else:
    print("the operator is invalid")

#short hand if
x=8
print("even" if x%2==0 else "odd")

#discount calculator
original_cost=float(input("enter the cost:"))
discount=float(input("enter the discount:"))
final_cost=original_cost-(original_cost*(discount/100))
print(final_cost)

#BMI
weight=float(input("enter weight:"))
height=float(input("enter height:"))
BMI=float(weight/(height**2))
print(BMI)                          