counter = 0

while True:
    user = input("Enter y or n: ")
    if user == "Y":
        print("yes")
        counter += 1
    if user == "N":
        break
print(counter)