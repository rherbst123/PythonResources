


def main():
    letterCount = 0

    sentence = input("Enter a bunch of letters or a sentence: ")

    
    for ch in sentence:
        if ch == "l" or ch == "m":
            letterCount += 1

    print(f"The total amount of L's or M's in the input is: {letterCount}")

main()