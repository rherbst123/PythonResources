import random

numbers = []
for i in range(50):
    newNumber = random.randint(1,200)
    numbers.append(newNumber)

print(f"Unsorted: {numbers}")

numbers.sort()
print(f"Sorted: {numbers}")

print(f"Largest Number: {max(numbers)}")
print(f"Smallest Number: {min(numbers)}")

