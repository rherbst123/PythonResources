s = "acb"
t = "ahbgdc"

result = True
t_iter = iter(t)
for ch in s:
    if ch not in t_iter:
        result = False
        break

print("True" if result else "False")
