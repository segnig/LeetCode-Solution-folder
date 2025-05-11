class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        self.scaled_rows, self.scaled_cols = len(grid) * 3, len(grid[0]) * 3
        self.scaled_grid = [[0] * self.scaled_cols for _ in range(self.scaled_rows)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                r = i * 3
                c = j * 3
                if grid[i][j] == "\\":
                    self.scaled_grid[r][c] = 1
                    self.scaled_grid[r+1][c+1] = 1
                    self.scaled_grid[r+2][c+2] = 1
                elif grid[i][j] == "/":
                    self.scaled_grid[r][c+2] = 1
                    self.scaled_grid[r+1][c+1] = 1
                    self.scaled_grid[r+2][c] = 1

        self.visited = set()
        result = 0

        for row in range(self.scaled_rows):
            for col in range(self.scaled_cols):
                if (row, col) not in self.visited and self.scaled_grid[row][col] == 0:
                    self.dfs(row, col)
                    result += 1
        
        return result

    def dfs(self, r, c):
        if (
            r < 0 or c < 0 or
            r >= self.scaled_rows or c >= self.scaled_cols or
            self.scaled_grid[r][c] == 1 or (r, c) in self.visited
        ):
            return

        self.visited.add((r, c))
        for n_r, n_c in [(r, c+1), (r, c-1), (r-1, c), (r+1, c)]:
            self.dfs(n_r, n_c)
