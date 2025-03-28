#  11. Sleep Debt
#  A “sleep debt” represents the difference between a person’s desirable and actual amount 
# of sleep. Write a program that prompts the user to enter how many hours they slept each 
# day over a period of seven days. Using 8 hours per day as the desirable amount of sleep, 
# determine their sleep debt by calculating the total hours of sleep they got over the seven-day 
# period and subtracting that from the total hours of sleep they should have got. If the user 
# does not have a sleep debt, display a message expressing your jealousy.

totalSleep = 0
neededSleep = 56 
for i in range(7):
    sleep = int(input(f"Enter how much you slept for night {i+1}: "))
    totalSleep += sleep
#print("Total amount of sleep: ",totalSleep)
if totalSleep < neededSleep:
    print(f"you need more sleep, you got {totalSleep}, but needed {neededSleep} hours")
if totalSleep == neededSleep:
    print(f"Pro sleeper, with a toal of {totalSleep} hours")
if totalSleep > neededSleep:
    print(f"Too much sleep with {totalSleep} hours")



