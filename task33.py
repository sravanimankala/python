#inheritance
class parent():
    properties="10acrs"
    def details(self):
        print("this is a parent class")
class child(parent):
    def details1(self):
        print('this is child class')
        print(self.properties)
obj=child()
obj.details1()
obj.details()
print(obj.properties)

