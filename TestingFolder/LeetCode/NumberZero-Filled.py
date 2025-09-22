nums = [1,3,0,0,2,0,0,4]

permutations = 0
i = 0
while i < len(nums):
    if nums[i] == 0:
        count = 0
        while i < len(nums) and nums[i] == 0:
            count += 1
            i += 1
        permutations += count * (count + 1) // 2
    else:
        i += 1

print(permutations)
