s = "  hello world  "

s = s.split()

new = ""
print(s)

s = s[::-1]
print(s)
for word in s:
    new += word + ' '


print(new.rstrip())
