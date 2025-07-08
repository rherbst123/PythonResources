# 10.   Most Frequent Character
# Write a program that lets the user enter a string and displays the character that appears most 
# frequently in the string.

def counter(user_string):
    # get a counter and a string going
    max_chars = 0
    most_char = ''
    #for each character in the input string
    for ch in user_string:
        # if the character is NOT a space
        if ch != ' ':
            #Get the number of each character 
            numChars = user_string.count(ch)
            #if the number of that char is greater than the previous max char replace it
            if numChars > max_chars:
                #the number of the chars becomes the new max
                max_chars = numChars
                #the number of chars is assigned to the identififer for the char
                most_char = ch
        return most_char, max_chars






def main():
    user_string = input("Enter a string: ")
    most_char, max_chars = counter(user_string)
    print(f"The most frequent char is {most_char} with it appearing {max_chars} times")
main()