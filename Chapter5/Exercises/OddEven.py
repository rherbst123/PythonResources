# 16. Odd/Even Counter
#  Programming Exercises 
#  In this chapter, you saw an example of how to write an algorithm that determines 
# whether a number is even or odd. Write a program that generates 100 random numbers 
# and keeps a count of how many of those random numbers are even, and how many of 
# them are odd

import random

def numberGen():
    numbers = []
    for counter in range(10):
        number = random.randint(1,100)
        numbers.append(number)
        
    print(numbers)
    oddOrEven(numbers)
    return numbers

def oddOrEven(numbers):
    odd = 0
    even = 0
    for number in numbers:
        if number % 2 == 0:
            even += 1
        if number % 2 == 1:
            odd += 1
    print(f"There were: {odd} odd numbers and {even} even numbers")
    return odd, even

def main():
    numberGen()    
    return 0
    

main()