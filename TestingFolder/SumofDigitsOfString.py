s = "zbax"

k = 2

numbers = []
new = ""

for letter in s:
    digit = ord(letter)
    digit = digit - 96
    numbers.append(digit)
for number in numbers:
    new += str(number)

for _ in range(k):
    sumOfDigits = []
    for digit in new:
        digit = int(digit)
        sumOfDigits.append(digit)
    new = str(sum(sumOfDigits))

print(int(new))
