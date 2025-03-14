#
#
# # Example:
#
# class myclass:
#     def my_fun(self):
#         pass
#     def display(self,name):
#         print(name)
# mc=myclass() # mc-> my class is object we created like my class
#
# mc.my_fun()  # calling the function
# mc.display("mani")   # calling the function


# ===========================================

# example 2
class myclass:
    def m1(self):
     print("This Is Instance Method")
    @staticmethod
    def m2(self,num):
        print(self,num)
mc=myclass()
mc.m1()
mc.m2(100,200)

myclass.m2(10,25)  # here calling static method directly using class not through object


