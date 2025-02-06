class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros_indexs = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if not matrix[row][col]:
                    zeros_indexs.add((row, col))

        for row, col in zeros_indexs:
            self.helper(row, col, matrix)

    def helper(self, row, col, matrix):
        for c in range(len(matrix[0])):
            matrix[row][c] = 0

        for r in range(len(matrix)):
            matrix[r][col] = 0
    