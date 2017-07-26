#!/bin/python3

import sys
from random import randrange

if __name__ == "__main__":
    # n, q = input().strip().split(' ')
    # n, q = [int(n), int(q)]
    n, q = [randrange(3,8), randrange(1,4)]
    # arr = list(map(int, input().strip().split(' ')))
    arr = [randrange(2,100) for _ in range(n)]
    # print(arr, n, q)
    subarr = []
    for i in range(n):
        for j in range(i, n):
            # print(arr[i:j+1], end = ' ')
            subarr.append(arr[i:j+1])
    for a0 in range(q):
        x, y = input().strip().split(' ')
        x, y = [int(x), int(y)]
        # Write Your Code Here
        print(x, y)
        qualified = [i for i in subarr if i.count(x) == i.count(y)]
        print( len(qualified))