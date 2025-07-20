# # 14.    Gas Prices
# # In  the  student  sample  program  files  for  this  chapter,  you  will  find  a  text  file  named   
# # GasPrices.txt.  The  file  contains  the  weekly  average  prices  for  a  gallon  of  gas  in  the  
# # United States, beginning on April 5th, 1993, and ending on August 26th, 2013. Figure 8-7 
# # shows an example of the first few lines of the file’s contents:

# Each line in the file contains the average price for a gallon of gas on a specific date. Each line 
# is formatted in the following way:
#   MM-DD-YYYY:Price
# MM is the two-digit month, DD is the two-digit day, and YYYY is the four-digit year. Price is 
# the average price per gallon of gas on the specified date.
# For this assignment, you are to write one or more programs that read the contents of the file 
# and perform the following calculations:
# Average Price Per Year: Calculate the average price of gas per year, for each year in the file. 
# (The file’s data starts in April of 1993, and it ends in August 2013. Use the data that is pres-
# ent for the years 1993 and 2013.)
# Average Price Per Month: Calculate the average price for each month in the file.
# Highest and Lowest Prices Per Year: For each year in the file, determine the date and amount 
# for the lowest price, and the highest price.
# List of Prices, Lowest to Highest: Generate a text file that lists the dates and prices, sorted 
# from the lowest price to the highest.
# List of Prices, Highest to lowest: Generate a text file that lists the dates and prices, sorted 
# from the highest price to the lowest.
# You can write one program to perform all of these calculations, or you can write different 
# programs, one for each calculation

def averagePrice_year(lines):
    allPrices = []
    for prices in lines:
        allPrices.append(float(prices[11:15]))
    size = len(allPrices)
    total = sum(allPrices)
    average = total // size
    return average

def averagePrice_month(lines):
    months = []      
    month_prices = [] 

    for line in lines:
        month = line[:2]
        year = line[6:10]
        price = float(line[11:])
        key = f"{month}-{year}"

        if key in months:
            idx = months.index(key)
            month_prices[idx].append(price)
        else:
            months.append(key)
            month_prices.append([price])

    # Print averages
    for i in range(len(months)):
        avg = sum(month_prices[i]) / len(month_prices[i])
        month_price = f"{months[i]}: ${avg:.3f}"
        print(month_price)



def lowest_highest(lines):
    high_to_low = []
    for line in lines:
        date, price = line.split(":")
        high_to_low.append((date, float(price)))
    high_to_low.sort(key=lambda x: x[1])

    # Print the 10 lowest prices
    print("10 Lowest Prices:")
    for date, price in high_to_low[:10]:
        print(f"{date}: ${price:.3f}")

    # Print the 10 highest prices
    print("\n10 Highest Prices:")
    for date, price in high_to_low[-10:][::-1]:
        print(f"{date}: ${price:.3f}")



def highest_lowest(lines):
    for year in range(1993, 2014):
        highest_price = -1
        lowest_price = float('inf')
        highest_date = ""
        lowest_date = ""

        for line in lines:
            date, price = line.split(":")
            price = float(price)
            line_year = int(date[-4:])

            if line_year == year:
                if price > highest_price:
                    highest_price = price
                    highest_date = date

                if price < lowest_price:
                    lowest_price = price
                    lowest_date = date

        if highest_price != -1 and lowest_price != float('inf'):
            print(f"{year} - Highest: {highest_date} - ${highest_price:.3f}, Lowest: {lowest_date} - ${lowest_price:.3f}")






def main():
    with open(r"C:\Users\Riley\Documents\GitHub\RileyPython\Chapter8\Files\gasprices.txt",'r') as file:
        lines = file.readlines()
    # print(lines)

    all_prices = averagePrice_year(lines)
    print(all_prices)
    averagePrice_month(lines)
    lowest_highest(lines)
    highest_lowest(lines)


main()