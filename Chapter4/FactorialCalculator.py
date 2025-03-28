# 12. Calculating the Factorial of a Number
#  In mathematics, the notation n! represents the factorial of the nonnegative integer n. The 
# factorial of n is the product of all the nonnegative integers from 1 to n. For example,
#  7!  1  2  3  4  5  6  7  5,040
#  and
#  4!  1  2  3  4  24
#  Write a program that lets the user enter a nonnegative integer then uses a loop to calculate 
# the factorial of that number. Display the factorial.

number = int(input("Enter a number to calculate: "))
numbers = []

number = number + 1
for i in range(number):
    
    number = number - 1
    numbers.append(number)
    print(numbers)
numbers.pop()
print(numbers)
size = len(numbers)

factorial = 1
for number in numbers:
    factorial *= number
    print(number)
print(f"The Factorial of {number} is: {factorial}")
    
    
    
    