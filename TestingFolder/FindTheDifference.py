s = "a" 
t = "aa"

hashmap = {}

for ch in s:
    if ch in hashmap:
        hashmap[ch] += 1
    else:
        hashmap[ch] = 1

for ch in t:
    if ch in hashmap:
        hashmap[ch] += 1
    else:
        hashmap[ch] = 1


for ch, count in hashmap.items():
    if count % 2 != 0:
        print(f"The extra character is: {ch}")


print(hashmap)

# for ch in t:
#     if ch not in s:
#         print(ch)
#     if ch in s:
#         print(ch)
    


