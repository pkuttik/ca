#!/bin/python3

import sys
from collections import defaultdict, Counter
import operator
class Graph:
    def __init__(self, v):
        self.vertices = v
        self.graph = defaultdict(list)
    def addEdges(self, u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def addWeight(self, wtlist):
        self.wtlist = wtlist
    def dfs(self, start,goal, path=None):
        if path is None:
            path = [start]
        if start == goal:
            yield path
        for next in list(set(self.graph[start])- set(path)):
            yield  from self.dfs(next,goal,path + [next])
if __name__ == "__main__":
    n, q = input().strip().split(' ')
    n, q = [int(n), int(q)]
    n, q = [int(n), int(q)]
    g = Graph(n)
    c = list(map(int, input().strip().split(' ')))
    g.addWeight(c)
    for a0 in range(n-1):
        u, v = input().strip().split(' ')
        u, v = [int(u), int(v)]
        g.addEdges(u,v)
    # print(g.graph, g.wtlist)
    for a0 in range(q):
        u, v, k = input().strip().split(' ')
        u, v, k = [int(u), int(v), int(k)]
        path = list(g.dfs(u,v))
        pathWt = [g.wtlist[i-1] for i in path[0]]
        cnt = dict(Counter(pathWt))
        scnt = sorted(cnt.items(), key = operator.itemgetter(1,0), reverse = True)
        # print(path, Counter(path[0]))
        # print(pathWt,cnt, scnt)
        print(scnt[k-1][0])