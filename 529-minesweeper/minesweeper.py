class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.board = board
        self.directions = [
            (0, 1), (0, -1), (-1, 0), (1, 0), 
            (-1, -1), (-1, 1), (1, -1), (1, 1)
            ]
        row, col = click
        if self.board[row][col] == "M":
            self.board[row][col] = "X"
        else:
            self.bfs(row, col)
        return self.board
    
    def inbound(self, row, col):
        return 0 <= row < len(self.board) and 0 <= col < len(self.board[0])

    def count_mine(self, row, col):
        count = 0
        for dr, dc in self.directions:
            r = row + dr
            c = col + dc

            if self.inbound(r, c):
                if self.board[r][c] == "M":
                    count += 1
        return count
        
    
    def bfs(self, rw, cl):
        queue = deque([(rw, cl)])
        visited = set([(rw, cl)])
        self.board[rw][cl] = "B"

        while queue:
            row, col = queue.popleft()
            count_mine = self.count_mine(row, col)

            if count_mine > 0:
                self.board[row][col] = str(count_mine)
            else:
                for dr, dc in self.directions:
                    r = row + dr
                    c = col + dc
                    if self.inbound(r, c) and self.board[r][c] == "E":
                        self.board[r][c] = "B"
                        visited.add((r, c))
                        queue.append((r, c))           