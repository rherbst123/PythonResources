

def fibs(n):
    w = 0
    x = 1
    y = 1

    if n == 0:
        return n
    elif n == 1 or n == 2:
        return 1
    else:
        for _ in range(3, n + 1):
            z = w + x + y
            w = x
            x = y
            y = z
        return z
    
def main():
    n = int(input("Enter n: "))
    result = fibs(n)
    print(result)
main()