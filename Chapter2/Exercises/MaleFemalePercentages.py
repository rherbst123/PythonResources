""" Write a program that asks the user for the number of males and the number of females regis
tered in a class. The program should display the percentage of males and females in the class. """


males = float(input("How many men?:"))
females = float(input("How many women?:"))

total = (males + females)
print("Total amount of people:", format(int(total)))

#Do percentage calc
menPercentage = ((males / total) * 100.0)
womenPercentage = ((females / total) * 100.0)

print("Percentage of men is:", format(menPercentage, "0.2f"), "Female percentage:", format(womenPercentage, "0.2f"))