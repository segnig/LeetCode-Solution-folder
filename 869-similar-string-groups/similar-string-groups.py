class UnionFind:
    def __init__(self, strs):
        self.parent = {word : word for word in strs}
        self.size = {word : 1 for word in strs}
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, u, v):
        p_v = self.find(v)
        p_u = self.find(u)

        if p_v == p_u:
            return False

        if self.size[p_v] > self.size[p_u]:
            self.parent[p_u] = p_v
            self.size[p_v] += self.size[p_u]
        else:
            self.parent[p_v] = p_u
            self.size[p_u] += self.size[p_v]

        return True

class Solution:

    def check(self, s1, s2):
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
            if count > 2:
                return False

        return count == 0 or count == 2

    def numSimilarGroups(self, strs: List[str]) -> int:
        uf = UnionFind(set(strs))
        result = len(set(strs))
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if self.check(strs[i], strs[j]):
                    if uf.union(strs[i], strs[j]):
                        result -= 1

        return result