import math
from itertools import permutations

n = 10


IndDigits = []

n = str(n)

for digits in n:
    digits = int(digits)
    IndDigits.append(digits)


all_Digits = permutations(IndDigits)

# Convert each permutation tuple back into a single integer
perm_numbers = [int(''.join(map(str, perm))) for perm in all_Digits]

for number in perm_numbers:
    if number > 0 and (number & (number - 1)) == 0:
        print(f"{number} is a power of 2")
    else: 
        print(f"{number} is not a power of 2")

