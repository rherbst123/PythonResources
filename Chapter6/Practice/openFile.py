# Open and read a text file
file_path = "Chapter6/Practice/test.txt"  # Replace with your file path

try:
    with open(file_path, 'r') as file:
        # Read the entire file
        content = file.read()
        print("File contents:")
        print(content)
        
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except IOError:
    print("Error: An I/O error occurred while reading the file.")