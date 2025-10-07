# 4.  Roman Numerals
# Write a program that prompts the user to enter a number within the range of 1 through 10. 
# The program should display the Roman numeral version of that number. If the number is 
# outside the range of 1 through 10, the program should display an error message. The fol-
# lowing table shows the Roman numerals for the numbers 1 through 10


number = int(input("Enter a number to convert: "))


if number == 1:
    print("I")
if number == 2:
    print("II")
if number == 3:
    print("III")
if number == 4:
    print("IV")
if number == 5:
    print("V")
if number == 6:
    print("VI")
if number == 7:
    print("VII")
if number == 8:
    print("VIII")
if number == 9:
    print("IX")
if number == 10:
    print("X")

if number >10 or number <1:
    print("error")
        