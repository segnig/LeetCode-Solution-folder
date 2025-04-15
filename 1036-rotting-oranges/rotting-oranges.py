class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.grid = grid
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        result = -1
        queue = deque()
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))
                if self.grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
            
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if self.inbound(nr, nc) and self.grid[nr][nc] != 0 and( (nr, nc) not in visited):
                        fresh -= 1
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            result += 1
        
        return result if fresh == 0 else -1

    def inbound(self, row, col):
        return 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0])