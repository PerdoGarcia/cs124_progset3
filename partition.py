import sys

# Karmarkar-Karp algorithm
def karmarkar_karp(arr):
    while len(arr) > 1:
        arr.sort()
        arr[-1] = arr[-1] - arr[-2]
        arr.pop(-2)
    return arr[0]

