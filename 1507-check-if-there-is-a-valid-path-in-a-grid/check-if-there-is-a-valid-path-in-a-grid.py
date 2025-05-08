class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        self.map_directions = {
            1 : ((0, 1), (0, -1)),
            2 : ((1, 0), (-1, 0)), 
            3 : ((1, 0), (0, -1)), 
            4 : ((0, 1), (1, 0)),
            5 : ((0, -1), (-1, 0)),
            6 : ((0, 1), (-1, 0))
        }
        
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set([(0, 0)])
        self.grid = grid
        return self.dfs()

    def inbound(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols
    
    def dfs(self, r=0, c=0):
        if r == self.rows - 1 and c == self.cols - 1:
            return True
        for x, y in self.map_directions[self.grid[r][c]]:
            n_r, n_c = r + x, c + y
            if self.inbound(n_r, n_c) and (n_r, n_c) not in self.visited:
                if (-x, -y) in self.map_directions[self.grid[n_r][n_c]]:
                    self.visited.add((n_r, n_c))
                    if self.dfs(n_r, n_c):
                        return True
        return False