#  5. Sum of Numbers
#  Assume a file containing a series of integers is named numbers.txt and exists on the com
# puter’s disk. Write a program that reads all of the numbers stored in the file and calculates 
# their total.

#pretty simple
def main():
    numbers = open("Chapter6\\numbers.txt","r")

    total = 0.0

    for lines in numbers:
        number = float(lines)
        total += number

    print(total)

main()