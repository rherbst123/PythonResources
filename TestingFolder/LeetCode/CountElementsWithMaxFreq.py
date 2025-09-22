# You are given an array nums consisting of positive integers.

# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

# The frequency of an element is the number of occurrences of that element in the array.

#nums = [1,2,2,3,1,4]

nums = [1,2,3,4,5]

counts = {}

for number in nums:
    counts[number] = counts.get(number, 0) + 1

    max_count = max(counts.values())
    max_freq_elements = [count for count in counts.values() if count == max_count]
    total_sum = sum(max_freq_elements)

print(total_sum)

return total_sum