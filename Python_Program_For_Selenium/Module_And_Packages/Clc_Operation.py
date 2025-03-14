# #
# # Call the functions from one module to another module
# # # Approach 1
# #
# # import Calculator
# # Calculator.add(10,20)
# # Calculator.mul(10,20)
# # Calculator.div(10,20)
# # Calculator.sub(20,10)
#
# # Approach 2
#
# from Calculator import add,mul
#
# add(10,20)
# mul(10,20)

#Approach 3

from Calculator import *

add(10,20)
sub(10,20)