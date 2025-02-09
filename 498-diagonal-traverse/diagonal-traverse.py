class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []  
        total_elements = len(mat) * len(mat[0])  
        row, col = 0, 0  

        while len(result) < total_elements:  
            
            while row >= 0 and col < len(mat[0]):  
                result.append(mat[row][col])  
                row, col = row - 1, col + 1  

              
            if col >= len(mat[0]):  
                col = len(mat[0]) - 1  
                row += 2 

            row = max(row, 0)   

             
            if len(result) == total_elements:  
                return result   

             
            while row < len(mat) and col >= 0:  
                result.append(mat[row][col])  
                row, col = row + 1, col - 1  
  
            if row >= len(mat):   
                row = len(mat) - 1  
                col += 2   

            col = max(col, 0)  
            
            if len(result) == total_elements:  
                return result   
            
        return result  