# 9.  Vowels and Consonants
# Write  a  program  with  a  function  that  accepts  a  string  as  an  argument  and  returns  the  
# number of vowels that the string contains. The application should have another function 
# The Vowels and Consonants problem
# that accepts a string as an argument and returns the number of consonants that the string 
# contains. The application should let the user enter a string, and should display the number 
# of vowels and the number of consonants it contains.


def vowels_consonants(user_string):
    numVowels = 0
    numConsonants = 0
    vowels = ["A","E","I","O","U"]
    string = user_string.upper()
    for ch in string:
        if ch in vowels:
            numVowels += 1
        else:
            numConsonants += 1
    return numConsonants, numVowels




def main():
    user_string = input("Enter a string to count stuff about it: ")
    numConsonants, numVowels = vowels_consonants(user_string)
    print(f"The string contains {numVowels} vowels and {numConsonants} consonants.")

main()



