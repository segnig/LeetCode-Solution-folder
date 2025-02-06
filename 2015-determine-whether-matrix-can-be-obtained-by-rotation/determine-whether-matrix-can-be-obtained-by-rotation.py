class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        Poss = True

        for r in range(n):
            for c in range(n):
                if mat[r][c] != target[c][n - r - 1]:
                    Poss = False
        if Poss:
            return Poss
        Poss =True
        for r in range(n):
            for c in range(n):
                if mat[r][c] != target[n - c - 1][r]:
                    Poss = False

        if Poss:
            return Poss

        Poss =True
        for r in range(n):
            for c in range(n):
                if mat[r][c] != target[n - r - 1][n - c - 1]:
                    Poss = False

        if Poss:
            return Poss

        Poss =True
        for r in range(n):
            for c in range(n):
                if mat[r][c] != target[r][c]:
                    Poss = False

        return Poss