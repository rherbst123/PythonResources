
text = '''John Doe,25,New York
Jane Smith,30,Los Angeles
Bob Wilson,45,Chicago'''

# Process each line
for line in text.splitlines():
    # Split the line by comma
    name, age, city = line.split(',')
    
    # Print formatted output
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print("-" * 20)