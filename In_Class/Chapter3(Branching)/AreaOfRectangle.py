# 2.  Areas of Rectangles
# The area of a rectangle is the rectangle’s length times its width. Write a program that asks 
# for the length and width of two rectangles. The program should tell the user which rectan-
# gle has the greater area, or if the areas are the same.

rect1Width = int(input("Enter the Width for rectangle 1: "))

rect1Length = int(input("Enter the Length for rectangle 1: "))


rect2Width = int(input("Enter the Width for rectangle 1: "))

rect2Length = int(input("Enter the Length for rectangle 1: "))

rect1Area = rect1Width * rect1Length

rect2Area = rect2Width * rect2Length

print(f"The area for rectangle 1 is: {rect1Area} and the area for rectangle 2 is: {rect2Area}")

if rect1Area == rect2Area:
    print("The two rectangles are the same")
else:
    print("The two rectangles are NOT the same")