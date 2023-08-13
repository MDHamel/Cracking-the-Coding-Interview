# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

#not in place
def rotateMatrix(m):
    size = len(m)
    newMatrix = []

    for y in range(size):
        row = []
        for x in range(size):
            row.insert(0,m[x][y])
        newMatrix.append(row)

    return newMatrix

print(rotateMatrix([[1,2,3],[4,5,6],[7,8,9]]))


#in place and better space complexity
def rotateMatrixInPlace(m):
    size = len(m)

    # Transpose the matrix
    for y in range(size):
        for x in range(y, size): 
            m[y][x], m[x][y] = m[x][y], m[y][x]  # Swap elements at (y, x) and (x, y)

    # Reverse the rows
    for y in range(size):
        m[y].reverse()

    return m

print(rotateMatrixInPlace([[1,2,3],[4,5,6],[7,8,9]]))


#both have the time complexity of  O(n^2) because you do have to read each value of the array, n is the length of the
# nxn matrix