rowIndex =  3

# Generate the rowIndex-th row of Pascal's Triangle
# 1. Initialize the row with [1]
# 2. For each position from 1 to rowIndex:
#    a. Compute the next value using the previous value and the formula: value = prev_value * (rowIndex - i + 1) // i
#    b. Append the value to the row
# 3. Return the row

row = [1]

for i in range(1, rowIndex + 1):
    value = row[-1] * (rowIndex - i + 1) // i
    row.append(value)
print(row)