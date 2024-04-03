class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            for num in  nums:
                if num > target:
                    return False
                if num == target:
                    return True

        