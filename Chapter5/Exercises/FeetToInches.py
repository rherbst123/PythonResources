"""  10. Feet to Inches
 One foot equals 12 inches. Write a function named feet_to_inches that accepts a number 
of feet as an argument and returns the number of inches in that many feet. Use the function 
in a program that prompts the user to enter a number of feet then displays the number of 
inches in that many feet """



def main():
    feet = int(input("How many feet?: "))

    inches = feet_to_inches(feet)

    if feet == 1:
        print(f"{feet} foot is {inches}, inches")
    if feet > 1:
        print(f"1{feet} feet is {inches}, inches")
    return 0 


def feet_to_inches(feet):
    inches = feet * 12
    return inches

main()

