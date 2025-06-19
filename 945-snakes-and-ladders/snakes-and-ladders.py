class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        visited = set()
        queue = deque([(1, 0)])

        while queue:
            square, moves = queue.popleft()
            if square == n * n:
                return moves

            for next_square in range(square + 1, min(square + 7, n * n + 1)):
                r, c = self.get_coordinates(n, next_square)
                dest = board[r][c] if board[r][c] != -1 else next_square

                if dest not in visited:
                    visited.add(dest)
                    queue.append((dest, moves + 1))

        return -1

    def get_coordinates(self, n, square):
        quot, rem = divmod(square - 1, n)
        row = n - 1 - quot 
        if quot % 2 == 0:
            col = rem
        else:
            col = n - 1 - rem
        return row, col