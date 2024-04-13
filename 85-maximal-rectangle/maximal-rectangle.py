class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        matsum = [[0]*( len(matrix[0])) for i in range(len(matrix))]
        T = True
        gg = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1" and T and j > 0:
                    matsum[i][j] = matsum[i][j - 1] + 1
                elif matrix[i][j] == "1":
                    matsum[i][j] = 1
                else:
                    matsum[i][j] = 0
                
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                c = 0
                h = i
                mn = matsum[i][j]
                while h > -1:
                    if matsum[h][j] == 0:
                        break
                    c += 1
                    mn = min(mn, matsum[h][j])
                    ans = max(ans, c * mn)
                    h -= 1
                ans = max(ans, matsum[i][j])
        return ans