class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        self.candidates = [[set(str(num) for num in range(1, 10)) for _ in range(9)] for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    self.update_candidates(board, i, j, board[i][j])
        
        self.solve(board)

    def solve(self, board):
        min_candidates = 10
        best_cell = None
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.' and len(self.candidates[i][j]) < min_candidates:
                    min_candidates = len(self.candidates[i][j])
                    best_cell = (i, j)
                    if min_candidates == 1:
                        break
            if best_cell is not None and min_candidates == 1:
                break

        if best_cell is None:
            return True
        
        i, j = best_cell
        for val in list(self.candidates[i][j]):
            board[i][j] = val
            candidates_copy = self.copy_candidates()
            self.update_candidates(board, i, j, val)
            
            if self.solve(board):
                return True
            
            board[i][j] = '.'
            self.restore_candidates(candidates_copy)
        
        return False

    def update_candidates(self, board, i, j, val):
        for x in range(9):
            if val in self.candidates[i][x]:
                self.candidates[i][x].remove(val)
            if val in self.candidates[x][j]:
                self.candidates[x][j].remove(val)
        
        subgrid_row = (i // 3) * 3
        subgrid_col = (j // 3) * 3
        for x in range(subgrid_row, subgrid_row + 3):
            for y in range(subgrid_col, subgrid_col + 3):
                if val in self.candidates[x][y]:
                    self.candidates[x][y].remove(val)

    def copy_candidates(self):
        return [[set(cell) for cell in row] for row in self.candidates]

    def restore_candidates(self, candidates_copy):
        self.candidates = candidates_copy