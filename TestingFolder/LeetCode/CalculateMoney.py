n = 4

i = 1
week = 1
total = 0
for day in range(1, n+1):
    total += i
    i += 1
    if day % 7 == 0:
        week += 1
        i = week
print(total)