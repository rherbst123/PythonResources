n = 3

numbers = []



for i in range(n):
    i += 1
    numbers.append(i)
    # print(i)
string_without_separators = "".join(str(element) for element in numbers)
print(string_without_separators)