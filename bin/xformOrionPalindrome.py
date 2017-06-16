#!/bin/python3
import operator
import sys


def lps(str):
    n = len(str)
    L = [[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        L[i][i] = 1

    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if str[i] == str[j] and cl == 2:
                L[i][j] = 2
            elif str[i] == str[j]:
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i][j - 1], L[i + 1][j]);
    # print(*L, sep='\n')
    return L[0][n - 1]

def check(s):
    return s == s[::-1]


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

n,k,m = input().strip().split(' ')
n,k,m = [int(n),int(k),int(m)]
tDict = {}
for a0 in range(k):
    x,y = input().strip().split(' ')
    x,y = [int(x),int(y)]

    # x1 = tDict[x] if tDict.get(x) else ()
    # y1 = tDict[y] if tDict.get(y) else ()
    if tDict.get(x):
        tDict[x].add(y)
    else:
        tDict[x] = set([y])
    # tDict[x] = set(tDict[x].add(y) + y1) if tDict.get(x) else set(y,y1)
    if tDict.get(y):
        tDict[y].add(x)
    else:
        tDict[y] = set([x])
    # tDict[y] = set(tDict[y].add(x) + x1) if tDict.get(y) else set(x,x1)
    # print(x, y, [x],[y], tDict.get(x), tDict, x1, y1)
print(tDict)
for k, v in tDict.items():
    # for vl in v:
    #     x1 = tDict[vl] if tDict.get(vl) else []
    #     tDict[k] = list(set(list(tDict [k]  + x1)))
    tDict[k] = dfs(tDict, k)

a = list(map(int, input().strip().split(' ')))
a1 = []
for i in a:
    if i in tDict:
        a1.extend([min(tDict[i])])
    else:
        a1.extend([i])
# print(a,a1, lps(''.join(a1)))
    print(tDict, a1)
    # x1 = tDict[x] if tDict.get(x) else []
    # y1 = tDict[y] if tDict.get(y) else []
    tDict[x] = list(set(tDict[x] + [y] )) if tDict.get(x) else [y]
    # tDict[x] = list(set(tDict[x] + [y] + y1)) if tDict.get(x) else [y] + y1
    tDict[y] = list(set(tDict[y] + [x] )) if tDict.get(y) else [x]
    # tDict[y] = list(set(tDict[y] + [x] + x1)) if tDict.get(y) else [x] + x1
    # print(x, y, [x],[y], tDict.get(x), tDict, x1, y1)

for k, v in tDict.items():
    for vl in v:
        x1 = tDict[vl] if tDict.get(vl) else []
        tDict[k] = list(set(list(tDict [k]  + x1)))

# print(tDict)
a = list(map(int, input().strip().split(' ')))
a1 = [str(min(tDict[i])) for i in a]
# print(a,a1, lps(''.join(a1)))
print(lps(''.join(a1)))



# fh = a[:int(m//2)]
# sh = list(reversed(a[int(m//2)::])) if m%2 == 0 else list(reversed(a[int(m//2)+1:]))
# print(fh,sh, list(map(operator.sub, fh, sh)))
# sl = list(map(operator.sub, fh, sh))
# for i in range(len(sl)):
#     if sl[i] != 0 and (sh[i] in tDict[fh[i]] or fh[i] in tDict[sh[i]]):
#         sh[i] = fh[i]
#     elif sl[i] != 0 and i + 1 < len(fh) and (sh[i] in tDict[fh[i+1]] or fh[i+1] in tDict[sh[i]]):
#         fh.remove(fh[i+1])
#     elif sl[i] != 0 and i + 1 < len(sh) and (sh[i+1] in tDict[fh[i]] or fh[i] in tDict[sh[i+1]]):
#         sh.remove(sh[i + 1])
# print(fh,sh, list(map(operator.sub, fh, sh)))