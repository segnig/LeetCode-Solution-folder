class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        indexs = [(0, i) for i in range(len(matrix[0]))]

        for  i in range(1, len(matrix)):
            indexs.append((i, 0))

        for row, col in indexs:
            first_element = matrix[row][col]

            while row < len(matrix) and col < len(matrix[0]):
                if first_element != matrix[row][col]:
                    return False
                row, col = row + 1, col + 1

        return True   