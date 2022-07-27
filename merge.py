
def sort(A):
    n = len(A)
    if n <= 1:
        return A
    # floor(n/2)
    i = n // 2
    # Recursive case
    A1 = sort(A[0:i])
    A2 = sort(A[i:])
    return merge(A1, A2, A)

def merge(A1, A2, A):
    i, j = 0, 0
    while i < len(A1) and j < len(A2):
        if A1[i] < A2[j]:
            A[i+j] = A1[i]
            i += 1
        else:
            A[i+j] = A2[j]
            j += 1
    
    # make sure that the lists are emptied
    while i < len(A1):
        A[i+j] = A1[i]
        i += 1

    while j < len(A2):
        A[i+j] = A2[j]
        j += 1

    return A