import random

randomNumbers = []

for counter in range(100):
    number = random.randint(1,10)
    randomNumbers.append(number)

print(randomNumbers)

numberCount = {}

for numbers in randomNumbers:
    numberCount[numbers] = numberCount.get(numbers, 0) + 1

for num in range(1,11):
    print(f"Number: {num}: {numberCount.get(num, 0)} times")

