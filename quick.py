

def sort(A):
    low = 0
    high = len(A) - 1
    return quicksort(A, low, high)

def quicksort(A, low, high):
    if low >= high:
        return A
    p = partition(A, low, high)
    quicksort(A, low, p-1)
    quicksort(A, p+1, high)
    return A

def choosepivot(A, low, high):
    # We use median of three to choose the pivot
    mid = (low + high) // 2

    if A[high] < A[low]:
        A.swap(low, high)        
    if A[mid] < A[low]:
        A.swap(mid, low)
    if A[high] < A[mid]:
        A.swap(high, mid)
    
    return mid


def partition(A, low, high):
    p = choosepivot(A, low, high)
    A.swap(p, high)
    pivot = A[high]

    left = low
    right = high - 1

    while left <= right:
        while left <= right and A[left] <= pivot:
            left += 1
        while right >= left and A[right] >= pivot:
            right -= 1
        
        if left < right:
            A.swap(left, right)
    
    A.swap(left, high)
    return left

