#advance pythons
#lambda function
add=lambda a,b:a+b
print(add(12,2))

#filter function
def even(i):
    return i%2==0
obj=(even,[1,3,5,7,9])
print(list(obj))

#map function
obj=map(lambda i:i**2,[2,8,5,3,7,2])
print(list(obj))

#reduce function
from functools import reduce
list=[4,6,8,2,3]
def multiple(a,b):
    return a*b
obj=reduce(multiple,list)
print(obj)