# 1. Kilometer Converter
#  Write a program that asks the user to enter a distance in kilometers, then converts that 
# distance to miles. The conversion formula is as follows:
#  Miles 5 Kilometers 3 0.6214

def kiloToMiles(kilometers):
    miles = kilometers * 0.6124
    return miles


kilometers = float(input("Enter a distance in kilometers: "))

print(kiloToMiles(kilometers))