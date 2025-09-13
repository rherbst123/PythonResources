# 5.  Mass and Weight
# Scientists  measure  an  object’s  mass  in  kilograms  and  its  weight  in  newtons.  If  you  know  
# the amount of mass of an object in kilograms, you can calculate its weight in newtons with 
# the following formula:
# weight = mass X 9.8
# Write a program that asks the user to enter an object’s mass, then calculates its weight. If 
# the object weighs more than 500 newtons, display a message indicating that it is too heavy. 
# If the object weighs less than 100 newtons, display a message indicating that it is too light


mass = float(input("Enter the objects mass: "))

weight = mass * 9.8

print(f"The objects mass is: {mass} which comes out to a weight of: {format(weight, "0.2f")} newtons")

if weight > 500.0:
    print("The weight is too damn much!")
if weight < 100.0:
    print("The weight is too damn little!")

if weight < 500.0 and weight > 100.0:
    print("Good to go!")