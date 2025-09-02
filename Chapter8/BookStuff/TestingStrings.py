
def main():
    string_input = input("Hello Please say something: ")

    print("This is some stuff about the string:")
    print(45*"=")

    if string_input.isalnum():
        print("String is AlphaNumeric")

    if string_input.isdigit():
        print("String contains only digits")

    if string_input.isalpha():
        print("The string is only letters")

    if string_input.islower():
        print("All Lowers")

    if string_input.isupper():
        print("String is all uppers")


main()
