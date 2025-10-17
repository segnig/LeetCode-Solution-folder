class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        self.VISITED = set()
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.grid = grid
        count = 0

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if grid[row][col] == "1" and (row, col) not in self.VISITED:
                    self.dfs(row, col)
                    count += 1
        
        return count
        

    def dfs(self, row, col):
        if col < 0 or col >= self.COLS or row < 0 or row >= self.ROWS:
            return 
        if self.grid[row][col] == "0":
            return
        if (row, col) in self.VISITED:
            return

        self.VISITED.add((row, col))
        for dr, dc in self.directions:
            self.dfs(row+dr, col+dc)