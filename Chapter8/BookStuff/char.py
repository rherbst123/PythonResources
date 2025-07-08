


def main():
    letterCount = 0

    sentence = input("Enter a bunch of letters or a sentence: ")
    sentence = sentence.upper()
    
    for ch in sentence:
        if ch == "L" or ch == "M":
            letterCount += 1

    print(f"The total amount of L's or M's in the input is: {letterCount}")

main()