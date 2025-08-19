n = 7

dupe = n

if n == 1:
    print("True")
if n == 2:
    print("False")

while n != 1:
    n = str(n)
    total = []
    for digit in n:
        digit = int(digit)
        digit = digit ** 2
        total.append(digit)
        n = sum(total)
    if n in total and n != 1:
        print("False")
        break
    print(n)
    print("True")


    
