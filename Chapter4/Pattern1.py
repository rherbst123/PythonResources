""" 14. Write a program that uses nested loops to draw this pattern:
 *******
 ******
 *****
 ****
 ***
 **
 * """
n = 100
star = "*"
size = n
for i in range(n):
    print(size*star)
    size -= 1