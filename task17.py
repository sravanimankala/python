#list
#indexing
my_list = [10, 20, 30, 40, 50,"sravani"]
print(my_list[0])
print(my_list[4]) 
print(my_list[2]) 
print(my_list[5]) 

#negative indexing
my_list = [10, 20, 30, 40, 50]
print(my_list[-4])
print(my_list[-1])
print(my_list[-5])

#slicing
my_list = [10, 20, 30, 40, 50, 60, 70, 80]
print(my_list[0:8])
print(my_list[:3])
print(my_list[2:6])
print(my_list[:8])

#skipping
my_list = [10, 20, 30, 40, 50, 60, 70, 80]
print(my_list[::3])
print(my_list[::4])
print(my_list[::2])

#methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
numbers.append(8)
numbers.extend([7, 0])
numbers.copy()
numbers.count(2)
numbers.index(4)
numbers.remove(1)
numbers.pop(4) 
numbers.insert(2, 10) 
numbers.reverse()
numbers.sort()
print(numbers) 