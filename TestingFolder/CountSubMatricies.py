mat = [[1,0,1],
       [1,1,0],
       [1,1,0]]


rect = 0
#1x1
for i in range(len(mat)):
    for j in range(len(mat)):
        if mat[i][j] == 1:
            rect += 1
print(rect)


#1x2 horizontal rectangles
for i in range(len(mat)):
    for j in range(len(mat[0])-1):
        if mat[i][j] == 1 and mat[i][j+1] == 1:
            rect += 1
print(rect)


for i in range(len(mat)-1):
    for j in range(len(mat[0])-1):
        if mat[i][j] and mat[i +1][j] == 1:
            rect += 1
print(rect)

