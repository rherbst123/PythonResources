# get random number generator with "random" import
# 3 Guesses and after 3 wrong guesses it says "loser!!!"
# depending on guess says "High or Low"
# 1 - 20 range of numbers to guess

import random

def NumberGenerator():
    person_guesses = int(input("How many guesses do you need: "))
    #print(person_guesses)
    if person_guesses < 1 and person_guesses > 5:
        magicNumber = random.randint(1, 20)
    elif person_guesses < 6 and person_guesses > 10:
        magicNumber = random.randint(1, 30)
    else:
        magicNumber = random.randint(1, 10)

    #magicNumber = random.randint(1, 10)
    #print(magicNumber)
    return magicNumber, person_guesses

def Guesser(magicNumber, person_guesses):
    guesses = 0
    
    
    while guesses != person_guesses:
        guess = int(input("Make a Guess!: (between 1 and 20): "))
        #Correct guess logic works good
        if guess == magicNumber:
            print(f"YAY!!!! you won, the magic number was: {magicNumber}")
            break
        elif guess != magicNumber:
            print("Not the right answer keep guessing")
            
            guesses += 1
            person_guesses -= 1
            if guess > magicNumber:
                print("Your guess was too high! Think a lower number...")
            if guess < magicNumber:
                print("Your guess was too Low! Think a higher number...")

            if guess == (magicNumber + 1) or guess == (magicNumber-1):
                print ("So Close!")
        if person_guesses == 0:
            print("You LOSE!!")
            break
        print(f"You have {person_guesses} left")
            
def main():
    print("Welecome to the number Guesser!!!")

    magicNumber, person_guesses = NumberGenerator()
    Guesser(magicNumber, person_guesses)

main()