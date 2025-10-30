# 4.  Number Analysis Program
# Design a program that asks the user to enter a series of 20 numbers. The program should 
# store the numbers in a list then display the following data:
# •  The lowest number in the list
# •  The highest number in the list
# •  The total of the numbers in the list
# •  The average of the numbers in the list

import random

def makeList():
    numbers = []
    for i in range(20):
        randomNumber = random.randint(1,100)
        numbers.append(randomNumber)
    return numbers

def lowestNumber(numbers):
    numbers.sort()
    print(numbers)
    lowest = numbers[0]
    return lowest

def totalOfNumbers(numbers):
    total = sum(numbers)
    # for number in numbers:
    #     total += number
    return total

def averageOfNumbers(numbers, total):
    sizeOfList = len(numbers)
    print("Size of List: ", sizeOfList)
    average = total / sizeOfList
    return average


def highestNumber(numbers):
    numbers.sort()
    #print(numbers)
    highest = numbers[-1]
    return highest

def main():
    numbers = makeList()

    print(numbers)
    lowest = lowestNumber(numbers)
    print(f"The smallest numbers is: {lowest}")

    highest = highestNumber(numbers)
    print(f"The Largest numbers is: {highest}")

    total = totalOfNumbers(numbers)
    print(f"The Total of the list is: {total}")

    average = averageOfNumbers(numbers, total)
    print(f"The Average of the list is: {format(average,"0.1f")}")

main()

