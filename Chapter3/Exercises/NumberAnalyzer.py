""" Write a program that asks the user to enter an integer. The program should display 
“Positive” if the number is greater than 0, “Negative” if the number is less than 0, and 
“Zero”	if	the	number	is	equal	to	0.	The	program	should	then	display	“Even”	if	the	number	
is even, and “Odd” if the number is odd """



number = int(input("Enter a number "))
print("Your number is:", number)

if number % 2 == 0:
    print("Your number is even")
else:
    print(number, "is odd")

if number > 0:
    print("Number is positive")
else:
    print("Number is negative")

