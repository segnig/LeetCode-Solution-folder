class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)

        if parent_u == parent_v:
            return False

        if self.size[parent_u] > self.size[parent_v]:
            self.parent[parent_v] = parent_u
            self.size[parent_u] += self.size[parent_v]
        else:
            self.parent[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]

        return True

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        result = [False] * len(queries)
        edgeList.sort(key=lambda x: x[2])
        temp_queries = [[i, val] for i, val in enumerate(queries)] 
        temp_queries.sort(key=lambda x: x[1][2])
        current = 0
        for idx, edge_dist in temp_queries:
            while current < len(edgeList) and edge_dist[2] > edgeList[current][2]:
                uf.union(edgeList[current][0], edgeList[current][1])
                current += 1

            if uf.find(edge_dist[0]) == uf.find(edge_dist[1]):
                result[idx] = True
        return result
