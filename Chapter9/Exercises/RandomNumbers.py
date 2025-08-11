# 5.  Random Number Frequencies
# Write a program that generates 100 random numbers between 1 and 10. The program 
# should store the frequency of each number generated in a dictionary with the number as 
# the key and the amount of times it has occurred as the value. For example, if the program 
# generates the number 6 a total of 11 times, the dictionary will contain a key of 6 with an associated value of 11. Once all of the numbers have been generated, display information 
# about the frequency of each number.

import random

numbers = []

#Generate 100 Random numbers 
for counter in range(100):
    number = random.randint(1,10)
    numbers.append(number)

#print(numbers)

#Empty Dictionary
number_counts  = {}

#For each number in the numbers list
for number in numbers:
    #Take the empty Dictionary with the number in the list = dictionary
    number_counts[number] = number_counts.get(number ,0 ) + 1

for num in range(1, 11):
    print(f"Number {num}: {number_counts.get(num, 0)} times")

