# 11.   Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase. Convert the sentence to a string in which 
# the words are separated by spaces, and only the first word starts with an uppercase letter. For 
# example the string “StopAndSmellTheRoses.” would be converted to “Stop and smell 
# the roses.”

def separator(user_string):
    #Create new string
    new_string = ""
    #For each character in input
    for ch in user_string:
        #if the ch is an uppercase
        if ch.isupper():

            #print(ch)
            #Add a Space to the new String
            new_string += " "
            #Add each character to the string (See how its NOT in the if statement.)
        new_string += ch
        #Give us the new string
    return new_string


def main():
    #Get input and run function
    user_string = input("Enter a sentence with each word capitolized and no spaces: ")
    new_string = separator(user_string)
    print(new_string)

main()