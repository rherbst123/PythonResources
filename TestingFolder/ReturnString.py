def returnString():
    userInput = input("Enter your name: ")
    return userInput


def main():
    userInput = returnString()
    print(f"Hello {userInput}")

main()