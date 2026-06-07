class Student:
    brand = "Kia"
    speed = 170
    color = "red"
    seats = 4
    pay = 4320
    def __init__(self):
        print("Design your car!")
    def change_details(self):
        self.brand = input("Enter your car brand")
        self.speed = int(input("Enter the speed of your car "))
        self.color = input("Change the colour of your car ")
        self.seats = int(input("How many seats do you need... "))
        self.pay = int(input("How much pay? "))
        user = input("accelerate or deaccelerate ")
        if user == "accelerate":
            self.accelerate()
        else:
            self.deaccelerate()
    def show_details(self):
        print(self.brand)
        print(self.speed)
        print(self.color)
        print(self.seats)
        print(self.pay)
    def accelerate(self):
        self.speed += 10
    def deaccelerate(self):
        self.speed -= 10
AAGH = Student()
AAGH.change_details()
AAGH.show_details()