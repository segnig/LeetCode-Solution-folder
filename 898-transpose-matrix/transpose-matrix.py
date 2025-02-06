class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        matrix_trans = [[0 for _ in range(len(matrix))] for p in range(len(matrix[0]))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                matrix_trans[col][row] = matrix[row][col]

        return matrix_trans