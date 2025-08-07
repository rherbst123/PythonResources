nums = [0,1,0,3,12]

nums = sorted(nums)

for number in nums:
    if number == 0:
        nums.remove(number)
        nums.append(number)

print(nums)
