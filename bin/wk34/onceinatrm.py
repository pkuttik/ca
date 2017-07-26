#!/bin/python3

import sys

def _sum(x):
    return int(x[0]) + int(x[1]) + int(x[2])

def onceInATram(x):
    # Complete this function
    first = str(x)[0:3]
    second= str(x)[3:]
    while (True):
        print(first, second)
        if ( _sum(first) == _sum(second)):
            break
        else:
            second = str(int(second)+1).zfill(3)
            if second == '1000':
                first = str(int(first)+1)
                second = '000'

    return first+second

if __name__ == "__main__":
    x = int(input())
    result = onceInATram(x + 1)
    print(result)