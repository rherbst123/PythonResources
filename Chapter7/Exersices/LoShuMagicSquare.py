# 11.   Lo Shu Magic Square
# The Lo Shu Magic Square is a grid with 3 rows and 3 columns, shown in Figure 7-18. The 
# Lo Shu Magic Square has the following properties:
# •  The grid contains the numbers 1 through 9 exactly.
# •  The sum of each row, each column, and each diagonal all add up to the same number. 
# This is shown in Figure 7-19.
# In a program you can simulate a magic square using a two-dimensional list. Write a func-
# tion that accepts a two-dimensional list as an argument and determines whether the list is 
# a Lo Shu Magic Square. Test the function in a program.



square = [[4,9,2],
          [3,5,7],
          [8,1,6]]


lineTotal = 0
line = 1
checker = 0
Rows = False
column_sum = 0
columns = False
checker2 = 0


diag1 = 0
diag2 = 0
# #Finding Sums for each line
for lines in square:
    #print(lines)
    print(f"The sum of Line {line}: {sum(lines)}")
    line += 1
    checker += sum(lines)
    #print(checker)
if checker / 3 == sum(lines):
    print("Rows Are Good")
    Rows = True
else:
    print("Rows Are Bad!")


#Finding Sums for all Columns!
for i in range(len(square[0])):
    column_sum = sum(row[i] for row in square)
    print(f"The sum of Column {i + 1}: {column_sum}")
checker2 += column_sum
if checker / 3 == sum(row[i] for row in square):
    print("The Colummns are Good")
    columns = True
else:
    print("The Columns are Bad")




# find sums for diagianal?
# Print the diagonal numbers
print("Diagonal numbers Top to Bottom:")
for i in range(len(square)):
    #print(square[i][i], end=' ')
    diag1 += square[i][i]
print(f"Diagonal (Top left to bottom right): {diag1}")
if diag1 == 15:
    diagChe1 = True
else: 
    diagChe1 = False



for i in range(len(square)):
    #print(square[i][len(square) - 1 - i], end=' ')
    diag2 += square[i][len(square) - 1 - i]
print(f"Diagonal (Bottom left to top right): {diag1}")
if diag2 == 15:
    diagChe2 = True
else: 
    diagChe2 = False


if Rows == True and columns == True and diagChe1 == True and diagChe2 == True:
    print("Its a Square!")
else:
    print("Not a Square")




    
    


