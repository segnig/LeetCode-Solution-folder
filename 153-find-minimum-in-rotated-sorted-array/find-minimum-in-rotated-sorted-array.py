class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        current_min = float('inf')

        while left <= right:
            mid = (right + left)// 2
            current_min = min(current_min, nums[mid])
            if nums[right] < nums[mid]:
                left = mid + 1 
            else:
                right = mid - 1
                
        return min(current_min, nums[left])
