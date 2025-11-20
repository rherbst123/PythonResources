nums = [2,5,7,8,9,2,3,4,3,1]
k = 3

for numbers in nums:
    for i in range(len(nums) - k + 1):
        window = nums[i:i+k]
        is_increasing = all(window[j] + 1 == window[j+1] for j in range(len(window)-1))
        if is_increasing:
            print(True)
            break
        else:
            if i == len(nums) - k:
                print(False)