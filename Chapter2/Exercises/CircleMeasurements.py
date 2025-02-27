"""  Write a program that asks the user to enter the radius of a circle. The program should cal
culate and display the area and circumference of the circle using πr2 for the area and 2πr 
for the circumference. """



radius = float(input("Enter the radius of some circle: "))


circle = 3.14159
area =  circle * radius ** 2
print(area)


print("The area of said circle is: ", format(area, "0.2f"))

