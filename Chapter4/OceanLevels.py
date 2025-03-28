#  9. Ocean Levels
#  Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, create an 
# application that displays the number of millimeters that the ocean will have risen each year 
# for the next 25 years.

level = 1.0
rate = 1.6
for i in range(1,25):
    annual = level * (rate * i)
    print(f"Total level for year {i}: {annual:.2f}")