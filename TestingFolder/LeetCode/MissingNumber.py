nums = [3,0,1]

nums = sorted(nums)

for i in nums:
    if i + 1 < len(nums) and nums[nums.index(i) + 1] > i + 1:
        missing = (i + 1)
        return missing
        