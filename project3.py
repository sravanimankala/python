name=input("enter your name:")

#list of items
list='''
rice        Rs 10/kg
chocolate   Rs 100/pack
sugar       Rs 8/kg
oil         Rs 30/liter
milk        Rs 50/kg
salt        Rs 25/kg
paneer      Rs 40/kg
maggie      Rs 12/kg
boost       Rs 200/bottle
ice cream   Rs 50/pack
colgate     Rs 20/pack
'''

#declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#rate for each item
items={'rice': 10, 'chocolate':100, 'sugar': 8, 'oil': 30,'milk':50, 'salt': 25, 'paneer': 40, 'maggie': 12, 'boost': 200, 'ice cream': 50, 'colgate': 20}

while True:
    option=input("press 1 for list or 2 to exit:")
    if option=='2':
        print("thank you for shopping")
        break
    elif option=='1':
        print(list)

        while True:
            inp1=input("to buy press 1 or press 2 to exit:")
            if inp1=='2':
                print("thank you for shopping")
                break
            elif inp1=='1':
                item=input("choose your item:")
                quantity=int(input("enter quantity:"))
            if item in items:
                price=quantity*items[item]
                pricelist.append((item,quantity,items[item],price))
                totalprice+=price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
                tax=(totalprice*5)/100
                finalprice=tax+totalprice
            else:
                print("item is invalid")
        else:
            print("entered number is invalid")
        inp=input("bill the items yes or no:")
        if inp=='yes':
            pass
            if finalprice!=0:
                print("-"*20,"hydrabadi supermarket","-"*20)
                print(" "*25,"hyderabad")
                print("Name:",name)
                print("-"*63)
                print("sno"," "*10,"items"," "*11,"quantity"," "*10,"price")
                for i in range(len(pricelist)):
                    print(i," "*13,ilist[i]," "*15,qlist[i]," "*15,plist[i])
                print("-"*63)
                print(" "*35,"total amount:","Rs",totalprice)
                print("tax amount"," "*35,"tax Rs",tax)
                print("-"*63)
                print(" "*35,"finalamount:","Rs",finalprice)
                print("-"*63)
                print(" "*20,"thanks for visiting")
                print("-"*63)
        break

                    


                    
                
