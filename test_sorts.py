from countcompares import CountCompares
from countswaps import CountSwaps
import insertion
import radix
import quick
import merge
import selection
import sys
import pytest
import collections


def test_sort():
    with open('inputs/random_1000', 'r') as f:
        A = [int(x) for x in f.readlines()]

    ALGS1 = [insertion.sort, radix.sort, quick.sort, merge.sort, selection.sort]
    sorted_f = sorted(A)
    for algs in ALGS1:
        countA = CountSwaps([CountCompares(x) for x in A])
        all_sorts = algs(countA)
        for i, j in zip(all_sorts, sorted_f):
            if not(int(repr(i)) == j):
                assert False


test_sort()
