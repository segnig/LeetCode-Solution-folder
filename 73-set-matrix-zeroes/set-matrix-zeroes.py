class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        zero_cols = set()
        zero_rows = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if not matrix[row][col]:
                    zero_rows.add(row)
                    zero_cols.add(col)

        for col in zero_cols:
            for r in range(len(matrix)):
                matrix[r][col] = 0

        for row in zero_rows:
            for c in range(len(matrix[0])):
                matrix[row][c] = 0
   