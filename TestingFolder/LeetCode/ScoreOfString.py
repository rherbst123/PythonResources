s = "hello"

numbers = []
for ch in s:
    numbers.append(ord(ch))
print(numbers)

i = 0

# print(abs(numbers[i] - numbers[j]))

# print(abs(numbers[i+1] - numbers[j+1]))

# print(abs(numbers[i+2] - numbers[j+2]))

# print(abs(numbers[i+3] - numbers[j+3]))

total = []
for i in range(len(numbers) - 1):
    diff = abs(numbers[i] - numbers[i + 1])
    total.append(diff)
print(sum(total))
    