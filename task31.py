#program to create laptop objects
class laptop():
    color="black"
    brand="hp"
    ram="4gb"
    def on(self):
        print("your laptop is on")
        print(self.ram)
    def off(self):
        print("your laptop is shutdown")
        print(self.color)
Dell=laptop()
Dell.on()
Dell.off()
    



