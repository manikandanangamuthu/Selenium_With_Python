

# Conditional Statement

# if and if...else   elif

# Example 1

# If person eligible for vote or not

# Age>18

# Age=int(input("Enter the Your Age: "))
#
# if Age>=18:
#     print("Eligible for Vote")
# else:
#     print("Not Eligible for Vote")

# # Example 2:
#
# if True:
#     print("True conditions")
# else:
#     print("False conditions")

# Example 3
# if 1:
#     print("One")
# else:
#     print("Fail")

# Find a number is even or add

# num1=int(input("Enter the number here:"))
#
# if num1%2==0:
#     print("This is even number")
# else:
#     print("This is add number")

# # if else conditions  # single line (ternary operator)
#
# num=27
# print("even") if num%2==0 else print("add")

# # if else conditions  # multiple statement in single line (ternary operator)
# num=7
#
# {print("mani"),print("mass")} if num>=10 else {print("ECE"),print("B")}

# Multiple conditions using elif

weekno=int(input("Enter your day number here: "))

if weekno==1:
    print("Sunday")
elif weekno==2:
    print("Monday")
elif weekno==3:
    print("Tuesday")
elif weekno==4:
    print("Wednesday")
elif weekno==5:
    print("thursday")
elif weekno==6:
    print("friday")
elif weekno==7:
    print("saturday")
else:
    print("Happy Day!")


