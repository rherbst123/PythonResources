from itertools import combinations

nums = [366,809,6,792,822,181,210,588,344,618,341,410,121,864,191,749,637,169,123,472,358,908,235,914,322,946,738,754,908,272,267,326,587,267,803,281,586,707,94,627,724,469,568,57,103,984,787,552,14,545,866,494,263,157,479,823,835,100,495,773,729,921,348,871,91,386,183,979,716,806,639,290,612,322,289,910,484,300,195,546,499,213,8,623,490,473,603,721,793,418,551,331,598,670,960,483,154,317,834,352]

if len(nums) == 1:
    if nums[0] % 3 == 0:
        print(nums[0])
        exit  
    else:
        print(0)



for numbers in nums:
    all_sums = []
    for r in range(1, len(nums) + 1):
        for combo in combinations(nums, r):
            all_sums.append(sum(combo))

print(sorted(all_sums))
all_sums = sorted(all_sums)

all_sums = all_sums[::-1]

print(all_sums)

for sums in all_sums:
    if sums % 3 == 0:
        print(sums, "is divsible")
        break
    

print(all_sums)

