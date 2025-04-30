class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row, col = len(matrix), len(matrix[0])
        indegree = [[0] * col for _ in range(row)]

        for r in range(row):
            for c in range(col):
                for dx, dy in directions:
                    r_n, c_n = r + dx, c + dy
                    if 0 <= r_n < row and 0 <= c_n < col and matrix[r_n][c_n] < matrix[r][c]:
                        indegree[r][c] += 1

        queue = deque()
        for r in range(row):
            for c in range(col):
                if indegree[r][c] == 0:
                    queue.append((r, c))

        length = 0
        while queue:
            length += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dx, dy in directions:
                    r_n, c_n = r + dx, c + dy
                    if 0 <= r_n < row and 0 <= c_n < col and matrix[r_n][c_n] > matrix[r][c]:
                        indegree[r_n][c_n] -= 1
                        if indegree[r_n][c_n] == 0:
                            queue.append((r_n, c_n))

        return length
