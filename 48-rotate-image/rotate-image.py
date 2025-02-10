class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        for i in range(N//2):
            for j in range(ceil(N/2)):
                matrix[i][j], matrix[j][N-i-1], matrix[N-i-1][N-j-1], matrix[N-j-1][i] = matrix[N-j-1][i], matrix[i][j], matrix[j][N-i-1], matrix[N-i-1][N-j-1]
                
        