# recursive divide and conquer array summation

def sumRecur(A, start, end):
    if start == end:
        return A[start - 1]
    mid = int((start + end) / 2)
    s1 = sumRecur(A, start, mid)
    s2 = sumRecur(A, mid + 1, end)
    return s1 + s2