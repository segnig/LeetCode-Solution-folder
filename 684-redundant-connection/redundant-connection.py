class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1 for i in range(n + 1)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, v, u):
        r_v = self.find(v)
        r_u = self.find(u)


        if r_v != r_u:
            if self.size[r_v] > self.size[r_u]:
                self.size[r_v] += self.size[r_u]
                self.parent[r_u] = r_v
            else:
                self.size[r_u] += self.size[r_v]
                self.parent[r_v] = r_u
            return True
        else:
            False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for edge in edges:
            if not uf.union(*edge):
                return edge 

        return []    