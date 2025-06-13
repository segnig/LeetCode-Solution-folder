class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.result = [inf for _ in range(n)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v, dist):
        u_parent = self.find(u)
        v_parent = self.find(v)

        if u_parent == v_parent:
            self.result[v_parent] = min(
                dist, self.result[u_parent], self.result[v_parent]
            )
            return False

        if self.size[u_parent] > self.size[v_parent]:
            self.result[u_parent] = min(
                dist, self.result[u_parent], self.result[v_parent]
            )
            self.parent[v_parent] = u_parent
            self.size[u_parent] += self.size[v_parent]
        else:
            self.result[v_parent] = min(
                dist, self.result[u_parent], self.result[v_parent]
            )
            self.parent[u_parent] = v_parent
            self.size[v_parent] += self.size[u_parent]
        return True

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind(n)

        for u, v, dist in roads:
            u, v = u - 1, v - 1
            uf.union(u, v, dist)

        root = uf.find(0) 
        return uf.result[root]