class Solution(object):  
    def matrixBlockSum(self, mat, k):  
        if not mat or not mat[0]:  
            return []  

        row, col = len(mat), len(mat[0])  
         
        prefix_sum = [[0] * (col + 1) for _ in range(row + 1)]  

        for i in range(row):  
            for j in range(col):  
                prefix_sum[i + 1][j + 1] = (  
                    mat[i][j]  
                    + prefix_sum[i][j + 1]  
                    + prefix_sum[i + 1][j]  
                    - prefix_sum[i][j]  
                )  
 
        result = [[0] * col for _ in range(row)]  

        for i in range(row):  
            for j in range(col):  

                r1 = max(0, i - k)  
                r2 = min(row - 1, i + k)  
                c1 = max(0, j - k)  
                c2 = min(col - 1, j + k)  

                result[i][j] = (  
                    prefix_sum[r2 + 1][c2 + 1]  
                    - prefix_sum[r1][c2 + 1]  
                    - prefix_sum[r2 + 1][c1]  
                    + prefix_sum[r1][c1]  
                )  

        return result