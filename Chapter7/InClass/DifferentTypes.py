import random
import matplotlib.pyplot as plt



data  = []

for i in range(20):
    new = random.randint(45,55)
    data.append(new)
print(f"Whole list: {data}")


print(f"The First Element: {data[0]}")


data2 = data
data2 = list(data2)
print(data2[::-1])



try:
    index_of_52 = data.index(52) 
    print(f"Index of 52: {index_of_52}")
except ValueError:
    print("not in list")

smallest = min(data)
print(f"smallest{smallest}")


# for item in data:
#     if item == 50:
#         print(f"{item},True")