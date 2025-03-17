""" v On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are 
as follows:
 •	Pocket	0	is	green.
 •	For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered 
pockets are black.
 •	For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered 
pockets are red.
 •	For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered 
pockets are black.
 •	For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered 
pockets are red.
 Write a program that asks the user to enter a pocket number and displays whether the 
pocket is green, red, or black. The program should display an error message if the user 
enters a number that is outside the range of 0 through 36 """

pocket = int(input("Enter a pocket number: "))



if pocket == 0:
    print("Green!")
elif pocket > 0 and pocket < 11:
    if pocket % 2 ==0:
        print("Pocket is Black")
    if pocket % 2 == 1:
        print("Pocket is Red")
elif pocket > 10 and pocket < 19:
    if pocket % 2 == 0:
        print("Pocket is Red")
    if pocket % 2 == 1:
        print("Pocket is black")
elif pocket > 19 and pocket < 30:
    if pocket % 2 == 0:
        print("Pocket is black")
    if pocket % 2 == 1:
        print("Pocket is red")
elif pocket > 29 and pocket < 37:
    if pocket % 2 == 0:
        print("Pocket is red")
    if pocket % 2 == 1:
        print("Pocket is black")
elif pocket > 36:
    print("Too damn high!!!")