# 4.  Number Analysis Program
# Design a program that asks the user to enter a series of 20 numbers. The program should 
# store the numbers in a list then display the following data:
# •  The lowest number in the list
# •  The highest number in the list
# •  The total of the numbers in the list
# •  The average of the numbers in the list

#Get out list
numbers = []

def add_numbers():
    index = 1
    for counter in range(20):
        number = int(input(f"Enter a number for space {index}: "))
        numbers.append(number)
        index += 1
    #print(numbers)


def find_lowest(numbers):
    numbers.sort()
    print(f"The first item in the list is: {numbers[0]}")

def find_highest(numbers):
    numbers.sort()
    size = len(numbers)
    print(f"The largest number in the list is: {numbers[size -1]}")

def total_of_nums(numbers):
    total = 0
    for numbs in numbers:
        total += numbs
    print(f"The total of all numbers in the list is: {total}") 
    return total 

def average(numbers, total):
    size = len(numbers)
    average = total // size
    print(f"The average of all numbers is: {average}")


def main():
    add_numbers()
    find_lowest(numbers)
    find_highest(numbers)
    #Save total from total function
    total = total_of_nums(numbers)
    average(numbers, total)


main()