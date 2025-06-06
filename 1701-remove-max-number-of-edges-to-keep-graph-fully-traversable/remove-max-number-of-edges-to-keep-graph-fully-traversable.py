class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root == v_root:
            return False 

        if self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
            self.rank[u_root] += self.rank[v_root]
        else:
            self.parent[u_root] = v_root
            self.rank[v_root] += self.rank[u_root]
        return True 


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice_uf = UnionFind(n)
        bob_uf = UnionFind(n)

        removed = 0

        for edge in edges:
            if edge[0] == 3:
                u, v = edge[1] - 1, edge[2] - 1
                if not alice_uf.union(u, v) or not bob_uf.union(u, v):
                    removed += 1

        for edge in edges:
            if edge[0] == 1:
                u, v = edge[1] - 1, edge[2] - 1
                if not alice_uf.union(u, v):
                    removed += 1
            elif edge[0] == 2:
                u, v = edge[1] - 1, edge[2] - 1
                if not bob_uf.union(u, v):
                    removed += 1

        alice_root, bob_root = alice_uf.find(0), bob_uf.find(0)
        for node in range(n):
            if alice_root != alice_uf.find(node) or bob_uf.find(node) != bob_root:
                return -1

        return removed