class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        for  i in range(1, len(matrix)):
            test = self.helper(i, 0, matrix)
            if not test:
                return False

        for i in range(len(matrix[0])):
            test = self.helper(0, i, matrix)
            if not test:
                return False

        return True
          

    def helper(self, row, col, matrix): 
        first_element = matrix[row][col]

        while row < len(matrix) and col < len(matrix[0]):
            if first_element != matrix[row][col]:
                return False
            row, col = row + 1, col + 1

        return True 