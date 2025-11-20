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


#Reverse Dictionary
reverse_codes = {v : k for k,v in codes.items()}

with open('Chapter9/Files/encrypted.txt', 'r') as encrypted_file:
    encrypted_message = encrypted_file.read()

decrypted_message = ''
for ch in encrypted_message:
    if ch in reverse_codes:
        decrypted_message += reverse_codes[ch]
    else:
        decrypted_message += ch

print("Decrypted Message:")
print(decrypted_message)

