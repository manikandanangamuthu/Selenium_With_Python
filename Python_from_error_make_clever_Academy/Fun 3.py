
# get input for a and b and pass it to function called printrange().
# let function print number from a to b.


def printrange(a,b):

    for i in range(a,b+1):
        print(i)
a=int(input("get value from a: "))
b=int(input("get value from b: "))

printrange(a,b)