#if conditon
age = 18
if age>18:
     print("you are elgible to vote:")
     print(f"you age is {age} you are adult")
     print(age+10)
print("this is outside of code")

#elif conditon
marks = int(input("enter marks: "))
if marks>=90:
     print(f"you got A grade you obtained {marks} marks")
elif marks>=80:
     print(f"you got B grade you obtained {marks} marks")
elif marks>=70:
     print(f"you got C grade you obtained {marks} marks")
elif marks>=35:
     print(f"you got D grade you obtained {marks} marks")
else:
     print(f"you got F grade you obtained {marks} marks")

#if else conditon
user_name = input("enter username: ")
password =  input("enter password: ")
if user_name == "sravani":
     if password == "9948288231":
         print("Login success.........")
     else:
         print("invalid password..")
else:
     print("invalid username..")





