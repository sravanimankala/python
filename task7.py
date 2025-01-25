#1.program that prints a pattern using multiple print statements
print("***")
print("**")
print("*")

#2.adding comments to python script
std_1="shubman "#assigning a value to variable
std_2="gill"#assigning a value to variable
result=std_1+std_2#adding both variable values
print(result)
"""
in the above program we are taking two variables 
and assiging a values to both variables
to perform addition add operator is used
in between variables 
"""

#3.program that uses a dictionary to store information about a book
book_information={"title":"Ramayana","author":"Maharishi Valmiki","publication year":1883}
print(book_information)

#4.program that takes a string as input(35) and return float value
age=input("enter the value of age:")
float_con=float(age)
print(float_con)

#5.explore three python keywords and give examples
#true,false are used to represent truth values known as boolean values
x=15
y=18
z=15
print(x is y)
print(x is z)
#if keyword is used to create conditional statements
a=20
b=50
if b>a:print("b is greater than a")

#6.swaping the values of two variables without using a temporary variable
x=10
y=5
x=x+y#now x becomes 15
y=x-y#y becomes 10
x=x-y#x becomes 5
print("After Swapping:x=",x)
print("After Swapping:y=",y)

#7.program that takes user input for their age,converts it to an integer,add5,then print the result
age=input("enter age:")
int_con=int(age)
result=int_con+5
print(result)

#8.program that takes two numbers as input and performs the arthimetic operation
num_1=int(input("enter first number:"))
num_2=int(input("enter second number:"))
print("addition:",num_1+num_2)
print("subtraction:",num_1-num_2)
print("multiplication:",num_1*num_2)
