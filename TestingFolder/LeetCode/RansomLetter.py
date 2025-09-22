ransomNote = "fffbfg" 
magazine = "effjfggbffjdgbjjhhdegh"

counts1 = {}
counts2 = {}

for ch in ransomNote:
    counts1[ch] = counts1.get(ch, 0) + 1
for ch in magazine:
    counts2[ch] = counts2.get(ch, 0) + 1

can_construct = True
for ch in counts1:
    if counts1[ch] > counts2.get(ch, 0):
        can_construct = False
        break

if can_construct:
    print("True")
else:
    print("False")