#1.using break in a while loop
number=[25,30,20,40,15,25]
sum=0
for i in number:
    if sum>100:
        break
    sum+=i
print(f"{sum} is exceed the 100")

#2.using continue in a for loop
for i in range(1,601):
    if i%2==0:
        continue
    print(i)

#3.using pass in conditional statements
number=int(input("enter number:"))
if number%2==0:
    print(f"{number} is even number")
else:
    pass

#4.combining transfer statements
for i in ["hi","world","string","skip","break"]:
    if i=="break":
        break
    elif i=="skip":
        continue
    print(i)