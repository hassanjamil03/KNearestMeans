#problem link = https://www.hackerrank.com/challenges/mini-max-sum/problem?h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys


def qsort(arr):
    if len(arr) == 0:
        return []
    pivot = [arr[-1]]
    more = []
    less = []
    final = [0] * len(arr)
    arr = arr[:-1]

    for x in arr:
        # seeing if each element of array is more, less, or same as pivot and assigning to corrosponding array
        if x > pivot[0]:
            more.append(x)
        elif x < pivot[0]:
            less.append(x)
        elif x == pivot[0]:
            pivot.append(x)

    # if the array has been completely sorted
    if len(more) <= 1 and len(less) <= 1:
        final = less + pivot + more
        return final
    # else if arr is not completely sorted then add sorted pivot to final list
    else:
        for i in range(len(pivot)):
            final[len(less) + i] = pivot[i]
        more = qsort(more)
        less = qsort(less)
        return less + pivot + more


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr = qsort(arr)
    print(arr)


if __name__ == '__main__':
    arr = [5]

    miniMaxSum(arr)
