a = "11"
b = "1"

# Convert strings to integers using base 2
num_a = int(a, 2)
num_b = int(b, 2)

# Add the numbers
sum_num = num_a + num_b

# Convert the sum back to binary string
result = bin(sum_num)[2:]

print(result)