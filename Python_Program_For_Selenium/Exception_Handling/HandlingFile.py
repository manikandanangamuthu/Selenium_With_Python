# # example 1: Writing data in to text file
#
# file=open("D:\Manikandan\Demo_FileHandling\Myfile.txt",'w')
#
# file.write("This is 1st statement...\n")  #\n --> creating new line
# file.write("This is 2nd statement...\n")
# file.write("This is 3rd statement...\n")
# file.close()
#
# print("Program completed...")


# Example 2 --> read

# file=open("D:\Manikandan\Demo_FileHandling\Myfile.txt",'r')
# #print(file.read())  # It will read all lines of text file
# print(file.readline())
# file.close()
# print("Program completed...")

# Example 3 ---> Appeanding data into text file

file=open("D:\Manikandan\Demo_FileHandling\Myfile.txt",'a')

file.write("Im adding new line using appeand mode\n")

file.close()
print("program is completed ")