#  9. Exception Handing
#  Modify the program that you wrote for Exercise 6 so it handles the following exceptions:
#  •	It should handle any IOError exceptions that are raised when the file is opened and data 
# is read from it.
#  •	It	should	handle	any	ValueError exceptions that are raised when the items that are read 
# from the file are converted to a number


def numberStuff(numbers):
    total = 0.0
    size = 0
    try:
        with open(numbers, "r") as file:
            for line in file:
                try:
                    number = float(line)
                    total += number
                    size += 1
                except ValueError:
                    print(f"ValueError: Could not convert '{line.strip()}' to float. Skipping.")
    except IOError as err:
        print(f"IOError: {err}")
        return None

    if size == 0:
        print("No valid numbers to average.")
        return None

    avg = total / size
    return avg

def main():
    numbers = "Chapter6\\numbers.txt"
    avg = numberStuff(numbers)
    if avg is not None:
        print(f"average {format(avg, '0.2f')}")

main()