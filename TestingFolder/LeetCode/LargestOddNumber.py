num = "10133890"

#print(num[-1])

if int(num[-1]) % 2 == 1:
    print(num)

odds = []
for digit in num:
    digit = int(digit)
    if digit % 2 == 1:
        odds.append(str(digit))
# Print all odd digits concatenated as a string
print("".join(odds))
