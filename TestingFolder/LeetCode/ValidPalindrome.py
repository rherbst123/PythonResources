s = "   A man, a plan, a canal: Panama"


s = s.lower()
s = "".join(c for c in s if c.isalpha() or c.isdigit())
print(s)
print(s[::-1])

if s == s[::-1]:
    return True
else:
    return False


# forward = list(s)
# backward = list(s[::-1])


#print(forward,backward)