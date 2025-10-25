class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        target = (rows - 1, cols - 1)
        
        if k >= rows + cols - 2:
            return rows + cols - 2
        
        visited = [[-1] * cols for _ in range(rows)]
        
        queue = deque([(0, 0, k - grid[0][0])])
        visited[0][0] = k - grid[0][0]
        
        steps = 0
        while queue:
            for _ in range(len(queue)):
                row, col, remain_power = queue.popleft()
                
                if (row, col) == target:
                    return steps
                
                for drow, dcol in directions:
                    new_row, new_col = row + drow, col + dcol
                    
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        new_power = remain_power - grid[new_row][new_col]
                        
                        if new_power >= 0 and new_power > visited[new_row][new_col]:
                            visited[new_row][new_col] = new_power
                            queue.append((new_row, new_col, new_power))
            
            steps += 1
        
        return -1