class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, x):
        if self.parent[x] == x:
            return self.parent[x]

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        u_p = self.find(u)
        v_p = self.find(v)

        if u_p != v_p:
            if self.size[u_p] > self.size[v_p]:
                self.parent[v_p] = u_p
                self.size[u_p] += self.size[v_p]  
            else:
                self.parent[u_p] = v_p
                self.size[v_p] += self.size[u_p] 
            return True
        return False

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        complete_graph_edges = []
        for i in range(len(points)):
            x, y = points[i]
            
            for j in range(i + 1, len(points)):
                xi, yi = points[j]
                
                weight = abs(x - xi) + abs(y - yi)
                complete_graph_edges.append((weight, i, j))

        uf = UnionFind(len(points))
        complete_graph_edges.sort()

        result = 0
        for weight, a, b in complete_graph_edges:
            if uf.union(a, b):
                result += weight
        return result
    