n = 50
m = 100

while n != 0:
    #74 , 15 = 15 74 % 15
    m, n = n, m % n
    
print(f"HCF is: {m}")
#print(m) 