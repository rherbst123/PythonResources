# 12.   Pig Latin
# Write a program that accepts a sentence as input and converts each word to “Pig Latin.” In 
# one version, to convert a word to Pig Latin, you remove the first letter and place that letter 
# at the end of the word. Then, you append the string “ay” to the word. Here is an example:
# English: I SLEPT MOST OF THE NIGHT
# Pig Latin: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY


def pig_latin(user_string):
    #Split up the input
    words = user_string.split()
    #New String
    new_string= ""
    #Iterate through each word in string
    for word in words:
        #Take Every word - the first letter. Add the first letter to the end of the word and add an AY
        word = word[1:] + word[0] + "AY"
        #Add each "New" word to the list
        new_string += word + " "
    #Return the list
    return new_string

def main():
    #Get Info
    user_string = "I SLEPT MOST OF THE NIGHT"
    #user_string = input("Enter a phrase: ")
    new_string = pig_latin(user_string)
    print(new_string)
main()


