strs = ["flower", "flow", "flight"]

#if not in the list of words print ""
if not strs:
    print("")
else:
    #starts at first word and assigns prefix to first word
    prefix = strs[0]
    print(prefix)
    #For words in the string starting with the second one
    for word in strs[1:]:
        #While the word is not 
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            print(prefix)
            if not prefix:
                break
    print(prefix)