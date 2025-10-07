counter = 0

while True:
    user = int(input("Enter a Number: "))
    if user % 2 == 0:
        counter += 1
        if counter == 5:
            print("You have entered 5 even numbers")
            break
    elif user % 2 == 1:
        print("Nope Try again")
