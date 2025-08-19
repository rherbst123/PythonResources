digits = [2,7,4]
k = 181
numbers = ""


for number in digits:
    number = str(number)
    numbers += number
result = [int(digit) for digit in str(int(numbers) + k)]
print(result)