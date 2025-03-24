class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows = set()
        neg_dia = set()
        pos_dia = set()
        result = []

        def backtrack(i, res):
            nonlocal result
            if i == n:
                copy = ["".join(row) for row in res]
                result.append(copy)
                return 

            for j in range(n):
                if (j in rows) or ((i - j) in neg_dia) or ((i + j) in pos_dia):
                    continue

                res[j][i] = "Q"
                rows.add(j)
                neg_dia.add(i - j)
                pos_dia.add(j + i)

                backtrack(i+1, res)

                rows.remove(j)
                res[j][i] = "."
                neg_dia.remove(i - j)
                pos_dia.remove(j + i)

        res = [["."] * n for _ in range(n)] 

        backtrack(0, res)
        return result