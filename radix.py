import numpy as np 

def sort(A):
    n = len(A)

    max_size = 0
    max_num = None
    for num in A:
        if not max_num:
            max_num = num
        if num > max_num: 
            size = num.length
            if size > max_size:
                max_size = size
                max_num = num
            

    max_size = int(max_size)+1

    for i in range(max_size):
        A = bucketsort(A, i, n)

    return A

def bucketsort(A, ex, n):

    bucket = [[] for _ in range(10)]

    mod = 10 ** (ex+1)

    for i in range(n):
        idx = (A[i].elem % mod) // (mod//10)
        bucket[idx].append(A[i])

    i = 0
    for lst in bucket:
        for el in lst:
            A[i] = el
            i += 1
    
    return A


if __name__ == "__main__":
    pass