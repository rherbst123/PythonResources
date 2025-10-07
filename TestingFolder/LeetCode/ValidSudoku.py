board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]] 


        # Pseudocode for solving a Sudoku board using backtracking:

        # Define a function to check if placing a number at a given position is valid:
        #   - Check the row for duplicates
        #   - Check the column for duplicates
        #   - Check the 3x3 subgrid for duplicates

        # Define a recursive function to solve the board:
        #   - For each cell in the board:
        #       - If the cell is empty:
        #           - Try placing digits 1-9 in the cell:
        #               - If the placement is valid:
        #                   - Place the digit
        #                   - Recursively attempt to solve the rest of the board
        #                   - If solved, return True
        #                   - If not solved, reset the cell and try the next digit
        #           - If no digit fits, return False (backtrack)
        #   - If all cells are filled, return True (solved)

        # Call the recursive function to solve the board
