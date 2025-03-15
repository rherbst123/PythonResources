"""  The area of a rectangle is the rectangles length times its width. Write a program that asks 
for the length and width of two rectangles. The program should tell the user which rectan
gle has the greater area, or if the areas are the same.
 """

rec1W = int(input("Enter the Width of rectangle 1: "))
rec1H = int(input("Enter the Height of rectangle 1: "))

areaRec1 = rec1W * rec1H
print("Areat of Rectangle 1 is: ", areaRec1)


rec2W = int(input("Enter the Width of rectangle 2: "))
rec2H = int(input("Enter the Height of rectangle 2: "))

areaRec2 = rec2W * rec2H
print("Area of Rectangle 2 is: ", areaRec2)

if areaRec1 > areaRec2:
    print("Rectangle 1 is larger than rectangle 2")
else:
    print("Rectangle 2 is larger than rectangle 1")