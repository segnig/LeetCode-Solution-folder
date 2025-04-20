class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.rows = len(board)
        self.cols = len(board[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(self.rows):
            for j in range(self.cols):
                if self.dfs(i, j, 0, set()):
                    return True
        return False
        
    def dfs(self, row, col, index, visited):
        if not self.inbound(row, col) or (row, col) in visited:
            return False

        if self.board[row][col] != self.word[index]:
            return False

        if index == len(self.word) - 1:
            return True

        visited.add((row, col))
        for dr, dc in self.directions:
            if self.dfs(row + dr, col + dc, index + 1, visited):
                return True
        visited.remove((row, col))
        return False

    def inbound(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols
