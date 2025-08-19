num = "6777133339"

max_triplet = ""
count = 1

for i in range(1, len(num)):
    if num[i] == num[i-1]:
        count += 1
        if count == 3:
            triplet = num[i] * 3
            if max_triplet == "" or triplet > max_triplet:
                max_triplet = triplet
    else:
        count = 1

print(max_triplet if max_triplet != "" else "No digit repeats 3 times consecutively")