#  8. Average Word Length
#  Write a program with a loop that repeatedly asks the user to enter a word. The user should 
# enter nothing (press Enter without typing anything) to signal the end of the loop. Once the 
# loop ends, the program should display the average length of the words entered, rounded to 
# the nearest whole number.
words = []
sizeWords = []
total = 0

word = input("Enter a word: ")
words.append(word)
while word != "":
    word = input("Enter a word: ")
    words.append(word)
    
words.remove("")
print(words)
    

size = len(words)
#print(size)
for i in range(size):
    #print(words[i])
    #print(len(words[i]))
    total += len(words[i])
print("Total characters: ", total)
average = total / size
print("Average length of words is: ", average )


    
    