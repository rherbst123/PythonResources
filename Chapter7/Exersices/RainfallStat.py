#  3. Rainfall Statistics
#  Design a program that lets the user enter the total rainfall for each of 12 months into a  
# list. The program should calculate and display the total rainfall for the year, the average 
# monthly rainfall, the months with the highest and lowest amounts.


def rain_logging():
    rain = []
    month = 1
    for i in range(12):
        rain_fall = int(input(f"Enter the rainfall for month {month}: "))
        rain.append(rain_fall)
        month += 1
    #print(rain)
    return rain

def average(rain):
    total = 0    
    for i in range(len(rain)):
        total += rain[i]
        i += 1
    
    print(f"The Average of the rainfall is: {total / len(rain)} inches")
    return average == total / len(rain)


def high_and_low(rain):
    highest = max(rain)
    lowest = min(rain)
    highest_month = rain.index(highest) + 1
    lowest_month = rain.index(lowest) + 1

    print(f"The highest rainfall is: {highest} inches, which occurred in month: {highest_month}")
    print(f"The lowest rainfall is: {lowest} inches, which occurred in month: {lowest_month}")


def main():
    rain = rain_logging()
    average(rain)
    high_and_low(rain)


main()