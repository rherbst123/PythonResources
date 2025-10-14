# 2. File Head Display

#  Write a program that asks the user for the name of a file. The program should display only 
# the first five lines of the file’s contents. If the file contains less than five lines, it should 
# display the file’s entire contents.


def display(file_name):
    
    #tells you how many lines are in the textg file, for our case it is 21 TOTAl lines, we only want the first 5
    numOfLines = sum(1 for i in open(file_name)) # for anything in file # = 43 
    print(f"{numOfLines}, numOfLines")
    
    #Open file, if number of lines is lessThan 5 print it all, if greater than 5, only print 5 lines
    info = open(file_name, "r")

    if numOfLines < 5:
        for line in info:
            print("less than 5",line, end='')
            
    else:
        for i in range(10):
            print(info.readline(), end='') #Read line
            
def main():
    #file_name = input("Enter a file path: ")
    file_name = "Chapter6/numbers.txt"
    display(file_name)

main()