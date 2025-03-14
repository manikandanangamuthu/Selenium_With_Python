
# List


# A list is a collection which is ordered and changeable
# In python lists are written square brackets []
# List is mutable

#================================================================================================================
# how to create list
#
# mylist=[10,20,30,40,50]
#
# mylist2=["apple","banana","cherry"]
#
# mylist3=["apple",10,"banana",20]
#
# mylist4=list()  # empty list
#
# print(mylist)
# print(mylist2)
# print(mylist3)
# print(mylist4)

#================================================================================================================
# Example 2: Accessing items from the list

# mylist=["apple","banana",10,20]  # index will start from 0
# print(mylist[0])
# print(mylist[1])
#
# print(mylist[-1])      # negative value start from last index ex: -1 consider last value of the list
# print(mylist[-2])

#================================================================================================================

# Example 3: Range of indexes

# mylist=["apple","banana","mango","kiwi","orange","cherry","melon"]
#
# print(mylist[2:5])
#
# print(mylist[-4:-1])

#================================================================================================================
# example 4: Change item from the list

mylist=["apple","banana","cherry"]
print(mylist) # ['apple', 'banana', 'cherry']
#
mylist[0]="Mango" # this will change the values based on index
print(mylist)
#================================================================================================================

# Example 5: read the list items using loop

# mylist=["apple","banana","cherry","melon","orange"]
#
# for i in mylist:
#     print(i)
#
#================================================================================================================

#Exampl 6: Check if the items is exist in the list or not
#
# mylist=["apple","banana","cherry","melon","orange"]
#
# if "apple" in mylist:
#     print("Yes.. Apple is present")
# else:
#     print("Yes.. Apple is present")

# ================================================================================================================

# # Example 7: List lenth (counting number of items in a list)
#
# mylist=["apple","orange","banana"]
#
# print(len(mylist))

# # ================================================================================================================
# # example 8: Add items append() insert()
#
# mylist=["apple","orange","banana"]
#
# mylist.append("orange") # append will help us adding new items in list. It will add last in the list
# print(mylist)
#
#
# # ================================================================================================================
#
# # example 8: Add items append() or  insert()
#
# mylist=["apple","orange","banana"]
# mylist.insert(2,"melon") #  Add items some where in the list based on index
# print(mylist)

# ================================================================================================================


# Example 9 :  Remove item from the list using pop() or del

# pop() -> function, function have ()

# del -> keyword -->

# Mylist=["Apple","Orange","Banana","Cherry"]
# print(Mylist)
# Mylist.pop(1)  # pop function will remove items from the list based on index
# print(Mylist)
# del Mylist[1]  # del keyword also use for removing or deleting items from list
# print(Mylist)

# clear() -> function, function have ()
#
# Mylist=["Apple","Orange","Banana","Cherry"]
# Mylist.clear()
# print(Mylist) # []

# ================================================================================================================
# Example 10 : Copy list

Mylist1=["Apple","Orange","Banana","Cherry"]

Mylist2=list(Mylist1)

print(Mylist1)
print(Mylist2)

