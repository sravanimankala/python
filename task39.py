#exception handling 
try:
    num_1=int(input('enter a number :'))
    print(num_1)
except Exception as msg:
    print(f"NameError : {msg}")


try:
    num_1=int(input('enter a number :'))
    print(num_1)
except Exception as msg:
    print(f"ValueError : {msg}")


try:
    list_1=[1,2,34,3,2]
    print(list_1(3))
except Exception as msg:
    print(f"TypeError : {msg}")


try:
    list_1=[1,2,3,4,32]
    print(list_1)
except Exception :
    print(Exception)


try:
    num_1=int(input('eneter num_1:'))
    num_2=int(input('eneter num_2:'))
    print(num_1/num_2)
except Exception as msg:
    print(f"ZeroDivisionError : {msg}")


try:
    list=[2,4,5,4,53,8]
    print(list[10])
except Exception as msg:
    print(f"IndexError : {msg}")


try:
    dict={1:34,2:32,3:45,4:56,5:23}
    print(dict[7])
except Exception as msg:
    print(f"KeyError : {msg}")