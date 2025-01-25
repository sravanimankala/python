#1.squaring all numbers
square_all=map(int,input("enter number:").split())
obj=map(lambda i:i**2,square_all)
print(list(obj))

#2.filtering positive numbers
filter_positive=map(int,input("enter number:").split())
obj=filter(lambda i:i>=0,filter_positive)
print(list(obj))

#3.factorial of given number
from functools import reduce
factorial_number=int(input("enter number:"))
obj=reduce(lambda i,j:i*j,range(1,factorial_number+1))
print(obj)

#4.count the vowels
from functools import reduce
count_vowels=input("enter string:").lower()
vowels='aeiou'
obj=reduce(lambda acc,char:acc+(1 if char in vowels else 0),count_vowels,0)
print(obj)