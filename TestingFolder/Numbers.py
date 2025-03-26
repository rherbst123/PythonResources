test = int(input("Enter Num: "))

n = test
prev = 0

while True:
    # If input number becomes 0, just print 0 and break
    if n == 0:
        print(0)
        break
    
    # Store the current number as 'prev'
    prev = n
    print("Previous", prev)

    # Extract four digits of the current number
    digits = [0] * 4
    temp_n = n
    for i in range(4):
        digits[i] = temp_n % 10
        temp_n //= 10
        print("Get 4 digits of number", temp_n)

    # Sort digits to form the ascending number
    digits.sort()
    asc = 0
    for i in range(4):
        asc = asc * 10 + digits[i]
    print("Ascending", asc)

    # Re-sort (descending) to form the descending number
    digits.sort()
    desc = 0
    for i in range(3, -1, -1):
        desc = desc * 10 + digits[i]
    print("Descending", desc)

    # Compute the absolute difference
    diff = abs(asc - desc)
    print("Absolute diff :", asc, "-", desc, "=", diff)

    # If the difference matches the previous number, we've reached Kaprekar's constant
    if diff == prev:
        print(diff)
        break
    else:
        # Otherwise, keep iterating with the new difference
        n = diff
