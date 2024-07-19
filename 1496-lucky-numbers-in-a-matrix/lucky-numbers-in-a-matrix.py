class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        result = []

        trans = []
        for j in range(len(matrix[0])):
            row = []
            for i in range(len(matrix)):
                row.append(matrix[i][j])
            trans.append(row)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == max(trans[j]) == min(matrix[i]):
                    result.append(matrix[i][j])

        return result    