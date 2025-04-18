class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        result = [[0] * len(isWater[0])  for _ in range(len(isWater))]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque()
        
        far = 1

        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    queue.append((i, j))

        while queue:

            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    n_row, n_col = row + dr, col + dc

                    if self.inbound(len(isWater), len(isWater[0]), n_row, n_col) and isWater[n_row][n_col] == 0 and result[n_row][n_col] == 0:
                        result[n_row][n_col] = far
                        queue.append((n_row, n_col))   
            far += 1

        return result           

    def inbound(self, row, col, r, c):
        return 0 <= r < row and 0 <= c < col