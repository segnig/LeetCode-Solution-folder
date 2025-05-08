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
            if u_p < v_p:
                self.parent[v_p] = u_p 
            else:
                self.parent[u_p] = v_p

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(26)

        for i in range(len(s1)):
            u = ord(s1[i]) - ord("a")
            v = ord(s2[i]) - ord("a")

            uf.union(u, v)

        result = ""
        for i in range(len(baseStr)):
            result += chr(uf.find(ord(baseStr[i]) - ord("a")) + ord("a"))
        
        return result