#  1. Valid Number Information
#  Design a program that uses a loop to build a list named valid_numbers that contains only 
# the numbers between 0 and 100 from the numbers list below. The program should then 
# determine and display the total and average of the values in the valid_numbers list.
#  numbers = [74, 19, 105, 20, −2, 67, 77, 124, −45, 38]

numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

valid_numbers = []

invalid_numbers = []

total_for_valid = 0

index = 0
for i in range(len(numbers)):
    #print(numbers[index])
    if numbers[index] > 0 and numbers[index] < 100:
        print(f"{numbers[index]} is in the good range.")
        valid_numbers.append(numbers[index])
        #print(valid_numbers)
    else:
        print(f"{numbers[index]} is NOT in the good range")
        invalid_numbers.append(numbers[index])
        #print(invalid_numbers)
    index += 1

print(f"Valid Numbers: {valid_numbers}")

index2 = 0
for i in range(len(valid_numbers)):
    total_for_valid += valid_numbers[index2]
    index2 += 1

print(f"Total of Valid Numbers: {total_for_valid}")
print(f"Average of Valid Numbers: {total_for_valid // len(valid_numbers)}")
print(f"Invalid Numbers: {invalid_numbers}")