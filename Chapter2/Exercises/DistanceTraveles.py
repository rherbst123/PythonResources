"""  Assuming there are no accidents or delays, the distance that a car travels down the inter
state can be calculated with the following formula:
 Distance = Speed X Time
 A car is traveling at 70 miles per hour. Write a program that displays the following:
 • The distance the car will travel in 6 hours
 • The distance the car will travel in 10 hours
 • The distance the car will travel in 15 hours """


speed = 70


time = int(input("How long will you drive for?: "))


distance = (speed * time)
print("You will have traveled:", distance, "Miles")


