class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1

        total_elements = cols * rows

        while True:
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            if total_elements == len(result):
                return result

            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            if total_elements == len(result):
                return result

            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

            if total_elements == len(result):
                return result

            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

            if total_elements == len(result):
                return result