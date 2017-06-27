#!/bin/python3

import sys
from itertools import combinations
from collections import Counter

def checkPalindrome(d, n):
    o = 0
    e = 0

    for k,v in d.items():
        if v % 2 == 1:
            o += 1
            if o >=2:
                return  False
        else:
            e += 1
    if n != 1 and 0 in d and d[0] > 1 and (len(d) == 1 or (o == 1 and len(d) == 2 and n-d[0] ==1)):
        return False
    return True if (n%2==0 and o==0) or (n%2==1 and o==1) else False

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
table = []
for table_i in range(n):
   table_t = [int(table_temp) for table_temp in input().strip().split(' ')]
   table.append(table_t)
print(*table, sep='\n')
c = [(i,j) for i in range(n) for j in range(m)]
print(c)
print(*combinations(c,2))
print(*[(i,i) for i in c])
l = sorted([ i + tuple([(i[1][1] - i[0][1] + 1) * (i[1][0] - i[0][0] + 1)]) for i in list(combinations(c,2)) + [(i,i) for i in c] if i[0][0] <= i[1][0] and i[0][1] <= i[1][1]  ], key = lambda x: x[2], reverse = True)
print("list {}".format(l), sep='\n')
for i in l:
    m = [table[r][c] for r in range(i[0][0],i[1][0] + 1) for c in range(i[0][1],i[1][1] + 1)]
    e = dict(Counter(m))
    print(i, e, checkPalindrome(e, len(m)))
    if checkPalindrome(e, len(m)):
        print(i[2], ' '.join(map(str,i[0]+ i[1])), sep='\n')
        break
