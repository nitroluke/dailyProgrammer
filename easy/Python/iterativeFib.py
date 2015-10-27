
def fib(n):
    M = []
    M.append(0)
    M.append(1)
    for i in range(2, n + 1):
        M.append(M[i - 1] + M[i - 2])
    return M

print(fib(50))
