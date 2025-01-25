#looping statements
#for loop
vegetables=['onion','potato','cabbage','tomato']
for vegetable in vegetables:
    print(vegetable)

#while loop
count=0
while count<5:
    print(count)
    count+=1

#nested for loop
for i in range(5):
    for j in range(2):
        print(i,j)

#nested while loop
outer=0
while outer<5:
    inner=0
    while inner<3:
        print(outer,inner)
        inner+=1
    outer+=1
      