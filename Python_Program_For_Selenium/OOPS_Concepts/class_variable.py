# # # # # Example --> Class variable
# # # #
# # # # class Myclass:
# # # #
# # # #     a,b=10,25   # Class variable
# # # #
# # # #     def fun_add(self):
# # # #         print(self.a + self.b)  # Adding A+B value
# # # #     def fun_mul(self):
# # # #         print(self.a * self.b)
# # # #
# # # # mc=Myclass()
# # # # mc.fun_add() # 10+25 = 35
# # # # mc.fun_mul() # 10*25 = 250
# # #
# # # #========================================================
# # #
# # # # Example 2
# # #
# # # i,j,k=10,20,30
# # #
# # #
# # # class Myclass:
# # #
# # #     a,b=50,100  # a,b is class variable
# # #
# # #     def add(self,x,y): # x,Y is local variable
# # #         print(x+y)
# # #         print(self.a+self.b)
# # #         print(i+j+k)
# # #
# # # mc=Myclass()
# # # mc.add(100,200)
# #
# #
# # #==================================================
# #
# # a,b=10,20  # globals variable
# #
# # class Myclss:
# #
# #     a,b=30,40  # class variable
# #     def add(self,a,b):
# #         print(a+b)
# #         print(self.a+self.b)
# #         print(globals()['a']+globals()['b'])  # When we access global variable the we need to use global inbulid function if the variable name same for local and global and class variable
# #
# # mc=Myclss()
# # mc.add(50,60)
#
# #======================================================================
#
# # Example 4 -->  One class can have multiple objects
#
# class myclass:
#
#     def display(self,name):
#         print("Thi sis display method....")
#         print(name)
# obj1=myclass()
# obj1.display("Mani")
#
# obj2=myclass()
# obj2.display("kandan")

#=============================================================

# Example 5 -->>