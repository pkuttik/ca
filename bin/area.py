from decimal import *
import math
import sys
from itertools import combinations
getcontext().prec = 15
onearea = lambda x : Decimal(math.pi) * Decimal(x*x)
def area(nl):
    totalRadius = 0
    sqft = 0
    if isinstance(nl, tuple):
        for i in nl:
            if isinstance(i, tuple):
                sqft  = sqft + area(i)
            else:
                totalRadius = totalRadius + i
        sqft = sqft + onearea(totalRadius)
    else:
        sqft = onearea(nl)
    return sqft
print(area((1, (2, (3, 4)))))