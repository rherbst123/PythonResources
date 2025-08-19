# Define the string to search within
haystack = "sadbutsad"

# Define the substring to search for
needle = "sad"

# Initialize the starting index for searching
start = 0

# Begin an infinite loop to find all occurrences of 'needle' in 'haystack'
while True:
    # Search for 'needle' in 'haystack' starting from index 'start'
    # Returns the lowest index where 'needle' is found, or -1 if not found
    idx = haystack.find(needle, start)
    
    # If 'needle' is not found, exit the loop
    if idx == -1:
        break
    
    # Print the index where 'needle' was found
    print(idx)
    
    # Update 'start' to one position after the current found index
    # This allows searching for subsequent occurrences of 'needle'
    start = idx + 1