# # #Example 3--->> keyword arguments
# #
# # def greetings(name,greetmsg):
# #     print(greetmsg+" "+name)
# # greetings(name="mani",greetmsg="Helo")
# #
# # greetings(greetmsg="Mass",name="Mani")
#
#
# # example 4 --> comination of positional parameter and keyword arugment
#
#
# def my_fun(a,b,c):
#     print(a,b,c)
#
# my_fun(20,30,40)  # positional argument
#
# my_fun(a=10,b=20,c=30)
# my_fun(a=10,c=30,b=20)
#
# my_fun(10,20,c=30)
# my_fun(10,b=20,c=30)
#
# #my_fun(10,b=20,30) # this is wrong as positional argument must appear before any keyword argumnet

# example 5--->   function can return multiple values

def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a
print(largest(20,30))