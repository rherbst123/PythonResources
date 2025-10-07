def StringAndNumber(string, number):
    string = string + " Another Part"
    number = number + 5
    return string, number

def StringAndNumber2(string, number):
    string = string + " Another Part plus more"
    number = number * 5
    return string, number


def main():
    string = "This is a String"
    number = 5
    stringStart, numberStart = StringAndNumber(string, number)

    print(stringStart)

    print(numberStart)

    string, number = StringAndNumber2(string, number)

    print(string)


    print(number)

main()