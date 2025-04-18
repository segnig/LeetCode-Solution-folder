class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        start_color = image[sr][sc]

        queue = deque([(sr, sc)])
        if color == start_color:
            return image
        image[sr][sc] = color
        while queue:
            pixel = queue.popleft()

            for dr, dc in direction:
                n_row, n_col = dr + pixel[0], dc + pixel[1]
                if self.inbound(len(image), len(image[0]), n_row, n_col) and image[n_row][n_col] == start_color:
                    queue.append((n_row, n_col))
                    image[n_row][n_col] = color

        return image


    def inbound(self, row, col, r, c):
        return 0 <= r < row and 0 <= c < col