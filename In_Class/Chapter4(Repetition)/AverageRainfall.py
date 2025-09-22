"""  5. Average Rainfall
 Write a program that uses nested loops to collect data and calculate the average rainfall over 
a period of years. The program should first ask for the number of years. The outer loop will 
iterate once for each year. The inner loop will iterate twelve times, once for each month. 
Each iteration of the inner loop will ask the user for the inches of rainfall for that month. 
After all iterations, the program should display the number of months, the total inches of 
rainfall, and the average rainfall per month for the entire period. """

years = int(input("How many years have passed: "))

#total Inches 
totInch = 0

#Months counter
months = 0

#Total for all
added = 0

for i in range(years):
    for j in range(12):
        
        months += 1
        inches = int(input(f"How many inches for month {j + 1}: "))
        totInch += inches

        added += totInch



    print(f"Total inches for year {i + 1}: ",totInch)
    totInch = 0

average = added // months
print(f"Total rain is:", totInch, "Inches. Over", months, "months. With an average rainfall of",average, "inches per month over the time period")
    



