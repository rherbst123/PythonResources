# 7.  Character Analysis
# If you have downloaded the source code you will find a file named text.txt in the Chapter 08 
# folder. Write a program that reads the file’s contents and determines the following:
# •  The number of uppercase letters in the file
# •  The number of lowercase letters in the file
# •  The number of digits in the file
# •  The number of whitespace characters in the file


def main():
    uppers = 0
    lowers = 0
    digits = 0
    whiteSpaces = 0

    #Look in Chapter8 > BookStuff > TestingStrings.py
    with open("Chapter8/Files/text.txt", 'r') as file:
        for line in file:
            for ch in line:
                if ch.isalnum():
                    digits += 1
                if ch.upper():
                    uppers += 1
                if ch.lower():
                    lowers += 1
                if ch == " ":
                    whiteSpaces += 1

        print(uppers,lowers,digits,whiteSpaces)
                

main()