text = "leet code"
brokenLetters = "e"

words = []
letters = []
for ch in brokenLetters:
    letters.append(ch)

for word in text.split():
    words.append(word)

print(words, letters)

final = 0

for word in words:
    can_type = True
    for letter in letters:
        if letter in word:
            print(letter ,"in", word)
            can_type = False
            break
    if can_type:
        final += 1





print(final)


