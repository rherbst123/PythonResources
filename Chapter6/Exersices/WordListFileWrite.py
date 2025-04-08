#  7. Word List File Writer
#  Write a program that asks the user how many words they would like to write to a file, and 
# then asks the user to enter that many words, one at a time. The words should be written 
# to a file.

def main():
    wordsNum = int(input("How many words would you like to write to file?: "))

    textFile = open("Chapter6\\words.txt", "w")
    index = 1
    for i in range(wordsNum):
        word = input(f"Enter a word[{index}]: ")
        textFile.write(word + "\n")
        index += 1
    textFile.close()

    textFile = open("Chapter6\\words.txt", "r")
    for line in textFile:
        print(line, end="")

main()