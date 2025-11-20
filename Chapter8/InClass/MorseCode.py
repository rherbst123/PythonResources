# 4.  Morse Code Converter
# Morse  code  is  a  code  where  each  letter  of  the  English  alphabet,  each  digit,  and  various  
# punctuation characters are represented by a series of dots and dashes. Table 8-4 shows part 
# of the code.

def conversion(message):
      legend = [
        ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'),
        ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'), ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'),
        ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'), ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
        ('Y', '-.--'), ('Z', '--..'), ('1', '.----'), ('2', '..---'), ('3', '...--'), ('4', '....-'), ('5', '.....'),
        ('6', '-....'), ('7', '--...'), ('8', '---..'), ('9', '----.'), ('0', '-----'), (',', '--..--'), ('.', '.-.-.-'),
        ('?', '..--..'), (' ', '/')
            ]
      
      finalMessage = []
      for char in message.upper():
        morse_char = '?'
            #In the double these columns are named letter and code. seperated by a ,
        for letter, code in legend:
            if letter == char:
                morse_char = code
                break
        finalMessage.append(morse_char)
        print(" ".join(finalMessage))
        
def main():
    message = input("Enter a message to convert: ")
    conversion(message)

main()
