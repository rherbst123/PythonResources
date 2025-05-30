#  12. Average Steps Taken
#  A Personal Fitness Tracker is a wearable device that tracks your physical activity, calories 
# burned, heart rate, sleeping patterns, and so on. One common physical activity that most 
# of these devices track is the number of steps you take each day.
#  If you have downloaded this book’s source code from the Premium Companion Website, 
# you will find a file named steps.txt in the Chapter 06 folder. (The Premium Companion 
# Website can be found at www.pearsonglobaleditions.com/gaddis.) The steps.txt file 
# contains the number of steps a person has taken each day for a year. There are 365 lines 
# in the file, and each line contains the number of steps taken during a day. (The first line is 
# the number of steps taken on January 1st, the second line is the number of steps taken on 
# January 2nd, and so forth.) Write a program that reads the file, then displays the average 
# number of steps taken for each month. (The data is from a year that was not a leap year, 
# so February has 28 days.)



def main():
    with open("Chapter6/steps.txt") as step_file:
        steps_list = [int(line.strip()) for line in step_file]

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_names = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    
    index = 0
    for month, days in enumerate(days_in_month):
        print(f"{month_names[month]}:")
        for day in range(days):
            print(f"  {month_names[month]} {day + 1}: {steps_list[index + day]}")
        index += days

    index = 0
    for month, days in enumerate(days_in_month):
        month_steps = steps_list[index:index+days]
        avg_steps = sum(month_steps) / days
        print(f"{month_names[month]}: {avg_steps:.2f} average steps")
        index += days

main()