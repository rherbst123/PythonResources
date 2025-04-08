#  1. File Display
#  Assume a file containing a series of integers is named numbers.txt and exists on the com
# puter’s disk. Write a program that displays all of the numbers in the file.


f = open("Chapter6\\numbers.txt", "r")
f2 = open("Chapter6\\numbers.txt", "r")
info = f.readline()
info2 = f2.read() # enter a number in the parenteses for .read(), it will print out that many characters
print(f"First line:\n {info}")
print(50*"=","\n")
print(f"Whole Thing:\n {info2}") 