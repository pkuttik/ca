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
tarea = lambda tx : sum ([area(i) for i in tx])
listDiff = lambda l,e : [l[k] for k in range(len(l)) if l[k] not in e]
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
r = list(map(int, input().strip().split(' ')))
# print(area(3)+area(3))
def unnest(p):
    ri = []
    for i in p:
        if isinstance(i,tuple):
            ri = ri + unnest(i)
        else:
            ri.append(i)
    return ri
cl = r
for iCollision in range(2,k+2):
    ll = list(combinations(cl, iCollision))
    uni = []
    for i in ll:
        if isinstance(i, tuple):
            check = unnest(i)
            if len(set(check)) == len(check) and len(set(check)) <= 2 * (iCollision-1):
                uni.append(i)
        else:
            uni.append(i)
    cl = cl + uni
    print(cl)

print('last list {}'.format(uni))
print(sum([area(i) + tarea(listDiff(r,i)) for i in  uni])/len(uni))
# print(list(combinations(r, n-k-1)))
# com = list(combinations(r, n-k-1 if k >0 else n))
# com = []
# round = n if 2 * k > n else 2 * k
# if k > 0:
#     for i in range(k+1,round+1):
#         collisionList = list(combinations(r, i))
#         # kcollisionList = list(combinations(collisionList, k))
#         com = com + collisionList
# else:
#     com = com + list(combinations(r, n))
# print(com, len(com))
# print(sum([tarea(i) + area(sum(listDiff(r,i))) for i in  com])/len(com))
# end = [(i,set(r).difference(i)) for i in com ]
# print(end)
# end = [(sum(i),sum(set(r).difference(i))) for i in com ]
# print(end)
# end = [tarea(i) for i in com ]
# print("Uncolided area {}".format(end))
# end = [(sum( listDiff(r,i) ), area(sum( listDiff(r,i) )))  for i in  com]
# print("Colided area {}".format(end))
#
# a = n-k+1
# # com = list(combinations(r, n-k-1 if k >0 else n))
# # com = list(combinations(r, +1 if k >0 else n))
# print(len(com))
# end = sum([tarea(i) + area(sum( listDiff(r,i) ))  for i in  com])/ (len(com))
# print([tarea(i) + area(sum( listDiff(r,i) ))  for i in  com])
# print(end)
# print(sum([area(sum(i)) + area(sum( listDiff(r,i) ))  for i in  com])/ (len(com)))
# # print(sum([tarea(i) + sum(area(sum( listDiff(r,i) ))  for i in  com])/ (len(com)))
# uc = sum([tarea(i)  for i in  com])/len(com)
# co = sum([area(sum( listDiff(r,i) ))  for i in  com])/ (len(com))
# print(uc + co)