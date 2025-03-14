class myclass:
    def __init__(self):
        print("this is constructor")
    def m1(self):
        print("this is method...")

    def m2(self,a,b):
        return (a+b)
mc=myclass()  # --> no need to create object for printing value
mc.m1()  # method we have call explicitely by using object

print(mc.m2(20,30))