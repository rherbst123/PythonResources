import time
import sys
sys.set_int_max_str_digits(0)

x = 0
y = 1

n = int(input("Number:"))
for i in range(n):
    start = time.time()
    z = x + y
    x = y
    y = z
    end = time.time()
    length = end - start
    
print(z)
lengthF = "{:.6f}".format(length)
print("Calculation time: ", lengthF)