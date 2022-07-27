
def sort(A):
    n = len(A)
    for i in range(0, n):
        k = i
        for j in range(i+1, n):
            if A[j] < A[k]:
                k = j
        if i != k:
            A.swap(k, i)
    return A
