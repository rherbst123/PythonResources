"""  A cookie recipe calls for the following ingredients:
 • 1.5 cups of sugar
 • 1 cup of butter
 • 2.75 cups of flour
 The recipe produces 48 cookies with this amount of the ingredients. Write a program that 
asks the user how many cookies he or she wants to make, then displays the number of cups 
of each ingredient needed for the specified number of cookies. """


cookies = float(input("how many cookies do you want to make?: "))


cupsSugarPer = 1.5 / 48.0

cupsButterPer = 1.0 / 48.0

cupsFlowerPer = 2.75 / 48.0

#print("For each cookie it takes:", cupsSugarPer, cupsButterPer, cubsFlowerPer)

cupsSugar = cupsSugarPer * cookies
cupsButter = cupsButterPer * cookies
cupsFlower = cupsFlowerPer * cookies

print("You will need:", format(cupsSugar, "0.2f"), "Cups of sugar",
      format(cupsButter, "0.2f"), "Cups of Butter,", 
      format(cupsFlower, "0.2f"), "cups of Flower")