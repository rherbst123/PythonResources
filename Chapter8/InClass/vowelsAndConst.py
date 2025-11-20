# 9.  Vowels and Consonants
# Write  a  program  with  a  function  that  accepts  a  string  as  an  argument  and  returns  the  
# number of vowels that the string contains. The application should have another function

def main():
    userMessage = input("Enter some garbage: ")

    numVowels = 0
    numConsonats = 0

    vowels = ["A","E","I","O","U"]
    userMessage = userMessage.upper()

    for ch in userMessage:
        if ch in vowels:
            numVowels += 1
        else:
            numConsonats += 1
    print(numVowels, numConsonats)

main()