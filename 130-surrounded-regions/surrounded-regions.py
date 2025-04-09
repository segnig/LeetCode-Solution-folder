class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        self.visited = [[False] * len(self.board[0]) for _ in range(len(self.board))]

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == "O" and not self.visited[i][j]:
                    self.surrounded = True
                    self.temp = []
                    self.dfs(i, j)
                    if self.surrounded:
                        for r, c in self.temp:
                            self.board[r][c] = "X"
                

    def inbound(self, row, col):
        return 0 <= row < len(self.board) and 0 <= col < len(self.board[0])

    def dfs(self, row, col):
        if not self.inbound(row, col):
            self.surrounded = False
            return
        if self.board[row][col] == "X" or self.visited[row][col]:
            return
        
        self.visited[row][col] = True
        self.temp.append((row, col))
        
        for dr, dc in self.directions:
            self.dfs(row + dr, col + dc)