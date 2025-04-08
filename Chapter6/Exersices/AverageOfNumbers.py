# 6. Average of Numbers
#  Assume a file containing a series of integers is named numbers.txt and exists on the 
# computer’s disk. Write a program that calculates the average of all the numbers stored in 
# the file.

#VERRY SIMILAR TO PREVIOUS ONE

def numberStuff(numbers):
    total = 0.0
    size = 1
    numbers = open(numbers,"r")
    
    for lines in numbers:
        number = float(lines)
        total += number
        size += 1
    
    avg = total / size
    return avg




def main():
    numbers = "Chapter6\\numbers.txt"
    avg = numberStuff(numbers)
    print(f"average {format(avg,"0.2f")}")

main()
    