"""  2. Calories Burned
 Running on a particular treadmill you burn 4.2 calories per minute. Write a program that 
uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes """


cpm = 4.2
minutes = 0
burned = 0
for counter in range(5,31,5): #From index 5 to 30(less than 31) in increments of 5, 1:Start, 2:Stop, 3:Step
    print("You have burned", format(burned,"0.1f"), "clories in", minutes, "minutes")
    minutes += 1
    burned += cpm
