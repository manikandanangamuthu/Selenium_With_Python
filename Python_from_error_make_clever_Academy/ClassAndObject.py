# create a class called student

# create a variable = name and register no using constructor

# craete function called display which should display the name and register no of the student


class student:

    def __init__(self):
        self.name="Mani"
        self.regno="1"
    def display(self):
        print(self.name)
        print(self.regno)

stu=student()
#print(stu.name)
#print(stu.regno)
stu.display()
