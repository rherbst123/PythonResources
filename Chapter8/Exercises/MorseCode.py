# 4.  Morse Code Converter
# Morse  code  is  a  code  where  each  letter  of  the  English  alphabet,  each  digit,  and  various  
# punctuation characters are represented by a series of dots and dashes. Table 8-4 shows part 
# of the code.
# Write a program that asks the user to enter a string, then converts that string to Morse code

def conversion(message):
    
    legend = [
        ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'),
        ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'), ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'),
        ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'), ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
        ('Y', '-.--'), ('Z', '--..'), ('1', '.----'), ('2', '..---'), ('3', '...--'), ('4', '....-'), ('5', '.....'),
        ('6', '-....'), ('7', '--...'), ('8', '---..'), ('9', '----.'), ('0', '-----'), (',', '--..--'), ('.', '.-.-.-'),
        ('?', '..--..'), (' ', '/')
            ]
    
    morse_code = []
    for char in message.upper():
        morse_char = '?'
            #In the double these columns are named letter and code. seperated by a ,
        for letter, code in legend:
            if letter == char:
                morse_char = code
                break
        morse_code.append(morse_char)
    print(" ".join(morse_code))




def main():
    message = input("Enter Something to convert: ")
    conversion(message)

main()



