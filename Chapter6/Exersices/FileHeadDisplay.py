# 2. File Head Display

#  Write a program that asks the user for the name of a file. The program should display only 
# the first five lines of the file’s contents. If the file contains less than five lines, it should 
# display the file’s entire contents.


def display(file_name):
    info = open(file_name, "r")
    for i in info:
        print(info)
        return info
            

def main():
    file_name = input("Enter the filepath for the file: ")
    display(file_name)

main()