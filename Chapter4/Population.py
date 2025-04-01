"""  13. Population
 Write a program that predicts the approximate size of a population of organisms. The  
application should use text boxes to allow the user to enter the starting number of organ
isms, the average daily population increase (as a percentage), and the number of days the 
organisms will be left to multiply. For example, assume the user enters the following values:
 Starting number of organisms: 2
 Average daily increase: 30%
 Number of days to multiply: 10
 The program should display the following table of data:
 Day Approximate
 Population
 """


startNum = int(input("Starting population: "))
Population = startNum

rate = int(input("Rate of growth: "))
rate = float(rate/100)

days = int(input("Days to simulate: "))

print("Day Approximate",15*"-","Population")

#print(days-days + 1, 30*" ", Population)
day = 1
for i in range(days):
  
  Population += Population * rate
  day += 1
  print(day,30*" ",format(Population,"0.2f"))  
    