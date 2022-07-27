import time
import random

def insertionsort(A, n):
    for i in range(1, n):
        j = i
        while j > 0 and A[j-1] > A[j]:
            swap(A, j-1, j)
            j -= 1
    return A


def bogosort(A, n):
    """The worst possible sorting algorithm with O(n!) runtime. Shuffles the array until it is sorted. 

    Args:
        A (ndarray): array
        n (int): size of array

    Yields:
        A: the array after each iteration, to be used in animation
    """
    sorted = False
    while not sorted: 
        sorted = True
        for i in range(n+1):
            if A[i] > A[i+1]:
                sorted = False
                break
        np.random.shuffle(A)
    print(A)
    return A

def mergesort(A):
    if len(A) <= 1:
        return A

    # Recursive case
    left = []
    right = []
    for i, x in enumerate(A):
        if i < (len(A)/2):
            left.append(x)
        else:
            right.append(x)
    
    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

# def mergesort(A:
#     pass  

def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            del left[0]
        else:
            result.append(right[0])
            del right[0]

    while left:
        result.append(left[0])
        del left[0]

    while right:
        result.append(right[0])
        del right[0]

    return result


def quicksort(A, n):
    pass


if __name__ == '__main__':
    n = 5
    A = [i for i in range(n+1)]
    random.shuffle(A)
    print(A)
    A = mergesort(A)
    print(A)

