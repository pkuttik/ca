#!/bin/python3

import sys

import math


def duplication(x):
    # Complete this function
    s = '0'
    return '0' if x == 0 else 0
    print(math.ceil(math.log(x,2)))
    for i in range(math.ceil(math.log(x,2))+1):
        # t = bin(~int(s, 2)).split('b')[1].zfill(len(s))
        t = s.replace('0','2').replace('1','0').replace('2','1')
        s = s + t
        print(s, t)
    return s[x]

q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    result = duplication(x)
    print(result)
