"""  Write a program that asks the user for a month as a number between 1 and 12. The 
program should display a message indicating whether the month is in the first quarter, 
the second quarter, the third quarter, or the fourth quarter of the year. Following are the 
guidelines:
 •	If	the	user	enters	either	1,	2,	or	3,	the	month	is	in	the	first	quarter.
 •	If	the	user	enters	a	number	between	4	and	6,	the	month	is	in	the	second	quarter.
 •	If	the	number	is	either	7,	8,	or	9,	the	month	is	in	the	third	quarter.
 •	If	the	month	is	between	10	and	12,	the	month	is	in	the	fourth	quarter.
 •	If	the	number	is	not	between	1	and	12,	the	program	should	display	an	error. """

month = int(input("Enter a number coorespnding to a numeric month code: "))

if month in {1,2,3}:
    print("first quarter")

if month in {4,5,6}:
    print("Second Quarter")

if month in {7,8,9}:
    print("Third quarter")

if month in {10,11,12}:
    print("Fourth Quarter")

if month > 12:
    print("ERROR")
