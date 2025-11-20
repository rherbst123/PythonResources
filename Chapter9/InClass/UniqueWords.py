# 4.  Unique Words
# Write a program that opens a specified text file then displays a list of all the unique words 
# found in the file

with open("Chapter9/Files/uniqueWords2.txt", 'r') as file:
    message = file.read()

print(message)

words = message.split()
print(words)

uniqueWords = {}

#print(uniqueWords)

for word in words:
    uniqueWords[word] = True

print("List of unique words")
for word in uniqueWords:
    print(word)


