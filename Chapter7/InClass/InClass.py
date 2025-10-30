names = ['John', 'Emma', 'Michael', 'Sarah', 'David', 'Lisa', 'James', 'Emily', 'Daniel', 'Sophia']

check = input("Enter a name in the roster: ")

if check in names:
    print(f"{check} is in the roster!")
else:
    names.append(check)
    print(names)


print(names.index("Sarah"))

names.insert(3, "Riley")

print(names)

removeName = input("Remove a name in the list: ")
names.remove(removeName)
print(names)
print(names[::-1])