class Solution:
    def totalNQueens(self, n: int) -> int:
        rows = set()
        neg_dia = set()
        pos_dia = set()
        result = 0

        def backtrack(i):
            nonlocal result
            if i == n:
                result += 1
                return 

            for j in range(n):
                if (j in rows) or ((i - j) in neg_dia) or ((i + j) in pos_dia):
                    continue

                rows.add(j)
                neg_dia.add(i - j)
                pos_dia.add(j + i)

                backtrack(i+1)

                rows.remove(j)
                neg_dia.remove(i - j)
                pos_dia.remove(j + i) 

        backtrack(0)
        return result    