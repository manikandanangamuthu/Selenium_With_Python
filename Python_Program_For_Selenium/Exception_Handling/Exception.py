# #
# # Example 1
# # print("this is starting point program..")
# # print("this is starting point program..")
# # print("this is starting point program..")
# # try:
# #     print(x)
# # except:
# #     print("Exception Occured")
# # print("this is after x program..")
#
# # example 2
# #
# # print("This is starting point of program..")
# # print("program in progress")
# # try:
# #    print(10/5)
# #  except:
# #      print("This exception error handled..")
# # print("After exception error")
#
# # Example 3  ->> Multiple except blocks...  - try, except, else, finally
#
# try:
#     num1,num2=10,2  # use 10,2 and try instead 10,0
#     result=num1/num2
#     print("Result is:",result)
# except ZeroDivisionError:
#     print("Thrown zeroDivisionError exception...")
#
# except SyntaxError:
#     print("Thrown syntax error exception....")
# except:
#     print("thrown handled..")
# else:
#     print("No exception occured...")
# finally:
#     print("Always execute...")

# Example 4: raising our own exceptions..


def enter_age(num):
    if num<0:
        raise ValueError("only Integers are allowed")
    if num%2==0:
        print("even")
    else:
        print("add")
print("checking number is even or add by calling functions,,")
num=-1
try:
    enter_age(num)
except ValueError:
    print("value error exception occured and handled....")
print("program complated....")
