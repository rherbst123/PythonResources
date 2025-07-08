# 6.  Average Number of Words
# If you have downloaded the source code from the Premium Companion Website you will 
# find a file named text.txt in the Chapter 08 folder. The text that is in the file is stored 
# as one sentence per line. 
# Write a program that reads the file’s contents and calculates the  average number of words per sentence






def main():
    total = 0
    with open("Chapter8/Files/text.txt",'r') as file:
        lines = sum(1 for _ in file)
        file.close()
    with open("Chapter8/Files/text.txt",'r') as file:
       
        for line in file:
            length = int(len(line.strip()))
            total += length
        #print(total)
        #print(lines)
        print(f"The Average length of the sentences in the list are: {total//lines} characters")
main()