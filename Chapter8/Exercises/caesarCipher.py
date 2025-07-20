# 15.   Caesar Cipher 
# A “Caesar Cipher” is a simple way of encrypting a message by replacing each letter with a 
# letter a certain number of spaces up the alphabet. For example, if shifting the message by 
# 13 an A would become an N, while an S would wrap around to the start of the alphabet to 
# become an F.
# Write a program that asks the user for a message (a string) and a shift amount (an integer). 
# The values should be passed to a function that accepts a string and an integer as arguments, 
# and returns a string representing the original string encrypted by shifting the letters by the 
# integer. For example, a string of “BEWARE THE IDES OF MARCH” and an integer of 13 
# should result in a string of “ORJNER GUR VQRF BS ZNEPU”.


#Im not doing functions you get the idea...

user_string = input("Enter a word: ")
shift = int(input("Enter a number of the character shift: "))


numbers = []
new_numbers = []
new_word_chars = []

new_word = ""

for ch in user_string:
    ch = ord(ch)
    numbers.append(ch)
#print(numbers)

for numb in numbers:
    numb = numb + shift
    # If the shifted character code goes past 'z' for lowercase or past 'Z' for uppercase (while keeping the original case), subtract 26 to wrap it around to the start of the alphabet.
    if (numb > ord('z') and chr(numb - shift).islower()) or (numb > ord('Z') and chr(numb - shift).isupper()):
        numb -= 26
    new_numbers.append(numb)
#print(new_numbers)

for numb in new_numbers:
    letters = chr(numb)
    new_word_chars.append(letters)
new_word = ''.join(new_word_chars).replace('-', ' ')
print(new_word)
    



