class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        self.count = 0

        start = end = (-1, -1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != -1:
                    self.count += 1
                if grid[i][j] == 1:
                    start = (i, j)

        self.result = 0
        path = set([start])
        self.backtrack(start[0], start[1], path)

        return self.result

    def backtrack(self, row, col, path):
        if len(path) == self.count and self.grid[row][col] == 2:
            self.result += 1
            return

        for dx, dy in self.directions:
            nr, nc = row + dx, col + dy
            if (
                0 <= nr < len(self.grid) and
                0 <= nc < len(self.grid[0]) and
                self.grid[nr][nc] != -1 and
                (nr, nc) not in path
            ):
                path.add((nr, nc))
                self.backtrack(nr, nc, path)
                path.remove((nr, nc))