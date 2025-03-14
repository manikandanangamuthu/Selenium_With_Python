#
#
# # Example 1
#
# # create string value
#
# s="mani"
# s='mani'
# s=str("mani")
# s=str('msni')
#
# # Creating empty string value
#
# name =str()
# # name =str("")
# # name=str('')
# #====================================================
#
# # Example 2
#
# # Mutable -->> can not change the value of the variable
# # Immutable -->> can change the value of the variable
#
# str1="Welcome"
#
# print(id(str1)) # 2306655497840
#
# str1=str1+"to python"
#
# print(id(str1))  #1427794526336
# # If the value got change after updation it is called immutable


#======================================================================

# example 3   + and * with string

str1="mani"
print(str1+"kandan")

print(str1*5)

#==========================================================================

# example 4 --> slicing value

str1="manikandan"  # m a n i k a n d a n
                   # 0 1 2 3 4 5 6 7 8 9

print(str1[1:3])  # 1-> starting index and 3 -> ending index

print(str1[:5])  # Starting index will take default 0


print(str1[2:])  # ending value not spcified so it will end with the string


print(str1[2:-1])  # removing the letters from  last character as per end value if it negative value


#==========================================================


# example ord() and chr()

print(ord('A'))

print(chr(88))


#============================================================

# example  max() and min() and len()

print(max("manikandan"))
print(min('manikandan'))
print(len("mani"))

#==============================================================
# example 7, in --> not in operator --> true or false
s="manikandan"
print("mani" in s)
print("manoj" in s )

#=============================================================

# example String comparison

print ("mani" == "kandan")  # false
print('mani'=="mani") # true
print("mass">"ka") # true
print('mani'>="mani") # true
print(('manikandan'<'ma')) # false
print("poda"<="manikdan") # false
print("mass">"") # true


#===================================================


# example 9 Testing string --> True or false

name="manikdandan"

print(name.isalnum()) # false

print(name.isalpha()) # true

print(name.islower()) # true
print(name.isupper()) # false
print("123".isdigit()) # true
print(name.isspace()) # false
#========================================================

# example 10 --> searching for substrings

name1="mani kandan"

print(name1.startswith("mani")) # true
print(name1.endswith("mani")) # false
print(name1.find("kan"))
print(name1.count('a'))

#============================================================

# example 11 --> converting string

name2="TamiL"

name3=name2.capitalize()
print(name3)

name4=name2.title()
print(name4)

name5=name2.lower()
print(name5)

name6=name2.upper()
print(name6)

name7=name2.replace("T","E")
print(name7)

#===============================================

# example 12  --> reverse string

str5="mani"
rev_str=""
for i in str5:
    rev_str=i+rev_str

print("reverse string is: ",rev_str)

# method 2
rev_str=str5[::-1]
print(rev_str)