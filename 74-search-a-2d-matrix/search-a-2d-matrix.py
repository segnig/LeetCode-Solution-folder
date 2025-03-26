class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][-1] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                break
        
        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            m = left + (right - left) // 2
            if matrix[mid][m] == target:
                return True
            elif matrix[mid][m] > target:
                right = m - 1
            else:
                left = m + 1
        return False


        


