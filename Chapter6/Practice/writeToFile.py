# Open and read a text file
file_path = "Chapter6/Practice/test.txt"  # Replace with your file path

# First read the file
try:
    with open(file_path, 'r') as file:
        # Read the entire file
        content = file.read()
        print(content)
        
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    exit()
except IOError:
    print("Error: An I/O error occurred while reading the file.")
    exit()

# Get user input
new_line = input("Enter the line you want to add: ")

# Append the new line to the file
try:
    with open(file_path, 'a') as file:
        file.write('\n' + new_line)
        print("Line successfully added to the file.")
        
except IOError:
    print("Error: An I/O error occurred while writing to the file.")