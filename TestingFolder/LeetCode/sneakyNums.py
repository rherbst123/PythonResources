nums = [7,1,5,4,3,4,6,0,9,5,8,2]

sneaky = {}
final =[]
for numbers in nums:
    if numbers in sneaky:
        sneaky[numbers] += 1

    else:
        sneaky[numbers] = 1

for num, count in sneaky.items():
    if count == 2:
        final.append(num)
return final