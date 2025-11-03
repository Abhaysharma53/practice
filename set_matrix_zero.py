matrix = [[7, 0, 1, 3], [1, 20, 0, 4], [19, 0, 5, 11], [4, 27, 14, 7]]
rows  = len(matrix)
cols = len(matrix[0])
print(rows, cols)
row_track = [0 for _ in range(rows)]
col_track = [0 for _ in range(cols)]
#rint(row_track)
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            row_track[i] = -1
            col_track[j] = -1
#rint(row_track, col_track)
for i in range(rows):
    for j in range(cols):
        if row_track[i] == -1 or col_track[j] == -1:
            matrix[i][j] = 0

print(matrix)

