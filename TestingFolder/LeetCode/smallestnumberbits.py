n = 10
final = []


n = bin(n)
n = n[2:]
for dig in n:
    final.append(dig)
for i, dig in enumerate(final):
    if dig == '0':
        final[i] = '1'

final = int(''.join(final), 2)
return final
