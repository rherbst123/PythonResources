# 3.  File Encryption and Decryption
# Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For 
# example:
# codes = { ‘A’ : ‘%’, ‘a’ : ‘9’, ‘B’ : ‘@’, ‘b’ : ‘#’, etc . . .}
# Using  this  example,  the  letter  A  would  be  assigned  the  symbol  %,  the  letter  a  would  be  
# assigned the number 9, the letter B would be assigned the symbol @, and so forth.
# The  program  should  open  a  specified  text  file,  read  its  contents,  then  use  the  dictionary  
# to write an encrypted version of the file’s contents to a second file. Each character in the 
# second file should contain the code for the corresponding character in the first file.
# Write  a  second  program  that  opens  an  encrypted  file  and  displays  its  decrypted  contents  
# on the screen.


codes = {
    'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '!', 'c': '1',
    'D': '^', 'd': '2', 'E': '&', 'e': '3', 'F': '*', 'f': '4',
    'G': '(', 'g': '5', 'H': ')', 'h': '6', 'I': '-', 'i': '7',
    'J': '_', 'j': '8', 'K': '=', 'k': '0', 'L': '+', 'l': '[',
    'M': '{', 'm': ']', 'N': '}', 'n': '|', 'O': ':', 'o': ';',
    'P': '"', 'p': "'", 'Q': '<', 'q': ',', 'R': '>', 'r': '.',
    'S': '?', 's': '/', 'T': '~', 't': '`', 'U': 'z', 'u': 'x',
    'V': 'c', 'v': 'v', 'W': 'b', 'w': 'n', 'X': 'm', 'x': 'a',
    'Y': 's', 'y': 'd', 'Z': 'f', 'z': 'g', ' ': 'h', '\n': 'j'
}


with open('Chapter9/Files/toEncrypt.txt', 'r') as file:
    message = file.read()

# Encrypt the message and write to a file
with open('Chapter9/Files/encrypted.txt', 'w') as encrypted_file:
    encrypted_message = ''
    for ch in message:
        if ch in codes:
            encrypted_message += codes[ch]
        else:
            encrypted_message += ch
    encrypted_file.write(encrypted_message)

# Print the encrypted message
print("Encrypted Message:")
print(encrypted_message)

# Create a reverse dictionary for decryption
reverse_codes = {v: k for k, v in codes.items()}

# Read the encrypted file and decrypt its contents
with open('Chapter9/Files/encrypted.txt', 'r') as encrypted_file:
    encrypted_message = encrypted_file.read()

decrypted_message = ''
for ch in encrypted_message:
    if ch in reverse_codes:
        decrypted_message += reverse_codes[ch]
    else:
        decrypted_message += ch

# Print the decrypted message
print("Decrypted Message:")
print(decrypted_message)