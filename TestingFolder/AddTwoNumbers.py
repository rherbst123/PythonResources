l1 = [2,4,3]
l2 = [5,6,4]

l1 = l1[::-1]
l2 = l2[::-1]

print(l1,l2)

l1 = int("".join(map(str,l1)))
l2 = int("".join(map(str,l2)))

result = l1 + l2
result = str(result)
final = []
for digit in result:
    final.append(int(digit))
print(final[::-1])