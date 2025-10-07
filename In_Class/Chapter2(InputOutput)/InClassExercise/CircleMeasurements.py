# 9.  Circle Measurements
# Write a program that asks the user to enter the radius of a circle. The program should cal-
# culate and display the area and circumference of the circle using πr2 for the area and 2πr 
# for the circumference.
# Hint: You can either use 3.14159 as the value of pi (π), or add the statement "import math" 
# to the start of the program and then use "math.pi" wherever you need the value of pi in 
# the program.

PI = 3.14159

radius = float(input("What is the radius of the Circle?: "))

area = PI * (radius ** 2)

print(f"The Area is: {format(area, "0.2f")}")

circumferencea = 2 * PI * radius

print(f"The circumferencea of the circle is: {format(circumferencea, "0.2f")}")

