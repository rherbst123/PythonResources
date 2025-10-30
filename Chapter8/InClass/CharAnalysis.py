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
    whiteSpace = 0

    with open("/home/riley/Documents/GitHub/RileyPython/Chapter8/Files/text.txt", 'r') as words:
        for line in words:
            for ch in line:
                if ch.isupper():
                    uppers += 1
                if ch.islower():
                    lowers += 1
                if ch.isdigit():
                    digits += 1
                if ch.isspace():
                    whiteSpace += 1 

        print(uppers,lowers,digits,whiteSpace)
                


main()