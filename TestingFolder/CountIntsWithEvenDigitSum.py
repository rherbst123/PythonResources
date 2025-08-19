num = 2

counter = 0

for number in range(1, num + 1):
    number_str = str(number)
    digitsSum = []
    for digit in number_str:
        digitsSum.append(int(digit))
    if sum(digitsSum) % 2 == 0:
        counter += 1
print(counter)
