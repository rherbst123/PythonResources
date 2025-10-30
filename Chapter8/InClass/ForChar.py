word = "Hello"

print(word[1:4])

print(len(word))


counter = 0

for ch in word:
    if ch == "l":
        counter += 1

print(counter)