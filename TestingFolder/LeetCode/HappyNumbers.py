n = 19

seen = []
while n != 1 and n not in seen:
    seen.append(n)
    digits = [int(d) ** 2 for d in str(n)]
    n = sum(digits)
if n == 1:
    print("Happy number")
else:
    print("Not a happy number")
