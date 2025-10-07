nums1 = [1,2,2,1]
nums2 = [2,2]

result = []

if len(nums2) > len(nums1):
    nums1 ,nums2 = nums2 , nums1


for number in nums1:
    if number in nums2:
        result.append(number)
        nums2.remove(number)
print(result)
        