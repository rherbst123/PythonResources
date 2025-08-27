# matrix = [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]



# countOnes = 0

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[i][j] == 1:
#             countOnes += 1
# print(countOnes)


# countTwos = 0

# for i in range(len(matrix) - 1):
#     for j in range(len(matrix[0]) - 1):

#         if matrix[i][j] == 1 and matrix[i][j + 1] == 1 and matrix[i + 1][j] == 1 and matrix[i + 1][j + 1] == 1:
#             countTwos += 1

# print(countTwos)



# countThrees = 0

# for i in range(len(matrix) - 2):
#     for j in range(len(matrix[0]) - 2):
#         if matrix[i][j] == 1 and matrix[i][j + 1] == 1 and matrix[i][j + 2] == 1 and \
#            matrix[i + 1][j] == 1 and matrix[i + 1][j + 1] == 1 and matrix[i + 1][j + 2] == 1 and \
#            matrix[i + 2][j] == 1 and matrix[i + 2][j + 1] == 1 and matrix[i + 2][j + 2] == 1:
#             countThrees += 1
# print(countThrees)


# total = countOnes + countTwos + countThrees

# print(f"Total: {total}")







def countSquares(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    total_squares = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:  # First row or first column
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                total_squares += dp[i][j]

    return total_squares

# Example usage:
matrix = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
print(countSquares(matrix))  # Output: 7