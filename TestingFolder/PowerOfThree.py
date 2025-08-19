n = -1

powerOfThree = n ** (1/3)

if n < 3:
    print("False")
    print(powerOfThree)
else:
    if powerOfThree % 3 == 0:
        print("True")
        print(powerOfThree)
    else: 
        print("False")
        print(powerOfThree)