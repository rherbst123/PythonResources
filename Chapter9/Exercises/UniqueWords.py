# 4.  Unique Words
# Write a program that opens a specified text file then displays a list of all the unique words 
# found in the file.
# Hint: Store each word as an element of a set.


with open(r'/home/riley/Documents/GitHub/RileyPython/Chapter9/Files/UniqueWords.txt', 'r') as file:
    message = file.read()

words = message.split()
# Create an empty set to store unique words
uniqueWords = {}

# Add each word to the dictionary
for word in words:
    uniqueWords[word] = True
    
# Print all unique words
print("List of unique words found in the file:")
for word in uniqueWords:
    print(word)