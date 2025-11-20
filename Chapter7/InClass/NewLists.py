def adding(items):
    total = sum(items)

    return total

def main():
    items = [3,5,3,6,7,4,5,3,5]

    total = adding(items)
    final =  total / len(items)
    print(final)


main()