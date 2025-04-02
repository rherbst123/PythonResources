#  7. Stadium Seating
#  There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost 
# $15, and Class C seats cost $10. Write a program that asks how many tickets for each class 
# of seats were sold, then displays the amount of income generated from ticket sales

def costCalculator(a,b,c):
    classA = a * 20
    classB = b * 15
    classC = c * 10
    total = classA + classB + classC
    return classA,classB,classC,total


a = int(input("Enter number of Class A tickets sold: "))
b = int(input("Enter number of Class B tickets sold: "))
c = int(input("Enter number of Class C tickets sold: "))
        


cost_a, cost_b, cost_c, total = costCalculator(a, b, c)

print(f"Class A Sales: ${cost_a}")
print(f"Class B Sales: ${cost_b}")
print(f"Class C Sales: ${cost_c}")
print(f"Total Sales: ${total}")


    

