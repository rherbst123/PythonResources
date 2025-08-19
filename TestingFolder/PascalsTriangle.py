numRows = 3


answer = []

for r in range(numRows):
    row = [1] * (r + 1)


    for calc in range(1 , r):
        row[calc] = answer[-1][calc-1] + answer[-1][calc]
    answer.append(row)

print(answer)
    