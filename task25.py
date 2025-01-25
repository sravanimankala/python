#1.create a tuple
tuple=("sravani","20","black")
print(tuple)

#2.access tuple elements
days=('sunday','monday','tuesday','wednesday','thursday','friday','saturday')
print(days[2])

#3.tuple concatenation
odd=(1,3,5)
even=(2,3,6)
tuple=odd+even
print(tuple)

#4.tuple unpacking
tuple=(5,10)
length,width=tuple
print("length:",length)
print("width:",width)
area=length*width
print(area)

#5.check if an element exists
tuple=(1,2,3,4,5)
number=(3)
result=number in tuple
print(result)

#6.super market
items=[("apple",99),("banana",99),("milk",49)]
total=0
print("item\tprice")
print("-"*15)
for i,j in items:
    print(f"{i}\t{j}")
    total+=j
print("-"*15)
print("total\t",total)