from collections import defaultdict
class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.weight = []
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def addWeight(self,wtlist):
        self.weight = wtlist

    def f(self, i):
        if i <= 1:
            return 1
        else:
            return self.f(i-1)  + self.f(i-2)

    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''

    def getAllPathsUtil(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            print(path)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.getAllPathsUtil(i, d, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # Prints all paths from 's' to 'd'
    def getAllPaths(self, s, d):

        # Mark all the vertices as not visited
        visited = [False] * (self.V)
        print(visited)

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.getAllPathsUtil(s, d, visited, path)

    def dfs_paths(self, start, goal, path=None):
        if path is None:
            path = [start]
        if start == goal:
            yield path
        for next in list(set(self.graph[start]) - set(path)):
            yield from self.dfs_paths(next, goal, path + [next])

#
# g = Graph(3)
# g.addEdge(1,2)
# g.addEdge(1,3)
# g.addWeight([2,1,1])
# g.addEdge(2,3)
# print(g.graph, g.weight)

n = int(input())
g = Graph(n)
for i in range(n-1):
    u,v = [int(i) for i in input().strip().split()]
    g.addEdge(u,v)
g.addWeight([int(i) for i in input().split()])


# print(g.graph, g.weight)
# l = [(i,j,list(g.dfs_paths(i,j))) for i in g.graph.keys() for j in g.graph.keys()]
l = [(i,j,list(g.dfs_paths(i,j)), g.f(sum(g.weight[x-1] for k in list(g.dfs_paths(i,j)) for x in k))) for i in g.graph.keys() for j in g.graph.keys()]
l = sum([g.f(sum(g.weight[x-1] for k in list(g.dfs_paths(i,j)) for x in k)) for i in g.graph.keys() for j in g.graph.keys()])
print(l)
