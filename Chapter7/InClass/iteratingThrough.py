numbers = [1,5,6,8,5,3,6,7,4]

names = ["BOB", "TOM", "BILL"]

combinedList = []


#print(things)

for number in numbers:
    print(number, end=" ")
print("\n")

for name in names:
    print(name, end=" ")
print("\n")

# for name in names:
#     combinedList.append(name)
# for number in numbers:
#     combinedList.append(number)
combinedList = names + numbers
print(combinedList)