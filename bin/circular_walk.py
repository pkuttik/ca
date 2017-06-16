#!/bin/python3

import sys

def circularWalk(n, s, t, r_0, g, seed, p):
    # Complete this function
    R = [r_0]
    for i in range(1, n):
        R.append(((R[i-1] * g) + seed) % p)
    print(R)

n, s, t = input().strip().split(' ')
n, s, t = [int(n), int(s), int(t)]
r_0, g, seed, p = input().strip().split(' ')
r_0, g, seed, p = [int(r_0), int(g), int(seed), int(p)]
result = circularWalk(n, s, t, r_0, g, seed, p)
print(result)

