class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            if not self.is_valid_board(row):
                return False

        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.is_valid_board(column):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.is_valid_board(subgrid):
                    return False
        
        return True


    def is_valid_board(self, sub_board):
        seen = set()
        for cell in sub_board:
            if cell != '.':
                if cell in seen:
                    return False
                seen.add(cell)
        return True
