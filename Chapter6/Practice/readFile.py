def read_file():
    # Ask user for file path
    file_path = "input"

    try:
        with open(file_path, 'r') as file:
            # Read the entire file
            content = file.read()
            print("\nFile contents:")
            print("-" * 50)
            print(content)
            print("-" * 50)
        
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print("Error: An I/O error occurred while reading the file.")

if __name__ == "__main__":
    read_file()