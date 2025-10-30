word = "letters"

letters = {}

for ch in word:
    if ch in letters:
        letters[ch] += 1
    else:
        letters[ch] = 1

print(letters)


for ch in word:
    if letters[ch] > 1:
        print(ch)
        break