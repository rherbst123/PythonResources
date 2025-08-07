nums1 = [4,9,5]
nums2 = [9,4,9,8,4]


intersection = []
for num in set(nums1):
    if num in nums2:
        intersection.append(num)

print(intersection)