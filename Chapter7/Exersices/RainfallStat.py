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
    print(rain)
    return rain





def main():
    rain_logging()


main()