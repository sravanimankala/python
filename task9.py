#1.area of rectangle
length=int(input("enter the length:"))
width=int(input("enter the width:"))
area=length*width
print(area)

#2.incrementing and decrementing a variable
num_1=10
num_1+=5 #+operator is used to increment the value of variable
num_2=6
num_2-=2 #-operator is used to decrement the value of variable
print(num_1)
print(num_2)

#3.convert celsius to fahrenheit
celsius=float(input("enter the celsius"))
Fahrenheit=(celsius * 9/5)+32
print(Fahrenheit)

#4.simple intrest
principal_amount=float(input("enter principal amount: "))
rate=float(input("enter rate of intrest: "))
time=float(input("enter time in years: "))
intrest=(principal_amount*rate*time)/100
print(f"simple intrest is {intrest}")

#5.concatenate
num_1=input("enter a number:")
num_2=input("enter a number:")
result=num_1+num_2
print(result)

#6.kilometers  to miles
kilometers=float(input("enter value in kilometers: "))
conv_fac=0.621371
miles=kilometers*conv_fac
print(miles)