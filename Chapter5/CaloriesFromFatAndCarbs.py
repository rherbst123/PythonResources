# 6. Calories from Fat and Carbohydrates
#  A nutritionist who works for a fitness club helps members by evaluating their diets. As part 
# of her evaluation, she asks members for the number of fat grams and carbohydrate grams 
# that they consumed in a day. Then, she calculates the number of calories that result from 
# the fat, using the following formula:
#  calories from fat 5 fat grams x 9
# Programming Exercises 
# 303
#  Next, she calculates the number of calories that result from the carbohydrates, using the 
# following formula:
#  calories from carbs 5 carb grams x 4
#  The nutritionist asks you to write a program that will make these calculations


def calsFromFat(fatGrams):
    caloriesFromFat = fatGrams * 9
    return caloriesFromFat

def calsFromCarbs(carbGrams):
    caloriesFromCarbs = carbGrams * 4
    return caloriesFromCarbs


fatGrams = int(input("How many fatGrams?: "))
carbGrams = int(input("How many carbGrams?: "))

print(f"Total calories from fat: {calsFromFat(fatGrams)}")
print(f"Total calories from carbs: {calsFromCarbs(carbGrams)}")

