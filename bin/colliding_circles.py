from decimal import *
import math
from itertools import permutations
from itertools import combinations
getcontext().prec = 15
area = lambda x : Decimal(math.pi) * Decimal(x*x)
tarea = lambda tx : sum ([area(i) for i in tx])
listDiff = lambda l,e : [l[k] for k in range(len(l)) if l[k] not in e]
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
r = list(map(int, input().strip().split(' ')))
# print(area(3)+area(3))
print(r)
# print(list(combinations(r, n-k-1)))
# com = list(combinations(r, n-k-1 if k >0 else n))
com = []
round = n if 2 * k > n else 2 * k
if k > 0:
    for i in range(k+1,round+1):
        collisionList = list(combinations(r, i))
        # kcollisionList = list(combinations(collisionList, k))
        com = com + collisionList
else:
    com = com + list(combinations(r, n))
print(com, len(com))
print(sum([tarea(i) + area(sum(listDiff(r,i))) for i in  com])/len(com))
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