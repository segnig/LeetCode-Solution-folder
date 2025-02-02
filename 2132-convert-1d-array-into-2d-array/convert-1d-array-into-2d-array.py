class Solution(object):
    def construct2DArray(self, original, m, n):
        result = []
        if len(original) - m * n:
            return result
        for row in range(m):
            row_elements = []
            for col in range(n):
                element = original[row * n + col]
                row_elements.append(element)
            result.append(row_elements)
        
        return result