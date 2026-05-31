class Student():
    name="abcdefghijklmnopqrstuvwxyz"
    age=1234567891011121314151617181920
    teacher_age=5678901234567891234567891234567891234567890123456789
    teacher_name="Yurlate"
    form="URLATE"
    #constructor-gets called when object is created
    def __init__(self):
        print("UR LATE AGAIN!")
    def change_details(self):
        self.name=input("ENTER YOUR NAME!")
        self.age=int(input("ENTER YOUR AGE!"))
        self.teacher_name=input("WHAT'S MY NAME!")
        self.teacher_age=input("WHAT'S MY AGE REMEMBER I'M NOT THAT OLD!I'M ONLY A CENTURY, SO YOUNG!")
        self.form=input("*Principal barges in* Teachers says calmy, what's your classroom name?")
    def show_details(self):
        print(self.name)
        print(self.age)
        print(self.teacher_age)
        print(self.teacher_name)
        print(self.form)
#creating object of the class
Simpson= Student()
Simpson.change_details()
Simpson.show_details()