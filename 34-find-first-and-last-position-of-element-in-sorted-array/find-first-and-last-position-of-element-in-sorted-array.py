class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if self.binary_search(nums, target) == -1:
            return [-1, -1]

        left = self.binary_search(nums, target)
        right = left
        mid = left

        while left > -1:
            if nums[left] != nums[mid]:
                break
            left -= 1

        while right <len(nums):
            if nums[right] != nums[mid]:
                break
            right += 1
        return [left+1, right -1]
        
    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
        

        