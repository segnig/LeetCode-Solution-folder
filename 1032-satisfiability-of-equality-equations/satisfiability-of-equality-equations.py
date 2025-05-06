class UnionFind:
    def __init__(self):
        self.parent = [i for i in range(26)]
        self.size = [1 for i in range(26)]

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

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equality_equations = [equ for equ in equations if equ[1] == "="]
        unequality_equations = [equ for  equ in equations if equ[1] == "!"]

        equations = equality_equations + unequality_equations
        uf = UnionFind()

        for equ in equations:
            u = ord(equ[0]) - ord("a") 
            v = ord(equ[3]) - ord("a")

            if equ[1] == "=":
                uf.union(u, v)
            else:
                if uf.find(u) == uf.find(v):
                    return False
        return True