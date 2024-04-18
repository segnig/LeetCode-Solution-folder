class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        result = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    counted = 0
                    if i - 1 < 0 or not grid[i-1][j]:
                        counted += 1
                    if i + 1 == row or not grid[i + 1][j]:
                        counted += 1
                    if j - 1 < 0 or not grid[i][j-1]:
                        counted += 1
                    if j + 1 == col or not grid[i][j + 1]:
                        counted += 1
                    result += counted
        return result