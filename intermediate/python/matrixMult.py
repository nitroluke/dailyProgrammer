import random

def matMult(A, B):
    C = [[0 for _ in range(len(A))] for _ in range(len(A))]
    tmp = [0 for _ in range(len(A))]
    for i in range(len(A)):                     # spwan
        for j in range(len(A)):                 # spawn
            for k in range(len(A)):             # spawn
                tmp[k] = A[i][k] * B[k][j]
                # C[i][j] = C[i][j] + A[i][k] * B[k][j]
                                                # sync
            C[i][j] = sum(tmp)                  # spawn

            # tmp = [0 for _ in range(len(A))]
    return C


def printMatrix(matrix):
    for row in matrix:
        print(row)


# mat1 = [[2, 4], [1, 3]]
# mat2 = [[1, 1], [0, 1]]
mat1 = [[random.randint(0, 9) for _ in range(6)] for _ in range(6)]
mat2 = [[random.randint(0, 9) for _ in range(6)] for _ in range(6)]
printMatrix(mat1)
print()
printMatrix(mat2)
print()
printMatrix(matMult(mat1, mat2))
