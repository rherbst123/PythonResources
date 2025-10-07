# 2.  Calories Burned
# Running on a particular treadmill you burn 4.2 calories per minute. Write a program that 
# uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes


CALORIES_PER_MINUTE = 4.2
total_calories_burned = 0

for minute in range(10,31,5):
    caloriesBurned = CALORIES_PER_MINUTE * minute
    total_calories_burned += caloriesBurned
    print(f"For minute: {minute}, you burned a total of {caloriesBurned} calories for a total of {total_calories_burned}")