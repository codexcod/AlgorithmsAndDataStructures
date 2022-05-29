def diagonalDiference(matrix):
    leftDiagonal = 0
    rightDiagonal = 0

    rows = len(matrix)
    columns = len(matrix[0])

    right = len(matrix) - 1
    left = 0

    while left < rows and left < columns and left < rows and right >= 0:
        leftDiagonal += matrix[left][left]
        rightDiagonal += matrix[left][right]

        right -= 1
        left += 1

    return leftDiagonal - rightDiagonal


matrix = [[1, 2, 3],
          [4, 5, 6],
          [9, 8, 9]]

print(diagonalDiference(matrix))
