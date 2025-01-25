#1.reverse list
my_list=[10,20,30,40,50,11]
my_list.reverse()
print(my_list)

#2.common element
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
list3=[]
for i in list1:
    if i in list2:
        list3.append(i)
print(list3)

#3.unique elements
original_list=[1,2,2,3,4,4,5]
unique_list=[]
for i in original_list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)

#4.remove duplicates
duplicated_list=[1,2,2,3,4,4,5]
list=[]
for i in duplicated_list:
    if i not in list:
        list.append(i)
print(list)

#exercise1:list concatenation
list1=[1,2,3,4]
list2=[5,6,7,8]
list3=list1+list2
print(list3)

#exercise2:list repetition
list=["sravani",1,2,3,[5,6]]
result=list*3
print(result)

#exercise3:list removal
list=[1,2,3,4,5,6,7,8]
print(list[::2])

#exercise4:list insertion
list=[1,2,3,4]
list.insert(0,10)
list.insert(1,11)
list.insert(2,12)
print(list)

#list comprehensions
#1.square numbers
print([i**2 for i in range(11) if i!=0])

#2.even numbers
print([i for i in range(1,21) if i%2==0])

#3.words lengths
words=["apple","banana","cherry","date"]
print([len(word) for word in words])



