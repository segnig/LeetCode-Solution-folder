class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        def check(col, c):
            count = 0
            for i in range(len(col)):
                if not col[i][c]:
                    count += 1
            return count > len(col)// 2
        for row in grid:
            if not row[0]:
                for h in range(len(row)):
                    row[h] = int(not(row[h]))

        for i in range(len(grid[0])):
            if check(grid, i):
                for j in range(len(grid)):
                    grid[j][i] = int(not grid[j][i])

        result = 0
        n = len(grid[0])
        for i in range(len(grid)):
            for j in range(n):
                result += grid[i][j] * 2 ** (n - 1- j)

        return result

        