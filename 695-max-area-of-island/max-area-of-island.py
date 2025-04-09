class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.board = grid
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        self.visited = [[False] * len(self.board[0]) for _ in range(len(self.board))]
        result = 0

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 1 and not self.visited[i][j]:
                    self.count = 0
                    self.dfs(i, j)
                    result = max(result, self.count)

        return result
                    
            
    def inbound(self, row, col):
        return 0 <= row < len(self.board) and 0 <= col < len(self.board[0])

    def dfs(self, row, col):
        if not self.inbound(row, col) or self.board[row][col] == 0 or self.visited[row][col]:
            return
        
        self.visited[row][col] = True
        self.count += 1
        
        for dr, dc in self.directions:
            self.dfs(row + dr, col + dc)