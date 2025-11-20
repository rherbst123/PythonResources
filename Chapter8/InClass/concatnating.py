firstPart = "some"
secondPart = "thing"

combined = firstPart + secondPart
print(combined)

for i in range(5):
    combined += secondPart
print(combined)


combined = combined + "LAST BIT"
print(combined)

