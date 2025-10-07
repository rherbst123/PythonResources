import random

# Global constants are typically written in ALL_CAPS
PI = 3.14159
MAX_CONNECTIONS = 100
DEFAULT_NAME = "Riley"
DEFAULT_AGE = 24

def show_me(name=DEFAULT_NAME, age=DEFAULT_AGE):
    # Constants don't need the 'global' keyword if you're only reading them
    print(f"Pi is approximately {PI}")
    print(f"Name: {name}, Age: {age}")
    print(f"Maximum connections allowed: {MAX_CONNECTIONS}")

def main():
    # Since these are constants, we shouldn't modify them
    # Just read and use them
    show_me()
    show_me("Alice", 30)

if __name__ == "__main__":
    main()


