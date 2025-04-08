#  3. Line Numbers
#  Write a program that asks the user for the name of a file. The program should display the 
# contents of the file with each line preceded with a line number followed by a colon. The 
# line numbering should start at 1.


def displayFile(text):
    start = 1
    text = open(text, "r")
    #print(text)
    for line in text:
        print(f"{start}; {line}", end="")
        start += 1

#Here is an example of something that LOOKS RIGHT but is not
""" def displayFile(text):
    start = 1
    text = open(text,"r")
    #print(text)
    for line in text:
        info = text.readline() #Our culprit
        print(f"{start}; {info}", end="")
        start += 1 """


def main():
    text = "Chapter6//numbers.txt"
    displayFile(text)

main()

