
#Example 1
#
# global_var=20 # Global variable
#
# def myfun():
#     local_var=10    # local variable
#     print(local_var)
#     print(global_var)
# myfun()
#
# #print(local_var)  # invalid because local_var is local var of function
# print(global_var)  # valid because global_var is global var of function

#====================================================
# Example 2

# x=100
#
# def cool():
#     global x
#     x=500
#     print(x)
# #cool()
# print(x)

#=====================================

# example 3

def cool():
    global x
    x=100
    print(x)

cool()
print(x)