columnTitle = "ZY"

#print(len(columnTitle))

if len(columnTitle) < 2:
    for ch in columnTitle:
        ch = ord(ch)

        print(ch - 64)

elif len(columnTitle) > 1:
    result = 0
    for ch in columnTitle:
        result = result * 26 + (ord(ch) - 64)
    print(result)
        