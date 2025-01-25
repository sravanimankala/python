#1.print the characters at even indices
sentence="prince of indian cricket team"
print(sentence[::2])

#2.replacing spaces with underscores
sentence="he is the god of protection"
sentence1=sentence.replace(" ","_")
print(sentence1)

#3.check if string contains digits
number="9948288231"
number1=number.isdigit()
print(number1)

#4.print the string in reverse order
sentence="hare krishna"
print(sentence[::-1])

#5.captalize the first letter of each word in string

message="how are you"
message1=message.title()#title function is used to captalize the first letter of each word in string
print(message1)