# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.

def AbsoluteZero(m):
    rowNum = len(m[0])
    colNum = len(m)

    rowsToZero = []
    colsToZero = []

    for col in range(colNum):
        for row in range(rowNum):
            if m[col][row] == 0:
                rowsToZero.append(row)
                colsToZero.append(col)

    for row in rowsToZero:
        for col in range(rowNum):
            m[row][col] = 0

    for col in colsToZero:
        for row in range(colNum):
            m[row][col] = 0

    return m

#time complexity: O(M * N) where m is the number of row and n is the number of cols

matrix = [
    [1, 9, 2],
    [9, 0, 9],
    [3, 9, 4]
]

print(AbsoluteZero(matrix))