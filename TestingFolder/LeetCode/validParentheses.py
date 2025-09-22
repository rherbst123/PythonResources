s = "[)"

pairs = []




counter = 0
for parentheses in s:
    if parentheses == "{":
        counter += 1
        if parentheses == "}":
            counter -= 1
    if  parentheses == "[":
        if parentheses == "]":
            counter -=1
    if  parentheses == "(":
        if parentheses == ")":
            counter -=1
    
        counter -= 1

print(counter)
if counter == 0:
    print("Balanced")
else:
    print("UnBalanced")
    

