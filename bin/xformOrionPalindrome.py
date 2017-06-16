

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
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
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

for k, v in tDict.items():
    #for vl in v:
    #    x1 = tDict[vl] if tDict.get(vl) else []
    #    tDict[k] = list(set(list(tDict [k]  + x1)))
    tDict[k] = dfs(tDict, k)

# print(tDict)
a = list(map(int, input().strip().split(' ')))
a1 = []
for i in a:
    if i in tDict:
        a1.extend([min(tDict[i])])
    else:
        a1.extend([i])
# print(a,a1, lps(''.join(a1)))
print(lps(a1))
