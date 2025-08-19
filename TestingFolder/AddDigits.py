num = 38


if num < 10:
    print(num)

while num > 9:
    num = sum(int(digit) for digit in str(num))
    print(num)
