import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import time
import random
import sys 

def swap(A, i, j):
    """Swaps two elements in an array.

    Args:
        A (ndarray): Array
        i (int): First index 
        j (int): Second index
    """
    if i != j:
        A[i], A[j] = A[j], A[i]


def insertionsort(A, n):
    for i in range(1, n):
        j = i
        while j > 0 and A[j-1] > A[j]:
            swap(A, j-1, j)
            j -= 1
            yield A


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
        for i in range(n):
            if A[i] > A[i+1]:
                sorted = False
                break
        np.random.shuffle(A)
        yield A
    

def quicksort(A, n):
    pass

def animate(sorting_algo, N=50):

    # Make array using arange and shuffle it
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        A = [int(x) for x in f.readlines()]

    
    title = sorting_algo.__name__

    generator = sorting_algo(A, N)

    # Initialize figure and axis.
    fig, ax = plt.subplots()
    ax.set_title(title)

    # Initialize a bar plot. Note that matplotlib.pyplot.bar() returns a
    # list of rectangles (with each bar in the bar plot corresponding
    # to one rectangle), which we store in bar_rects.
    bar_rects = ax.bar(range(len(A)), A, align="edge")

    # Set axis limits. Set y axis upper limit high enough that the tops of
    # the bars won't overlap with the text label.
    # ax.set_xlim(0, N)
    # ax.set_ylim(0, int(1.07 * N))

    # Place a text label in the upper-left corner of the plot to display
    # number of operations performed by the sorting algorithm (each "yield"
    # is treated as 1 operation).
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    # Define function update_fig() for use with matplotlib.pyplot.FuncAnimation().
    # To track the number of operations, i.e., iterations through which the
    # animation has gone, define a variable "iteration". This variable will
    # be passed to update_fig() to update the text label, and will also be
    # incremented in update_fig(). For this increment to be reflected outside
    # the function, we make "iteration" a list of 1 element, since lists (and
    # other mutable objects) are passed by reference (but an integer would be
    # passed by value).
    # NOTE: Alternatively, iteration could be re-declared within update_fig()
    # with the "global" keyword (or "nonlocal" keyword).
    iteration = [0]
    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=generator, interval=1,
        repeat=False)
    plt.show()


if __name__ == '__main__':
    
    animate(insertionsort, 100)