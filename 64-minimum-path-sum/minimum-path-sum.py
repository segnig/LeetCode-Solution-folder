class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0]*( len(grid[0]) + 1) for i in range(len(grid) + 1)]
        for i in range(len(grid)):
            for j in  range(len(grid[0])):
                if j == 0 and i == 0:
                    dp[i+1][j+1] = grid[i][j]
                elif j == 0:
                    dp[i+1][j+1] = grid[i][j] + dp[i][j+1]
                elif i == 0:
                    dp[i+1][j+1] = grid[i][j] + dp[i+1][j]
                else:
                    dp[i+1][j+1] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
        return dp[len(grid)][len(grid[0])]


