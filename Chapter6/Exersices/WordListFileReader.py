#  8. Word List File Reader
#  This exercise assumes you have completed the Programming Exercise 7, Word List File 
# Writer. Write another program that reads the words from the file and displays the follow
# ing data:
#  •	The	number	of	words	in	the	file.
#  •	The	longest	word	in	the	file.
#  •	The	average	length	of	all	of	the	words	in	the	file.

def main():
    words = open("Chapter6\\words.txt", "r")
    amountOfWords = 0
    longestWord = ""
    totalWordLength = 0

    for line in words:
        word = line  # Remove any leading/trailing whitespace or newline characters
        amountOfWords += 1
        totalWordLength += len(word)
        
        if len(word) > len(longestWord):
            longestWord = word

    averageWordLen = totalWordLength / amountOfWords
    averageWordLen = format(averageWordLen,"0.0f") 

    print("Number of words:", amountOfWords)
    print("Longest word:", longestWord)
    print("Average word length:", averageWordLen)



main()