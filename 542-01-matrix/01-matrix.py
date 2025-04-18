class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        result = [[0] * len(mat[0])  for _ in range(len(mat))]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque()
        
        far = 1

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j))

        while queue:

            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    n_row, n_col = row + dr, col + dc

                    if self.inbound(len(mat), len(mat[0]), n_row, n_col) and mat[n_row][n_col] == 1 and result[n_row][n_col] == 0:
                        result[n_row][n_col] = far
                        queue.append((n_row, n_col))   
            far += 1

        return result           

    def inbound(self, row, col, r, c):
        return 0 <= r < row and 0 <= c < col 


