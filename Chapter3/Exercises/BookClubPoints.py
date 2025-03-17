"""  11. Book Club Points
 Serendipity Booksellers has a book club that awards points to its customers based on the 
number of books purchased each month. The points are awarded as follows:
 •	If	a	customer	purchases	0	books,	he	or	she	earns	0	points.
 •	If a customer purchases 2 books, he or she earns 5 points.
 •	If a customer purchases 4 books, he or she earns 15 points.
 •	If a customer purchases 6 books, he or she earns 30 points.
 •	If a customer purchases 8 or more books, he or she earns 60 points.
 Write a program that asks the user to enter the number of books that he or she has pur
chased this month, then displays the number of points awarded """


numBooks = int(input("Enter how many books you have bought this past month: "))
print("You have bought", numBooks, "books this month")


if numBooks == 0 or numBooks == 1:
    print("0 points awarded.")
elif numBooks == 2 or numBooks == 3:
    print("5 points given")
elif numBooks == 4 or numBooks == 5:
    print("15 points given")
elif numBooks == 6 or numBooks == 7:
    print("30 points given")
elif numBooks > 8:
    print("60 points given")