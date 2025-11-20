word = "aisudhkasudhaskjhaskjhasdkjhadskjhdsa"

#print(len(word))
firstCh = 0
secondCh = 0
for ch in word:
    firstCh += 1
    if ch == "u":
        break

for ch in word:
    secondCh += 1
    if ch == "k":
        break
print(firstCh, secondCh)

print(word[firstCh -1 :secondCh])