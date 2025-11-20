nums = [3,8,7,8,7,5]
k = 2
x = 2

numbers = {}

final = []

for i in range(len(nums) - k + 1):
    window = nums[i:i+k]
    freq = {}
    for num in window:
        freq[num] = freq.get(num, 0) + 1
    
    sorted_freq = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
    top_x = sorted_freq[:x]
    
    x_sum = sum(num * count for num, count in top_x)
    numbers[i] = x_sum
    final.append(x_sum)
return final

