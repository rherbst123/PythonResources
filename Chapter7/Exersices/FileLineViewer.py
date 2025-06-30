# 12.  File Line Viewer
# Write a program that asks the user for the name of a file. The program should read all of 
# the file’s data into a list and display the number of lines of data that the file contains, and 
# then ask the user to enter the number of the line that they want to view. The program should 
# display the specified line.
# The program should handle the following exceptions by displaying an error message:
# •  IOError  exceptions  that  are  raised  when  the  specified  filename  cannot  be  found  or  
# opened.
# •  ValueError exceptions that are raised when a non-integer value is given as a line number.
# •  IndexError exceptions that are raised when the line number is outside the range of the 
# data list

theFile = open("Chapter7/Extra_Files/BoyNames.txt", 'r')

try:
    # Read all lines into a list
    lines = theFile.readlines()
    print(f"The file contains {len(lines)} lines.")
    
    # Ask the user for the line number they want to view
    line_number = int(input("Enter the line number you want to view: "))
    
    # Display the specified line
    print(lines[line_number - 1].strip())
except IOError:
    print("Error: The file could not be found or opened.")
except ValueError:
    print("Error: Please enter a valid integer for the line number.")
except IndexError:
    print("Error: The line number is out of range.")
finally:
    theFile.close()
