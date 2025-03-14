

# get integer value from student(user input) and pass it to function studentmark().
# let the function should decide if student mark less than 35 fail or else pass


def studentmark(mark):

    if mark>35:
        print("Pass")
    else:
        print("Fail")

mark=int(input("Enter Student Mark: "))
studentmark(mark)

