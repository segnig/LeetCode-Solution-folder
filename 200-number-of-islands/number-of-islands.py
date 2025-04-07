class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        count = 0

        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == "1":
                    self.dfs(r, c)
                    count += 1
        return count

        
    def in_bound(self, row, col):
        return 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0])

    def dfs(self, row, col):
        
        if not self.in_bound(row, col) or self.grid[row][col] == "0":
            return 1
        if self.grid[row][col] == -1:
            return 0

        self.grid[row][col] = -1
        
        return (
            self.dfs(row - 1, col) + 
            self.dfs(row + 1, col) + 
            self.dfs(row, col - 1) + 
            self.dfs(row, col + 1)
        )