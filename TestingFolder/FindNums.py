nums = [1,3,5,6]
target = 2

def find_target_index(nums, target):
    for index, value in enumerate(nums):
        if value == target:
            return index
    if target not in nums:
        for index, value in enumerate(nums):
            if value > target:
                return index
        return len(nums)

result = find_target_index(nums, target)
print(result)
    