import random
import sumRecur


def matMult(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    tmp = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                tmp[k] = A[i][k] * B[k][j]
            C[i][j] = sumRecur.sumRecur(tmp, 1, n)
    printMatrix(C)
    return C


def printMatrix(matrix):
    for row in matrix:
        print(row)
    print()

mat1 = [[random.randint(0, 9) for _ in range(5)] for _ in range(5)]
mat2 = [[random.randint(0, 9) for _ in range(5)] for _ in range(5)]

printMatrix(mat1)
printMatrix(mat2)
printMatrix(matMult(mat1, mat2))
