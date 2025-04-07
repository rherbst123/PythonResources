#  1. File Display
#  Assume a file containing a series of integers is named numbers.txt and exists on the com
# puter’s disk. Write a program that displays all of the numbers in the file.


f = open("Chapter6\\numbers.txt", 'r')
for i in f:
    print(i, end='')